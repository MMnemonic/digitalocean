import logging
import traceback

from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from ipware import get_client_ip
import ipinfo

LOGGER = logging.getLogger(__name__)
salogger = logging.getLogger('main_app.stonealgo')


class IPinfo(MiddlewareMixin):
    def __init__(self, get_response=None):
        """Initializes class while gettings user settings and creating the cache."""
        self.get_response = get_response
        self.filter = getattr(settings, "IPINFO_FILTER", self.is_bot)

        self.is_debug = getattr(settings, "DEBUG")

        ipinfo_token = getattr(settings, "IPINFO_TOKEN", None)
        ipinfo_settings = getattr(settings, "IPINFO_SETTINGS", {})
        self.ipinfo = ipinfo.getHandler(ipinfo_token, **ipinfo_settings)

    def process_request(self, request):
        """Middleware hook that acts on and modifies request object."""
        if not self.is_debug or self.is_debug:
            try:
                if self.filter and self.filter(request):
                    request.ipinfo = None
                else:
                    ip_add = self.return_ip(request)
                    request.ipinfo = self.ipinfo.getDetails(ip_add)
            except Exception as exc:
                request.ipinfo = None
                LOGGER.error(traceback.format_exc())

    def is_bot(self, request):
        """Whether or not the request user-agent self-identifies as a bot"""
        lowercase_user_agent = request.META.get("HTTP_USER_AGENT", "").lower()
        return "bot" in lowercase_user_agent or "spider" in lowercase_user_agent

    def return_ip(self, request):

        try:
            ip, _ = get_client_ip(request)

            # salogger.info("Get Client IP: {0} - {1}".format(ip, _))

            if ip == '127.0.0.1':
                ip = '107.115.17.142'

            if ":" in ip:
                ip = ip.split(":")[0]
        except Exception as exc:
            ip = None
            salogger.error(traceback.format_exc())

        return ip

try:
    from account.mixins import LoginRequiredMixin
except ImportError:
    from django.contrib.auth.mixins import LoginRequiredMixin  # noqa


try:
    from unittest import mock
except ImportError:
    import mock  # noqa

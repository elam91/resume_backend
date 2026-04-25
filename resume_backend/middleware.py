from os import getenv
import zoneinfo  # <--- Use this instead of pytz
from django.utils import timezone


class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the TZ string from the environment
        environment_timezone = getenv('USER_TZ', 'Asia/Jerusalem')

        try:
            # Create a ZoneInfo object
            activated_timezone = zoneinfo.ZoneInfo(environment_timezone)
            timezone.activate(activated_timezone)
        except zoneinfo.ZoneInfoNotFoundError:
            # Fallback to UTC or a default if the env var is invalid
            timezone.activate(zoneinfo.ZoneInfo('UTC'))

        return self.get_response(request)
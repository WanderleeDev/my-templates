import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration
from src.core import settings


def init_sentry():
    sentry_logging = LoggingIntegration(level=20, event_level=40)

    sentry_sdk.init(
        dsn=settings.SENTRY_DNS,
        # Add data like request headers and IP for users,
        # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
        send_default_pii=True,
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for tracing.
        traces_sample_rate=1.0,
        # Set profile_session_sample_rate to 1.0 to profile 100%
        # of profile sessions.
        profile_session_sample_rate=1.0,
        # Set profile_lifecycle to "trace" to automatically
        # run the profiler on when there is an active transaction
        profile_lifecycle="trace",
        integrations=[sentry_logging],
    )

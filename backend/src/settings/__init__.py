from os import environ

from split_settings.tools import include, optional

ENVIRONMENT = environ.get("APP_ENVIRONMENT")

assert ENVIRONMENT in ("development", "staging", "production")

base_settings = [
    "components/base.py",
    "components/database.py",
    "components/loggers.py",
    "components/celery.py",
    # Environment setting override:
    "environments/{0}.py".format(ENVIRONMENT),
    # Optional setting override:
    optional("environments/local_override.py"),
]

include(*base_settings)

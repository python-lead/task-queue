LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "faker": {
            "handlers": ["console"],
            "level": "INFO",
        },
        "factory": {
            "handlers": ["console"],
            "level": "INFO",
        },
    },
}

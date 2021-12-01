import os
import structlog

from typing import Union

from structlog.dev import ConsoleRenderer
from structlog.processors import JSONRenderer

from .settings import DEBUG


LOGGING_LEVEL = os.environ.get("LOGGING_LEVEL", default="DEBUG")

if DEBUG:
    LOGGING_PROCESSOR: Union[ConsoleRenderer, JSONRenderer] = ConsoleRenderer()
else:
    LOGGING_PROCESSOR = JSONRenderer()

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "logging_formatter": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processor": LOGGING_PROCESSOR,
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "logging_formatter",
        },
    },
    "loggers": {
        "root": {
            "handlers": [
                "console",
            ],
            "level": LOGGING_LEVEL,
        },
    },
}

structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
    ],
    context_class=structlog.threadlocal.wrap_dict(dict),
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)

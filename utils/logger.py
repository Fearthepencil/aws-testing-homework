"""
Logging configuration
"""

import sys
from loguru import logger


def setup_logger():
    """Configure loguru logger for test execution"""

    # Remove default handler
    logger.remove()

    # Add console handler with custom format
    log_format = (
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
    )
    logger.add(
        sys.stdout,
        format=log_format,
        level="INFO",
        colorize=True,
    )

    # Add file handler for detailed logs
    logger.add(
        "test_execution.log",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        level="DEBUG",
        rotation="10 MB",
        retention="7 days",
    )

    logger.info("Logger configured successfully")
    return logger


# Initialize logger when module is imported
setup_logger()

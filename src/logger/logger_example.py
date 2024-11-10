import logging
import os
from datetime import datetime

# Setup log filename with current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the log path and ensure the directory exists
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(os.path.dirname(log_path), exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=log_path,
    filemode="w",
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Get a logger instance
logger = logging.getLogger(__name__)

# Example usage of different log levels
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
logger.debug("This is a debug message")

# Example of logging an exception (within an exception block)
try:
    raise ValueError("An example exception")
except ValueError as e:
    logger.exception("An exception occurred")

# Example of using a custom log level (50)
logger.log(50, "This is a log message with level 50")

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

# Get a logger instance and rename it to `logger_example`
logger_example = logging.getLogger(__name__)

# Example usage of different log levels
logger_example.info("This is an info message")
logger_example.warning("This is a warning message")
logger_example.error("This is an error message")
logger_example.critical("This is a critical message")
logger_example.debug("This is a debug message")

# Example of logging an exception (within an exception block)
try:
    raise ValueError("An example exception")
except ValueError as e:
    logger_example.exception("An exception occurred")

# Example of using a custom log level (50)
logger_example.log(50, "This is a log message with level 50")

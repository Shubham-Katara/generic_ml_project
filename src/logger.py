# The logging library in Python is a built-in module that provides a flexible and customizable framework for logging messages in your Python programs
import logging
import os
from datetime import datetime

# creating log file
# f"{}" syntax is used to create formatted strings
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# creating path and directory for the log file
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# config the loggging system
# filename: Specifies the name of the log file where log messages will be written. 
# level: Sets the root logger's level. Only log messages at or above this level will be emitted. The available levels, in increasing order of severity, are DEBUG, INFO, WARNING, ERROR, and CRITICAL.
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# if __name__=="__main__":
#     logging.info("Logging has started")
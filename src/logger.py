# Imports
import logging
from datetime import datetime
from logger_error import LoggerError

# Logger class definition
class Logger:
    def __init__(self,
                    application_name,
                    logging_level = logging.DEBUG,
                    file_name = None,
                    file_mode = "a",
                    message_format = "%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
                    date_format = "%H:%M:%S"):

        # Raise error if no application_name
        if application_name is None:
            raise LoggerError("Application name is required.")
        # Get current date time
        current_date_time = datetime.now()
        # Set default file name
        default_file_name = file_name if file_name is not None else (f"{current_date_time.year}-"
            f"{current_date_time.month}-"
            f"{current_date_time.day}-"
            f"{current_date_time.hour}-"
            f"{current_date_time.minute}-"
            f"{current_date_time.second}-"
            f"{application_name}.log")
        # Configure the logger
        logging.basicConfig(level = logging_level,
                            format = message_format,
                            datefmt = date_format,
                            filename = default_file_name,
                            filemode = file_mode)
        # Create the logger
        self._logger = logging.getLogger(application_name)
        # Create the method lookup dictionary
        self._function_map = dict(debug = "write_debug",
                                  info = "write_info",
                                  warning = "write_warning",
                                  error = "write_error",
                                  critical = "write_critical")

    # Simplified log method to call correct logging method
    def log(self, level, message):
        # Raise error if level is null
        if level is None:
            raise LoggerError("Logging Level is required.")
        # Raise error if message is null
        if message is None:
            raise LoggerError("Message is required")
        elif level.lower() in self._function_map:
                getattr(self, self._function_map[level])(message)

    # Write debug message to log file
    def write_debug(self, message):
        self._logger.debug(message)
    
    # Write info message to log file
    def write_info(self, message):
        self._logger.info(message)
    
    # Write warning message to log file
    def write_warning(self, message):
        self._logger.warning(message)
    
    # Write error message to log file
    def write_error(self, message):
        self._logger.error(message)
    
    # Write critical message to log file
    def write_critical(self, message):
        self._logger.critical(message)
    
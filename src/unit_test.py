import unittest
import logging
from logger_error import LoggerError
from logger import Logger

class Test_LoggerTest(unittest.TestCase):
    # Test writing debug
    def test_logger_will_log_debug(self):
        application_name = "Unit Test Application"
        file_name = "unit-test.log"
        log_message = "We have written our first debug line"
        expected_message = f"{application_name} DEBUG {log_message}"
        self._logger = Logger(application_name, logging.DEBUG, file_name)
        self._logger.log("debug", log_message)
        with open(file_name, "r") as file:
            first_line = file.readline()
            for file_line in file:
                pass
        log_file_message = " ".join(file_line.split()[1:])
        self.assertEqual(log_file_message, expected_message)

    # Test writing info
    def test_logger_will_log_info(self):
        application_name = "Unit Test Application"
        file_name = "unit-test.log"
        log_message = "We have written our first info line"
        expected_message = f"{application_name} INFO {log_message}"
        self._logger = Logger(application_name, logging.DEBUG, file_name)
        self._logger.log("info", log_message)
        with open(file_name, "r") as file:
            first_line = file.readline()
            for file_line in file:
                pass
        log_file_message = " ".join(file_line.split()[1:])
        self.assertEqual(log_file_message, expected_message)

    # Test writing warning
    def test_logger_will_log_warning(self):
        application_name = "Unit Test Application"
        file_name = "unit-test.log"
        log_message = "We have written our first warning line"
        expected_message = f"{application_name} WARNING {log_message}"
        self._logger = Logger(application_name, logging.DEBUG, file_name)
        self._logger.log("warning", log_message)
        with open(file_name, "r") as file:
            first_line = file.readline()
            for file_line in file:
                pass
        log_file_message = " ".join(file_line.split()[1:])
        self.assertEqual(log_file_message, expected_message)

    # Test writing error
    def test_logger_will_log_error(self):
        application_name = "Unit Test Application"
        file_name = "unit-test.log"
        log_message = "We have written our first error line"
        expected_message = f"{application_name} ERROR {log_message}"
        self._logger = Logger(application_name, logging.DEBUG, file_name)
        self._logger.log("error", log_message)
        with open(file_name, "r") as file:
            first_line = file.readline()
            for file_line in file:
                pass
        log_file_message = " ".join(file_line.split()[1:])
        self.assertEqual(log_file_message, expected_message)

    # Test writing critical
    def test_logger_will_log_critical(self):
        application_name = "Unit Test Application"
        file_name = "unit-test.log"
        log_message = "We have written our first critical line"
        expected_message = f"{application_name} CRITICAL {log_message}"
        self._logger = Logger(application_name, logging.DEBUG, file_name)
        self._logger.log("critical", log_message)
        with open(file_name, "r") as file:
            first_line = file.readline()
            for file_line in file:
                pass
        log_file_message = " ".join(file_line.split()[1:])
        self.assertEqual(log_file_message, expected_message)

    # Test exception for missing application name
    def test_logger_will_throw_exception_without_application_name(self):
        try:
            self._logger = Logger(None)
        except LoggerError as e:
            error = e.args[0]
            self.assertEqual(error, "Application name is required.")

    # Test exception for missing logging level
    def test_logger_will_throw_exception_without_logging_level(self):
        application_name = "Unit Test Application"
        file_name = "unit-test.log"
        log_message = "We have written our first debug line"
        expected_message = f"{application_name} DEBUG {log_message}"
        self._logger = Logger(application_name, logging.DEBUG, file_name)
        try:
            self._logger.log(None, log_message)
        except LoggerError as e:
            error = e.args[0]
            self.assertEqual(error, "Logging Level is required.")

    # Test exception for no logging message
    def test_logger_will_throw_exception_without_logging_message(self):
        application_name = "Unit Test Application"
        file_name = "unit-test.log"
        log_message = "We have written our first debug line"
        expected_message = f"{application_name} DEBUG {log_message}"
        self._logger = Logger(application_name, logging.DEBUG, file_name)
        try:
            self._logger.log("debug", None)
        except LoggerError as e:
            error = e.args[0]
            self.assertEqual(error, "Logging Message is required.")

if __name__ == '__main__':
    unittest.main()
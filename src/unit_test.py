import unittest
import logging
from logger import Logger

class Test_LoggerTest(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()
import logging
from logging.handlers import TimedRotatingFileHandler
import datetime
import os

from requests import Response


class Logger:
    log_directory = "logs"  # Directory for logs
    base_directory = os.path.dirname(os.path.realpath(__file__))  # Get the directory where this file is located
    full_log_directory = os.path.join(base_directory, log_directory)  # Full path to the logs directory

    # Ensure the logs directory exists
    if not os.path.exists(full_log_directory):
        os.makedirs(full_log_directory)

    # Full path for the log file, using the full_log_directory
    log_file_path = os.path.join(full_log_directory, "log.log")  # Using a single log file name, rotated by TimedRotatingFileHandler

    logger = logging.getLogger('Logger')
    logger.setLevel(logging.INFO)

    file_handler = TimedRotatingFileHandler(
        log_file_path,
        when='midnight',
        interval=1,
        backupCount=3,
        encoding='utf-8'
    )

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    @classmethod
    def add_request(cls, url: str, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST', 'Unknown Test')
        cls.logger.info(f"Test: {test_name}")
        cls.logger.info(f"Request method: {method}")
        cls.logger.info(f"Request URL: {url}")

    @classmethod
    def add_response(cls, result: Response):
        cookies_as_dict = dict(result.cookies)
        headers_as_dict = dict(result.headers)

        cls.logger.info(f"Response code: {result.status_code}")
        cls.logger.info(f"Response text: {result.text}")
        cls.logger.info(f"Response headers: {headers_as_dict}")
        cls.logger.info(f"Response cookies: {cookies_as_dict}")

from requests import Response
from src.enums.global_errors import GlobalErrorMessages
"""Check's methods for our response"""


class Checking():
    """Status code checking method"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        print(f'Status code: {status_code} successful!')


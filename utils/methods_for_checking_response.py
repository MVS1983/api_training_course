from requests import Response
from src.enums.global_errors import GlobalErrorMessages


"""Check's methods for our response"""


class Checking:
    """Status code checking method"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        print(f'Status code: {status_code} successful!')

    """Required fields' check method in request response"""
    @staticmethod
    def check_json_field(response: Response, expected_field):
        token = response.json()
        assert list(token) == expected_field, GlobalErrorMessages.WRONG_KEY_FIELD.value
        print("All fields are present")

    """Required value check method in request response"""
    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_value = check.get(field_name)
        assert check_value == expected_value, GlobalErrorMessages.WRONG_VALUE.value
        print(f"{field_name} value is correct")

    """Required certain value check method in request response"""
    @staticmethod
    def check_json_certain_value(response: Response, field_name, certain_value):
        check = response.json()
        check_value = check.get(field_name)
        if certain_value in check_value:
            print(f"{certain_value} value is correct")
        else:
            print(f"{certain_value} isn't correct")


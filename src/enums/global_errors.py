from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Received status code is not equal to expected"
    WRONG_KEY_FIELD = "Not all fields are present"
    WRONG_VALUE = "Wrong value"

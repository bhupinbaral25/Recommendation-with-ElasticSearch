import json
from pydantic import ValidationError
from fastapi import HTTPException


def error_handler(func):
    """Decorator used to catch certain types of Exceptions"""

    def validate(*args, **kwargs):
        try:
            to_return = func(*args, **kwargs)
        except ValidationError as e:
            errors = []
            errors_list = json.loads(e.json())
            for error in errors_list:
                errors.append({"attribute": error["loc"][0], "msg": error["msg"]})
            return {
                "statusCode": 400,
                "body": errors,
            }
        except HTTPException as e:
            return {
		"statusCode": e.status_code,
		"body": e.detail,
	    }
        except Exception as e:
            print(e)
            raise e
        return to_return

    return validate
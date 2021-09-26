import json

from aws_lambda_powertools import Logger

from src.helper.tools import ApiHelper
from src.controller.user import UserController

logger = Logger(service="SaveUser")


@logger.inject_lambda_context
def handler(event, context):
    logger.debug(event)

    response = {"statusCode": 404, "body": json.dumps(event)}

    input_data = ApiHelper.get_input_data(event)
    username = ApiHelper.get_path_parameter(event, "username")

    logger.debug(f"username[{username}]")
    logger.debug(f"input_data[{input_data}]")

    user_controller = UserController(logger=logger)

    try:
        user_controller.save_user(username=username, dateOfBirth=input_data["dateOfBirth"])
        response = {"statusCode": 204}

    except Exception as e:
        logger.exception(e)

    logger.debug(response)

    return response

import json

from aws_lambda_powertools import Logger

from src.helper.tools import ApiHelper
from src.controller.user import UserController

logger = Logger(service="GetUser")


@logger.inject_lambda_context
def handler(event, context):
    logger.debug(event)

    response = {"statusCode": 404, "body": json.dumps(event)}

    username = ApiHelper.get_path_parameter(event, "username")

    logger.debug(f"username[{username}]")

    user_controller = UserController(logger=logger)

    try:
        user_message = user_controller.get_user_message(username=username)
        if user_message:
            response = {"statusCode": 200, "body": json.dumps({"message": user_message})}

    except Exception as e:
        logger.exception(e)

    logger.debug(response)

    return response

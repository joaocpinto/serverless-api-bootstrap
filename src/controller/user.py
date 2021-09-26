import json

from aws_lambda_powertools import Logger

from datetime import date
from src.helper.config import Config
from src.service.dynamodb import DynamoDbService
from src.model.user import UserModel


class UserController:
    """
    Class containing user logic
    """

    def __init__(self, logger: Logger = None):
        self.__dynamodb_service = DynamoDbService(Config.DYNAMODB_TABLE.value)
        self.__logger = logger if logger else Logger(service="UserController")

    def __convert_to_dict(self, user: UserModel) -> dict:
        user_dict = json.loads(user.json())

        return user_dict

    def save_user(self, username: str, dateOfBirth: date):
        self.__logger.info("Saving an user...")
        user = UserModel(username=username, dateOfBirth=dateOfBirth)

        self.__dynamodb_service.put_item(item=self.__convert_to_dict(user))

    def get_user(self, username: str):
        self.__logger.info("Getting an user...")
        existing_user = self.__dynamodb_service.get_item(username=username)

        if existing_user is None:
            return None

        user = UserModel(**existing_user)
        return user

    def get_user_message(self, username: str):
        self.__logger.info("Getting an user message...")
        user_message = ""
        user = self.get_user(username)
        if user:
            if user.is_birthday():
                user_message = f"Hello, {user.username}! Happy birthday!"
            else:
                user_message = f"Hello, {user.username}! Your date of birth is {user.dateOfBirth}"

        return user_message

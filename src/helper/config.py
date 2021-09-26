import os
from enum import Enum


class Config(Enum):

    REGION = os.getenv("REGION")
    DYNAMODB_TABLE = os.getenv("DYNAMODB_TABLE")

    def __str__(self):
        return str(self.value)

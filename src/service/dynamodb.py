import boto3
from src.helper.config import Config


class DynamoDbService:
    def __init__(self, table_name: str, region_name=Config.REGION.value):
        self.resource = boto3.resource("dynamodb", region_name)
        self.__table = self.resource.Table(table_name)

    def get_item(self, username: str):
        try:
            result = self.__table.get_item(Key={"username": username})
            return result["Item"] if "Item" in result else None
        except Exception as e:
            error_message = "{0} Except: {1}".format("Error get_item from DynamoDB", str(e))
            raise Exception(error_message)

    def put_item(self, item):
        try:
            response = self.__table.put_item(Item=item)
            return response
        except Exception as e:
            error_message = "{0} Except: {1}".format("Error put_item in DynamoDB", str(e))
            raise Exception(error_message)

import json


class ApiHelper:
    """
    API class to help parse params and arguments
    """

    @staticmethod
    def get_input_data(event: dict):
        input_data = None if not (event and event["body"]) else json.loads(event["body"])

        return input_data

    @staticmethod
    def get_path_parameter(event: dict, param_name: str):
        try:
            parameter = event["pathParameters"][param_name]
        except Exception:
            parameter = None

        return parameter

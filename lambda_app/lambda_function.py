import json
from app import add, subtract, multiply, divide


def lambda_handler(event, context):
    try:
        # Accept input from API Gateway or a direct Lambda event
        if isinstance(event.get("body"), str):
            data = json.loads(event["body"])
        elif isinstance(event.get("body"), dict):
            data = event["body"]
        else:
            data = event

        operation = data.get("operation")
        num1 = float(data["num1"])
        num2 = float(data["num2"])

        operations = {
            "add": add,
            "subtract": subtract,
            "multiply": multiply,
            "divide": divide,
        }

        if operation not in operations:
            raise ValueError(
                "Operation must be add, subtract, multiply, or divide."
            )

        result = operations[operation](num1, num2)

        if isinstance(result, str):
            return {
                "statusCode": 400,
                "body": json.dumps({"error": result}),
            }

        return {
            "statusCode": 200,
            "body": json.dumps({"result": result}),
        }

    except (KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": str(error)}),
        }
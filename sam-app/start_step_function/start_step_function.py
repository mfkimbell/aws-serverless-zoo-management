import json
import boto3
import os
import logging

# Initialize Step Functions client
client = boto3.client("stepfunctions")

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info("Received event: %s", json.dumps(event))

    state_machine_arn = os.environ["STATE_MACHINE_ARN"]

    # Parse the incoming API Gateway event
    body = event.get("body")
    if body:
        logger.info("Parsed body: %s", body)
        try:
            body = json.loads(body)
            logger.info("Loaded body JSON: %s", json.dumps(body))
        except json.JSONDecodeError as e:
            logger.error("Error parsing JSON body: %s", str(e))
            return {"statusCode": 400, "body": json.dumps({"message": "Invalid JSON"})}

    # Extract the required fields from the parsed body
    input_data = body.get("input", {})
    input_details = body.get("inputDetails", {})
    role_arn = body.get("roleArn")

    logger.info("Extracted input_data: %s", json.dumps(input_data))
    logger.info("Extracted input_details: %s", json.dumps(input_details))
    logger.info("Extracted role_arn: %s", role_arn)

    # Construct the input to match the expected format
    step_function_input = {"input": input_data, "inputDetails": input_details}

    if role_arn:
        step_function_input["roleArn"] = role_arn

    logger.info("Constructed step function input: %s", json.dumps(step_function_input))

    try:
        response = client.start_execution(
            stateMachineArn=state_machine_arn,
            input=json.dumps(step_function_input, default=str),
        )
        logger.info("Start execution response: %s", json.dumps(response, default=str))
        return {"statusCode": 200, "body": json.dumps(response, default=str)}
    except Exception as e:
        logger.error("Error starting step function execution: %s", str(e))
        return {"statusCode": 500, "body": json.dumps({"message": str(e)})}

import boto3
import json
import uuid
import logging
from datetime import datetime

# Initialize DynamoDB client
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("SamZooRegistry")

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    try:
        # Log the incoming event
        logger.info("Received event: %s", json.dumps(event))

        # Extract species and feedingSchedule from the event
        species = event.get("species")
        feeding_schedule = event.get("feedingSchedule")

        if not species or not feeding_schedule:
            logger.error("Missing species or feedingSchedule in the event")
            return {
                "statusCode": 400,
                "body": json.dumps(
                    {"message": "species and feedingSchedule are required"}
                ),
            }

        # Generate a unique animal ID and get the current time
        animal_id = str(uuid.uuid4())
        now = datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time

        # Create the item to be inserted into DynamoDB
        item = {
            "animalId": animal_id,
            "species": species,
            "feedingSchedule": feeding_schedule,
            "dateOfBirth": now,
            "lastFed": now,
        }

        # Log the item being inserted
        logger.info(
            "Registering animal with ID: %s, Data: %s", animal_id, json.dumps(item)
        )

        # Put the item into the DynamoDB table
        table.put_item(Item=item)

        logger.info("Animal registered successfully with ID: %s", animal_id)

        return {
            "statusCode": 201,
            "body": json.dumps(
                {"message": "Animal registered successfully", "animalId": animal_id}
            ),
        }

    except Exception as e:
        logger.error("Error registering animal: %s", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({"message": f"Error registering animal: {str(e)}"}),
        }

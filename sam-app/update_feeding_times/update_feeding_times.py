import boto3
import json
import logging
from datetime import datetime, timedelta

# Initialize DynamoDB client
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("SamZooRegistry")

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    try:
        # Log the incoming event
        logger.info("Feeding event triggered: %s", json.dumps(event))

        # Get the current UTC time
        now_utc = datetime.utcnow()
        logger.info("Current UTC time: %s", now_utc.isoformat())

        # Convert UTC time to Central Time (CDT, which is UTC-5)
        now_cdt = now_utc - timedelta(hours=5)
        logger.info("Current Central Daylight Time: %s", now_cdt.isoformat())

        # Floor the current UTC time to the nearest hour
        floored_utc = now_utc.replace(minute=0, second=0, microsecond=0)
        floored_hour_utc = floored_utc.hour
        logger.info("Floored time (nearest hour in UTC): %s", floored_utc.isoformat())
        logger.info("Floored hour in UTC: %d", floored_hour_utc)

        # Floor the current CDT time to the nearest hour for comparison
        floored_cdt = now_cdt.replace(minute=0, second=0, microsecond=0)
        floored_hour_cdt = floored_cdt.hour
        logger.info("Floored time (nearest hour in CDT): %s", floored_cdt.isoformat())
        logger.info("Floored hour in CDT: %d", floored_hour_cdt)

        # Scan the table for all animals
        response = table.scan()
        animals = response.get("Items", [])
        logger.info("Number of animals found: %d", len(animals))

        # Update the lastFed time for each animal if the floored time matches their feeding schedule
        for animal in animals:
            animal_id = animal["animalId"]
            feeding_schedule = animal.get("feedingSchedule", [])
            logger.info("Checking feeding schedule for animal ID: %s", animal_id)
            logger.info("Feeding schedule: %s", feeding_schedule)

            match_found = False
            for scheduled_time in feeding_schedule:
                # Convert feeding time to 24-hour format and compare
                scheduled_hour = datetime.strptime(scheduled_time, "%I:%M %p").hour
                logger.info("Scheduled feeding hour: %d", scheduled_hour)
                if (
                    scheduled_hour == floored_hour_utc
                    or scheduled_hour == floored_hour_cdt
                ):
                    match_found = True
                    logger.info(
                        "Match found: Floored hour %d matches scheduled hour %d for animal ID: %s",
                        floored_hour_utc,
                        scheduled_hour,
                        animal_id,
                    )
                    break

            if match_found:
                logger.info("Updating lastFed time for animal ID: %s", animal_id)
                table.update_item(
                    Key={"animalId": animal_id},
                    UpdateExpression="SET lastFed = :val1",
                    ExpressionAttributeValues={":val1": floored_utc.isoformat() + "Z"},
                )
                logger.info(
                    "Successfully updated lastFed time for animal ID: %s", animal_id
                )
            else:
                logger.info(
                    "No matching feeding time found for animal ID: %s", animal_id
                )

        return {
            "statusCode": 200,
            "body": json.dumps(
                {"message": "Feeding times checked and updated if necessary"}
            ),
        }

    except Exception as e:
        logger.error("Error updating feeding times: %s", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({"message": f"Error updating feeding times: {str(e)}"}),
        }

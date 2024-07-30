import json
import boto3
import os
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
table_name = os.environ["TABLE_NAME"]
table = dynamodb.Table(table_name)


def populate_zoo_registry(event, context):
    current_time = datetime.utcnow().isoformat() + "Z"
    animals = [
        {
            "animalId": "1",
            "species": "Elephant",
            "feedingSchedule": ["10:00 AM", "02:00 PM", "08:00 PM"],
            "dateOfBirth": current_time,
            "lastFed": current_time,
        },
        {
            "animalId": "2",
            "species": "Lion",
            "feedingSchedule": ["09:00 AM", "01:00 PM", "05:00 PM"],
            "dateOfBirth": current_time,
            "lastFed": current_time,
        },
        {
            "animalId": "3",
            "species": "Giraffe",
            "feedingSchedule": ["07:00 AM", "11:00 AM", "04:00 PM"],
            "dateOfBirth": current_time,
            "lastFed": current_time,
        },
        {
            "animalId": "4",
            "species": "Zebra",
            "feedingSchedule": ["06:00 AM", "12:00 PM", "06:00 PM"],
            "dateOfBirth": current_time,
            "lastFed": current_time,
        },
        {
            "animalId": "5",
            "species": "Panda",
            "feedingSchedule": ["08:00 AM", "12:00 PM", "04:00 PM"],
            "dateOfBirth": current_time,
            "lastFed": current_time,
        },
    ]

    for animal in animals:
        table.put_item(Item=animal)

    return {"statusCode": 200, "body": json.dumps("ZooRegistry populated successfully")}

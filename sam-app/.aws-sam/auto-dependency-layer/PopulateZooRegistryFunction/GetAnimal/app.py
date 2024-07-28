# import boto3
# import json

# # Initialize DynamoDB client
# dynamodb = boto3.resource('dynamodb')
# table = dynamodb.Table('ZooRegistry')

# def lambda_handler(event, context):
#     print(event)
    
#     # Extract animalId from the query string parameters
#     animal_id = event.get('queryStringParameters', {}).get('animalId')
    
#     if not animal_id:
#         return {
#             'statusCode': 400,
#             'body': json.dumps({'message': 'animalId is required'})
#         }
    
#     try:
#         # Query DynamoDB table 'ZooRegistry' for animalId
#         response = table.get_item(Key={'animalId': animal_id})  # Correctly provide the key
#         animal = response.get('Item', None)
        
#         if not animal:
#             return {
#                 'statusCode': 404,
#                 'body': json.dumps({'message': 'Animal not found'})
#             }
        
#         return {
#             'statusCode': 200,
#             'body': json.dumps(animal)  # Return the JSON object directly
#         }
#     except Exception as e:
#         return {
#             'statusCode': 500,
#             'body': json.dumps({'message': f'Error retrieving animal: {str(e)}'})
#         }

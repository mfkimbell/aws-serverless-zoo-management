# aws-serverless-zoo-management

## What this application does
It uses AWS SAM to creat a zoo animal registry

## Setup VScode with SAM
* ``` brew install aws cli ``` installs aws cli
* ``` aws configure ``` sync with account 
* ``` brew tap aws/tap ``` wrapper
* ``` brew install aws-sam-cli ``` install sam cli
* ``` sam -h ``` to check if it works

## Sam Commands to know
* ``` sam init ``` create sam template
* ``` sam validate ``` validates syntax of template
* ``` sam deploy --guided ``` deploy the sam template
* ``` sam sync --stack-name sam-app --watch ``` sync application to automatically make different udpates depending on saved changes
* ``` sam logs --stack-name sam-app --tail ``` locally streams all logs to terminal

## Lambda Functions

* **register_animal:** takes in a list of animals and adds them to a dynamoDB database. If they don't already have a birth date, it assumes they've just been born and gives them a DOB.
* **start_step_function:** used to initiate the step function from the "registerAll" API route
* **test_populate_zoo_registry:** initiates some test data to work with in the database
* **update_feeding_times:** scans the database, if the current floored time matches one of the feeding times, it updates the "lastFed" field for the animals that match. An eventbridge eventbus bus rule triggers this function every hour. 

## Example POST to API for registering

``` python
curl -X POST https://2dkpi4e09c.execute-api.us-east-1.amazonaws.com/Prod/registerAll \
-H "Content-Type: application/json" \
-d '{
  "input": {
    "request": {
      "animals": [
        {
          "species": "Elephant",
          "feedingSchedule": [
            "10:00 AM",
            "02:00 PM",
            "08:00 PM"
          ]
        },
        {
          "species": "CAT Lion",
          "feedingSchedule": [
            "09:00 AM",
            "01:00 PM",
            "05:00 PM"
          ]
        },
        {
          "species": "CAT Giraffe",
          "feedingSchedule": [
            "07:00 AM",
            "11:00 AM",
            "04:00 PM"
          ]
        }
      ]
    }
  },
  "inputDetails": {
    "truncated": false
  }
}'
```


<img width="1154" alt="Screenshot 2024-07-29 at 7 12 42 PM" src="https://github.com/user-attachments/assets/24662189-f1dc-4efe-9f85-7794bd7cefdf">

<img width="1162" alt="Screenshot 2024-07-29 at 7 13 58 PM" src="https://github.com/user-attachments/assets/bfa3d086-a573-4ca1-a909-7e6a0335011d">

Data populated by "test_populate_zoo_registry":
<img width="943" alt="Screenshot 2024-07-29 at 7 15 06 PM" src="https://github.com/user-attachments/assets/f13421f2-bc5b-4581-8f3f-8e36123cff56">

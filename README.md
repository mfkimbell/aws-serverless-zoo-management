# aws-serverless-zoo-management

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



<img width="1154" alt="Screenshot 2024-07-29 at 7 12 42 PM" src="https://github.com/user-attachments/assets/24662189-f1dc-4efe-9f85-7794bd7cefdf">

<img width="1162" alt="Screenshot 2024-07-29 at 7 13 58 PM" src="https://github.com/user-attachments/assets/bfa3d086-a573-4ca1-a909-7e6a0335011d">

Data populated by "test_populate_zoo_registry":
<img width="943" alt="Screenshot 2024-07-29 at 7 15 06 PM" src="https://github.com/user-attachments/assets/f13421f2-bc5b-4581-8f3f-8e36123cff56">

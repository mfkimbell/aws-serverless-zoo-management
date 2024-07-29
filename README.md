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

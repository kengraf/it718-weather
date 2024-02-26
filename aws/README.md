The deployment uses AWS SAM

Store your openweather api key as a secret in AWS SecretsManager.
The keyname must match "openweather-apikey" as the name is hardcoded in the Lambda function.

```
cd ./aws
sam build
sam deploy
```

This will create a CloudFormation stack with create: S3 bucket, REST API, and Lambda function resources.  
Built Artifacts  : .aws-sam/build  
Built Template   : .aws-sam/build/template.yaml  

*Open issue: Lambda permission to reads secrets.*
Although specified as documented by AWS, the SAM policy does not make it
into the generated role.  

*FIX* In the Lambda console. Open the attached role, then "Add Permissions", select&add "SecretsManagerReadWrite" policy.


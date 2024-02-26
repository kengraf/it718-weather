The deployment uses AWS SAM

```
cd ./aws
sam build
sam deploy
```

This will create a CloudFormation stack with a REST API and Lambda function resources.
Built Artifacts  : .aws-sam/build
Built Template   : .aws-sam/build/template.yaml

Commands you can use next
=========================
[*] Validate SAM template: sam validate
[*] Invoke Function: sam local invoke
[*] Test Function in the Cloud: sam sync --stack-name {{stack-name}} --watch
[*] Deploy: sam deploy --guided

# it718-weather
Complete overhaul of the Azure function implementation for weather app from IT718 textbook. Cloud Native Architectures, Copyright © 2018 Packt Publishing 

### Requirements:
- Register for a free account at [openweathermap.org](https://openweathermap.org/).  Securely store your API key.
- Register for a free account at [swagger.io](https://swagger.io/tools/).
- Access to a cloud CLI is assumed to run commands and the build application (AWS, Azure, and|or GCP).
- Function code is based on Python 3.9

### General steps
- Review the API yaml in this repo with: [Swagger Editor](https://editor.swagger.io/).  The intent is to reuse this yaml for AWS, Azure, and GCP.

Requests have the following format
```
curl https://api.openweathermap.org/data/2.5/weather?zip={zipcode}}&appid={API key}
```

You will receive a response like this: 
```
{"coord":{"lon":-70.8475,"lat":43.0353},"weather":\[{"id":701,"main":"Mist","description":"mist","icon":"50d"},{"id":501,"main":"Rain","description":"moderate rain","icon":"10d"}\],"base":"stations","main":{"temp":274.34,"feels_like":270.25,"temp_min":273.3,"temp_max":275.5,"pressure":1010,"humidity":91},"visibility":1006,"wind":{"speed":4.12,"deg":90,"gust":8.75},"rain":{"1h":1.42},"clouds":{"all":100},"dt":1677612774,"sys":{"type":1,"id":5415,"country":"US","sunrise":1677583302,"sunset":1677623435},"timezone":-18000,"id":0,"name":"Greenland","cod":200}
```
---
### Summary of AWS implementation
- Serverless application model (SAM) to build a CloudFormation stack
- API Gateway invokes a python based lambda function
- SecretsManager is used to hold the OpenWeather apikey
- URL template: https://{AWS-API-ID}.execute-api.{AWS-REGION}.amazonaws.com/Prod/weather?zip=00000
---
### Summary of Azure implementation
- Create a new Azure Function App and a HTTP trigger.  The function app name needs to be globally unique.  Runtime stack is Python 3.9.
- No secrets management, Key Vault not used.
- Support only for language version 1 not 2. i.e no decorater use



### Food for thought
- Github workflow.  This repo would need to add the required plumbing, because Function Apps can not be modfied in the console if Github integration is turned on.  
- Open Weather Map provides many API that are more engaging then the one used here.
- One set of common code for Azure, AWS, and GCP?
- Original source code used os.environ[rep_query_zip] to retrieve the zip paramenter, but the environment was not populated with the parameter values during testing.  Not sure if that was an environment/configuration issue or user error.

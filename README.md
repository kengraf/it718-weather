# it718-weather
Complete overhaul of the Azure function implementation for weather app from IT718 textbook. Cloud Native Architectures, Copyright © 2018 Packt Publishing 

### Requirements:
- Register for a free account at [openweathermap](https://openweathermap.org/).  Securely store your API key.
- Register for a free account at [swagger.io](https://swagger.io/tools/).
- Access to a cloud CLI to build application (AWS, Azure, and|or GCP)
- Function code is based on Python 3.12

### General steps
- Review the API yaml in this repo with: [Swagger Editor](https://editor.swagger.io/).  [Original yaml source](https://gist.github.com/KPS250/7d1cfc06caefe82ba008eccf911bb3af)

---
### The bare minimum process for AWS
1. Create a new Lambda function.  
---
### The bare minimum process for Azure
1. Create a new Azure Function App.  The function app name needs to be globally unique.  Runtime stack is Python 3.9.  Defaults for everything else is fine.  
2. Wait until the Function App shows "Your deployment is complete", then click "Go to Resource".  
3. Click "Functions" and create a new function.  Select "HTTP trigger", set the function trigger name, set Authorization level to anonymous.  
4. Click "Code & Test".  Replace the generated code for __init__.py with the code from this repo.  No changes are need for function.json.  
5. Click "SAve" then "Test/Run".  Set method to GET, add zip and apikey parameters, then click "Run".  The function should work.
6. Click "Get function URL".  In browser or with curl "https://~~YOUR_URL~~?zip=~~XXXXX~~&apikey=~~YOUR_API_KEY~~"

You will receive a response like this: 
{"coord":{"lon":-70.8475,"lat":43.0353},"weather":[{"id":701,"main":"Mist","description":"mist","icon":"50d"},{"id":501,"main":"Rain","description":"moderate rain","icon":"10d"}],"base":"stations","main":{"temp":274.34,"feels_like":270.25,"temp_min":273.3,"temp_max":275.5,"pressure":1010,"humidity":91},"visibility":1006,"wind":{"speed":4.12,"deg":90,"gust":8.75},"rain":{"1h":1.42},"clouds":{"all":100},"dt":1677612774,"sys":{"type":1,"id":5415,"country":"US","sunrise":1677583302,"sunset":1677623435},"timezone":-18000,"id":0,"name":"Greenland","cod":200}

### Food for thought
- Github workflow.  This repo would need to add the required plumbing, because Function Apps can not be modfied in the console if Github integration is turned on.  
- Open Weather Map provides many API that are more engaging then the one used here.
- One set of common code for Azure, AWS, and GCP?
- Original source code used os.environ[rep_query_zip] to retrieve the zip paramenter, but the environment was not populated with the parameter values during testing.  Not sure if that was an environment/configuration issue or user error.

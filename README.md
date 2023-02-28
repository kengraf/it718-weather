# it718-weather
Azure function implementation for weather app from IT718 textbook.

The bare minimum process
1. Create a new Azure Function App.  The function app name needs to be globally unique.  Runtime stack is Python 3.9.  Defaults for everything else is fine.  
2. Wait until the Function App shows "Your deployment is complete", then click "Go to Resource".  
3. Click "Functions" and create a new function.  Select "HTTP trigger", set the function trigger name, set Authorization level to anonymous.  
4. Click "Code & Test".  Replace the generated code for __init__.py with the code from this repo.  No changes are need for function.json.  

curl "https://~~YOUR_FUNCTION_NAME~~.azurewebsites.net/api/~~YOUR_TRIGGER_NAME~~?zip=~~XXXXX~~&apikey=~~YOUR_API_KEY~~"

You will receive a response like this: 
{"coord":{"lon":-70.8475,"lat":43.0353},"weather":[{"id":701,"main":"Mist","description":"mist","icon":"50d"},{"id":501,"main":"Rain","description":"moderate rain","icon":"10d"}],"base":"stations","main":{"temp":274.34,"feels_like":270.25,"temp_min":273.3,"temp_max":275.5,"pressure":1010,"humidity":91},"visibility":1006,"wind":{"speed":4.12,"deg":90,"gust":8.75},"rain":{"1h":1.42},"clouds":{"all":100},"dt":1677612774,"sys":{"type":1,"id":5415,"country":"US","sunrise":1677583302,"sunset":1677623435},"timezone":-18000,"id":0,"name":"Greenland","cod":200}

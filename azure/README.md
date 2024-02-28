- Defaults for everything else is fine.
- CLI using az command [process](https://learn.microsoft.com/en-us/azure/azure-functions/deployment-zip-push)
```
   az functionapp deployment source config-zip -g <resource_group> -n <app_name> --src <zip_file_path>
```
- Wait until the Function App shows "Your deployment is complete", then click "Go to Resource".  
- Click "Functions" and create a new function.  Select "HTTP trigger", set the function trigger name, set Authorization level to anonymous.  
- Click "Code & Test".  Replace the generated code for __init__.py with the code from this repo.  No changes are need for function.json.  
7. Click "Save" then "Test/Run".  Set method to GET, add zip and apikey parameters, then click "Run".  The function should work.
8. Click "Get function URL".  In browser or with curl "https://~~YOUR_URL~~?zip=~~XXXXX~~&apikey=~~YOUR_API_KEY~~"

- URL template: http://<APP_NAME>.azurewebsites.net/api/<FUNCTION_NAME>

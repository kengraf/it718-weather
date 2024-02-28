## Creation via the portal
- On Compute/FunctionApp page select create
   - Define name, resource group
   - Runtime stack=python, any supported version
   - Pick linux and serverless for compute environment
   - Use the defaults on the storage, networking, monitoring pages.
   - Wait until the Function App shows "Your deployment is complete", then click "Go to Resource".  
- Click "Functions" and create a new function.  Select "HTTP trigger", set the function trigger name, set Authorization level to anonymous.  
- Click "Code & Test".  Replace the generated code for __init__.py with the code from this repo.  No changes are need for function.json.  
7. Click "Save" then "Test/Run".  Set method to GET, add zip and apikey parameters, then click "Run".  The function should work.
8. Click "Get function URL".  In browser or with curl "https://~~YOUR_URL~~?zip=~~XXXXX~~&apikey=~~YOUR_API_KEY~~"

- URL template: http://<APP_NAME>.azurewebsites.net/api/<FUNCTION_NAME>


### Using the CLI
*Note* This is TBD.  Futher investigation is needed, currently reviewing the az and func command approaches with Cloud Shell.

import json
import urllib
from google.cloud import secretmanager_v1beta1 as secretmanager

def get_weather(request):
    # Extract query parameters from the request
    params = request.args

    # Check if parameters exist
    if params and 'zip' in params:
        zipcode = params['zip']
    
    if zipcode and len(zipcode) == 5:
        apikey = get_secret('openweather-apikey')
        ## construct full URL to invoke OpenWeatherMap service with proper inputs
        baseUrl = 'http://api.openweathermap.org/data/2.5/weather'
        completeUrl = f"{baseUrl}?zip={zipcode}&appid={apikey}"

        ## Invoke OpenWeatherMap API and parse response with proper exception handling
        try:
            apiresponse = urllib.request.urlopen(completeUrl)
            return apiresponse.read().decode('utf-8'), 200
        except urllib.error.HTTPError as e:
            return e, e.code
        except urllib.error.URLError as e:
            return e, e.code
    else:
        return 'URL args required ?zip=XXXXX',400

def get_secret(secret_name):
    project_id = 'unh-it718'
    
    # Create the Secret Manager client
    client = secretmanager.SecretManagerServiceClient()
    
    # Build the secret name
    name = f"projects/{project_id}/secrets/{secret_name}/versions/latest"
    # Access the secret
    response = client.access_secret_version(name=name)
    api_key = response.payload.data.decode('UTF-8')

    return( api_key )

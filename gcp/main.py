import boto3
import json
import urllib

def get_weather(request):
    # Extract query parameters from the request
    params = request.args

    # Check if parameters exist
    if params and 'zip' in params:
        zipcode = params['message']
    
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
    return( 'bf9ca2bcc1017086a8a69247d7a21dc0' )

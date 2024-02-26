import boto3
import json
import urllib
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    status_code = 200
    response_message = ''
    query_params = event.get('queryStringParameters', {})
    if len(query_params) > 0:
        zipcode = query_params.get('zip')
    
    if len(zipcode) == 5:
        apikey = get_secret('openweather-apikey')
        ## construct full URL to invoke OpenWeatherMap service with proper inputs
        baseUrl = 'http://api.openweathermap.org/data/2.5/weather'
        completeUrl = f"{baseUrl}?zip={zipcode}&appid={apikey}"
        print(completeUrl)
        ## Invoke OpenWeatherMap API and parse response with proper exception handling
        try:
            apiresponse = urllib.request.urlopen(completeUrl)
            response_message = apiresponse.read().decode('utf-8') 
        except urllib.error.HTTPError as e:
            status_code=e.code
            response_message = e
        except urllib.error.URLError as e:
            status_code=e.code
            response_message = e
    else:
        status_code = 400
        response_message = 'URL args required ?zip=XXXXX'

    return {
        'statusCode': status_code,
        'headers': { 'Content-Type': 'text/plain' },
        'body': response_message
    }

def get_secret(secret_name):
    # Create a Secrets Manager client
    client = boto3.client('secretsmanager')

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name,)
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    secret = get_secret_value_response['SecretString']
    key = json.loads(secret)['openweather-apikey']
    return( key )

import boto3
import urllib
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    status_code = 200
    response_message = ''
    query_params = event.get('queryStringParameters', {})
    zip = query_params.get('zip', '03824')  

    
    if zipcode:
        apikey = get_secret('opeweatherapi-apikey')
        ## construct full URL to invoke OpenWeatherMap service with proper inputs
        baseUrl = 'http://api.openweathermap.org/data/2.5/weather'
        completeUrl = f"{baseUrl}?zip={zipcode}&appid={apikey}"
        ## Invoke OpenWeatherMap API and parse response with proper exception handling
        try:
            apiresponse = urllib.request.urlopen(completeUrl)
            response_message = apiresponse.read().decode('utf-8') 
        except urllib.error.HTTPError as e:
            status_code=e.code
            response_message = "The server couldn't fulfill the request. Error code:" + e.code
        except urllib.error.URLError as e:
            status_code=e.code
            response_message =   "We failed to reach a server. Reason:" + e.reason
    else:
        status_code = 400
        response_message = 'URL args required ?zip=XXXXX'

    return {
        'statusCode': status_code,
        'headers': { 'Content-Type': 'text/plain' },
        'body': response_message
    }

def get_secret(secret_name):
    secret_name = "opeweatherapi-apikey"

    # Create a Secrets Manager client
    client = boto3.client('secretsmanager')

    try:
        get_secret_value_response = client.get_secret_value(secret_name)
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    secret = get_secret_value_response['SecretString']

    # Your code goes here.
    return( secret )


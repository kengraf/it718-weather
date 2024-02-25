# openweather.py

def lambda_handler(event, context):
    """
    Lambda handler function that returns a simple "Hello, world!" response.
    """
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'Hello, world!'
    }

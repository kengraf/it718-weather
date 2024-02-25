import urllib
import logging

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    zipcode = req.params.get('zip')
    apikey = req.params.get('apikey')

    if zipcode and apikey:
        ## construct full URL to invoke OpenWeatherMap service with proper inputs
        baseUrl = 'http://api.openweathermap.org/data/2.5/weather'
        completeUrl = f"{baseUrl}?zip={zipcode}&appid={apikey}"
        logging.info('Request URL--> ' + completeUrl)
    else:
        logging.info("URL required args missing." )
        return func.HttpResponse("URL args required ?zip=XXXXX&apikey=YOUR_API_KEY." )

    ## Invoke OpenWeatherMap API and parse response with proper exception handling
    try:
        apiresponse = urllib.request.urlopen(completeUrl)
        response = apiresponse.read().decode('utf-8') 
        return func.HttpResponse(response)
    except urllib.error.HTTPError as e:
        return func.HttpResponse(
            "The server couldn't fulfill the request. Error code:" + e.code,
            status_code=e.code )
    except urllib.error.URLError as e:
        return func.HttpResponse(
                    "We failed to reach a server. Reason:" + e.reason,
            status_code=e.code )

    

import logging
import requests
import json
import os

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    file = req.files["file"]

    print(file.filename)

    headers = {
        'Prediction-Key': os.environ['PREDICTION_KEY'],
        'Content-Type': 'application/octet-stream'
    }

    data = requests.post(os.environ['PREDICTION_URL'],
    headers=headers,
    data=file.stream.read())

    print(json.dumps(data.json()))

    return func.HttpResponse(json.dumps(data.json()))
    # name = req.params.get('name')
    # if not name:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         name = req_body.get('name')

    # if name:
    #     return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    # else:
    #     return func.HttpResponse(
    #          "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
    #          status_code=200
    #     )

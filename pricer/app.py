import json
from stocks import stocks
import numpy
from prices import get_prices
from pprint import pprint


def lambda_handler(event, context):
    urlqs = event['queryStringParameters']
    if urlqs:
        n = int(urlqs.get('n'))
        prices = get_prices(stocks, n)
        print('are we even here?', prices)
        return {
            "statusCode": 200,
            "body": json.dumps(prices),
            "headers": {
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',
                'Content-Type': 'application/json',
            },
        }
    return dict(statusCode=404,
                body=dict(message='error'))

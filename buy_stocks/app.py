import requests
import boto3
import os
import uuid
import random
from datetime import datetime
# from opentelemetry import trace


def lambda_handler(event, context):
    if 'AWS_SAM_LOCAL' in os.environ:
        s3 = boto3.client('s3', endpoint_url="http://host.docker.internal:4566")
    else:
        s3 = boto3.client('s3')
    alpaca_id = os.environ['ALPACA_ID']
    alpaca_secret = os.environ['ALPACA_SECRET']
    headers = {'APCA-API-KEY-ID': alpaca_id, 'APCA-API-SECRET-KEY': alpaca_secret}

    rankings_file = s3.get_object(Bucket=os.environ['BUCKET_NAME'], Key='rankings.txt')
    stock_ranking = rankings_file['Body'].read().decode('utf-8').split(' ')

    # customizedSpan = trace.get_current_span()
    # customizedSpan.set_attribute("alpaca.id", alpaca_id);
    # customizedSpan.set_attribute("alpaca.secret", alpaca_secret);
    # customizedSpan.set_attribute("rankings", str(stock_ranking));

    # We buy a share and then immediately sell the share so the fake trading account doesn't go broke
    for i in range(3):
        buy_response = requests.post('https://paper-api.alpaca.markets/v2/orders', headers=headers,
                                     json={'symbol': stock_ranking[i], 'qty': 1, 'side': 'buy', 'type': 'market',
                                           'time_in_force': 'day'})
        sell_reponse = requests.post('https://paper-api.alpaca.markets/v2/orders', headers=headers,
                      json={'symbol': stock_ranking[i], 'qty': 1, 'side': 'sell', 'type': 'market',
                            'time_in_force': 'day'})


    transaction_result = {
        "id": str(uuid.uuid4()),  # Unique ID for the transaction
        "price": str(random.randint(1, 100)),  # Random Price of each share
        "type": "buy",  # Type of transaction (buy/sell)
        "qty": str(
            random.randint(1, 10)
        ),  # Number of shares bought/sold (We are mocking this as a random integer between 1 and 10)
        "timestamp": datetime.now().isoformat(),  # Timestamp when the transaction was completed
    }

    return transaction_result

import json

import requests

proxies = {
    'http': 'socks5://127.0.0.1:1055',
    'https': 'socks5://127.0.0.1:1055'
}

def lambda_handler(event, context):

    try:
        ip = requests.get("http://100.101.247.121", proxies=proxies)
    except requests.RequestException as e:
        # Send some context about this error to Lambda Logs
        print(e)

        raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
             "location": ip.text.replace("\n", "")
        }),
    }

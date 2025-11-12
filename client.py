import sys
import requests
import json
import os
from os.path import join
import time

n = 1000

def buildRequest(jpegPath):
    """
    Performs an HTTP POST request to a given URL with a JSON payload.

    Args:
        url (str): The URL to send the POST request to.
        data (dict): The dictionary containing the data to be sent.

    Returns:
        tuple: A tuple containing the HTTP status code and the response body.
    """

    inferenceHeader = {
        "inputs": [
            {
                "name": "0",
                "shape": [1],
                "datatype": "BYTES",
            }
        ]
    }

    inferenceHeader = json.dumps(inferenceHeader).encode(encoding='utf-8', errors='strict')
    inferenceHeaderSize = len(inferenceHeader)
    
    inputSize = os.path.getsize(jpegPath)
    inputSizeBytes = inputSize.to_bytes(4,"little")
    body = inferenceHeader + inputSizeBytes + open(jpegPath, 'rb').read()
    bodySize = len(body)

    header = {
        'Content-Type': 'application/octet-stream',
        'Content-Length': f'{bodySize}',
        'Inference-Header-Content-Length': f'{inferenceHeaderSize}',
    }
   
    return header, body

def makeRequest(headers, body, url):
    url = f'http://{url}/v2/models/ovms-resnet50/infer'
    response = requests.post(url=url, headers=headers, data=body)

url = sys.argv[1]

requests = [(label, buildRequest(join('images',label)) for label in os.listdir('images')]

latencies = []
for i in range(n):
    label, request = bodies[i%len(bodies)]
    try:
        start = time.perf_counter()
        makeRequest(requests[0], requests[1], url)
        stop = time.perf_counter()
        latencies.append(stop - start)
    except:
        print(f'error on {label}')

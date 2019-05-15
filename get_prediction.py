#!/usr/bin/python

import boto3
import json
import numpy as np

from sagemaker.content_types import CONTENT_TYPE_JSON
from sagemaker.predictor import json_serializer, json_deserializer

client = boto3.client('sagemaker-runtime')

endpoint_name = "rl-auto-scaling-2019-04-29-07-09-01-876"
content_type = "application/json"
accept = "Accept"

payload = np.arange(1, 26)
payload = [ 10,20,30,40,50,60,70,80,90,100,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
payload = json_serializer(payload)

response = client.invoke_endpoint(
    EndpointName=endpoint_name, 
    ContentType=content_type,
    Accept=accept,
    Body=payload
    )

# then deserialize
print(json_deserializer(response['Body'], response['ContentType']))  
print(payload)

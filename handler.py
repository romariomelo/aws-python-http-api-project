import json
import boto3
import os
from extract_info import extract_info
from cout_words import count_words_returns_dic
from get_pdf import pdf_by_io, pdf_content_to_string

def hello(event, context):

    body_request = json.loads(event['body'])

    s3 = get_s3_client()
    bucket_name = 'test-bucket'
    file_name = body_request['key']

    s3_response_object = s3.get_object(Bucket=bucket_name, Key=file_name)
    object_content = s3_response_object['Body'].read()

    pdf_file = pdf_by_io(object_content)
    palavras = count_words_returns_dic(pdf_file)
    pdf = pdf_content_to_string(pdf_file)

    info = extract_info(pdf, palavras)

    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!!!",
        "input": event,
    }

    buckets = {"statusCode": 200, "body": json.dumps({**info, **body})}

    return buckets

def get_python_env():
    return os.getenv('PYTHON_ENV') or 'development'

def get_s3_client():
    if get_python_env() == 'development':
        return boto3.client('s3',
            endpoint_url='http://localhost:4566',
            region_name="us-east-1")
    else:
        return boto3.client('s3',
            region_name="us-east-1")
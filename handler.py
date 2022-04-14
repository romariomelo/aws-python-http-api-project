import json
import boto3
from extract_info import extract_info
from cout_words import count_words_returns_dic
from get_pdf import pdf_by_io, pdf_content_to_string

def hello(event, context):
    s3 = boto3.client('s3',
        endpoint_url='http://localhost:4566',
        region_name="us-east-1")
    bucket_name = 'test-bucket'
    file_name = 'votos/' + event['pathParameters']['filename']

    s3_response_object = s3.get_object(Bucket=bucket_name, Key=file_name)
    object_content = s3_response_object['Body'].read()

    pdf_file = pdf_by_io(object_content)
    palavras = count_words_returns_dic(pdf_file)
    pdf = pdf_content_to_string(pdf_file)

    info = extract_info(pdf, palavras)

    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!!!",
        "arquivo": event['pathParameters']['filename'],
        "input": event,
    }

    buckets = {"statusCode": 200, "body": json.dumps({**info, **body})}

    return buckets


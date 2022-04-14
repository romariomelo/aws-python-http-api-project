import json
import boto3
import os
from io import BytesIO
import PyPDF2
import spacy
from tika import parser


def hello(event, context):
    s3 = boto3.client('s3',
        endpoint_url='http://localhost:4566',
        region_name="us-east-1")
    bucket_name = 'test-bucket'
    file_name = 'votos/' + event['pathParameters']['filename']

    s3_response_object = s3.get_object(Bucket=bucket_name, Key=file_name)
    object_content = s3_response_object['Body'].read()

    pdf_file = parser.from_buffer(BytesIO(object_content))['content']

    info = extract_info(pdf_file)


    nlp = spacy.load("pt_core_news_sm")
    nlp.Defaults.stop_words |= {'ccee', 'n', 'linkx', 'ltda', '\n\n', '\n', '  '}

    pdf = str(nlp(pdf_file))

    print(pdf)

    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!!!",
        "arquivo": event['pathParameters']['filename'],
        "input": event,
    }

    buckets = {"statusCode": 200, "body": json.dumps({**info, **body})}

    return buckets

def extract_info(pdf_file):
    """Processo"""
    novodata = pdf_file.split("\n")
    primeiraLetraProcesso = pdf_file.find("P")
    processo = pdf_file[primeiraLetraProcesso+10:primeiraLetraProcesso+30]

    """Interessado"""
    interessadoInicio = pdf_file.find("INTERESSAD")
    interessadoFinal = pdf_file.find("RELATOR")
    interesado = pdf_file[interessadoInicio:interessadoFinal]


    """Relator"""
    relatorInicio = pdf_file.find("RELATOR")
    relatorFinal = pdf_file.find("RESPONSÁVEL:")
    relator = pdf_file[relatorInicio:relatorFinal]
  

    """RESPONSÁVEL"""
    responsavelInicio = pdf_file.find("RESPONSÁVEL:")
    responsavelFinal = pdf_file.find("ASSUNTO:")
    responsavel = pdf_file[responsavelInicio:responsavelFinal]

    """Assunto"""
    assuntoInicio = pdf_file.find("ASSUNTO:")
    assuntoFinal = pdf_file.find("I – RELATÓRIO")
    assunto= pdf_file[assuntoInicio:assuntoFinal]
    
   
    """Dispositivo"""
    dispositivoInicio = pdf_file.find("– DISPOSITIVO")
    dispositivoFinal = pdf_file.find("Brasília,")
    dispositivo = pdf_file[dispositivoInicio+14:dispositivoFinal]

    """Data"""
    data = pdf_file[dispositivoFinal:-1]
    data_final = data.find(".")
    dt = data[10:data_final]

    response = {
        "processo": processo,
        "interessado": interesado,
        "relator": relator,
        "responsavel": responsavel,
        "assunto": assunto,
        "dispositivo": dispositivo,
        "data": dt,
    }

    return response

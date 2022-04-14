# AWS PYTHON HTTP API PROJECT

## AWS CLI

- Instalar AWS CLI:

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

- Configure AWS CLI

```bash
aws configure
```

Será solicitado algumas informações de credenciais da AWS. Pode ser preenchido com alguns valores fakes para testes local.

```bash
AWS Access Key ID [Nome]: AAAA
AWS Secret Access Key [None]: ZZZZ
Default region name [None]: us-east-1
Default output format [None]:
```

## Docker localstack

- Levantar container docker do localstack:

```bash
docker-compose up -d
```

## Bucket fake

- Executar script para criar bucket e fazer upload de arquivo via AWS CLI:

```bash
cd scripts
sh op-bucket.sh
```

- Instalar `serverless` global:

```bash
npm i -g serverless
```

- Instalar plugin `serverless offline`:

```bash
serverless plugin install -n serverless-offline
```

## Python

- TODO : Instalar Python

## Iniciar serviço

- Iniciar serverless

```bash
serverless offline
```

- Testar endpoint

Acessar o link no navegador:

[http://localhost:4000/48500.006904-2019-52.pdf](http://localhost:4000/48500.006904-2019-52.pdf)

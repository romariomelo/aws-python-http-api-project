#!/bin/bash
BUCKET_NAME=test-bucket
alias awslocal="aws --endpoint-url=http://localhost:4566"
awslocal s3api create-bucket --bucket $BUCKET_NAME
awslocal s3 cp 48500.006904-2019-52.pdf s3://$BUCKET_NAME
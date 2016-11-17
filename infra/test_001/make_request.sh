#!/usr/bin/env bash 

set -eo pipefail

curl "https://jhgh1kwrpk.execute-api.us-west-2.amazonaws.com/test_001/lambda_a" -X POST -d '{"commands": ["invoke_lambda(\"master_lambda_b\", {\"cold_seconds\":1,\"hot_seconds\":0.1})"]}'

variable "aws_profile" {}
variable "aws_account" {}
variable "aws_region" {}
variable "aws_resource_prefix" {}
variable "s3_bucket" {}
variable "lambda_wheel_filename" {}
variable "lambda_wheel_s3_version" {}

resource "aws_api_gateway_rest_api" "api" {
  name = "${var.aws_resource_prefix}_aws_lambda_test"
}

module "endpoint_lambda_a" {
  source = "./modules/api_method"
  aws_account = "${var.aws_account}"
  aws_region = "${var.aws_region}"
  aws_resource_prefix = "${var.aws_resource_prefix}"
  rest_api_id = "${aws_api_gateway_rest_api.api.id}"
  parent_id = "${aws_api_gateway_rest_api.api.root_resource_id}"
  path_part = "lambda_a"
  http_method = "POST"
  function = "lambda_a"
}

module "lambda_a" {
  source = "./modules/lambda_a"
  function_name = "lambda_a"
  aws_account = "${var.aws_account}"
  aws_region = "${var.aws_region}"
  aws_resource_prefix = "${var.aws_resource_prefix}"
  s3_bucket = "${var.s3_bucket}"
  lambda_wheel_filename = "${var.lambda_wheel_filename}"
  lambda_wheel_s3_version = "${var.lambda_wheel_s3_version}"
  invocation_source_arn = "${module.endpoint_lambda_a.method_arn}"
}

module "lambda_b" {
  source = "./modules/lambda_b"
  function_name = "lambda_b"
  aws_account = "${var.aws_account}"
  aws_region = "${var.aws_region}"
  aws_resource_prefix = "${var.aws_resource_prefix}"
  s3_bucket = "${var.s3_bucket}"
  lambda_wheel_filename = "${var.lambda_wheel_filename}"
  lambda_wheel_s3_version = "${var.lambda_wheel_s3_version}"
  invocation_source_arn = "${module.lambda_a.function_arn}"
}

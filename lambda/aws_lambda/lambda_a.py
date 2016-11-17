import logging
import time
import os
import uuid
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)
instance_id_file_path = "/tmp/instance_id"
instance_info = ""
new_instance = ""

def get_instance_info():
    ii = ""
    if os.path.isfile(instance_id_file_path):
        with open(instance_id_file_path) as f:
            instance_id = str(f.read())
        ii = "old " + instance_id
    else:
        instance_id = str(uuid.uuid4())
        ii = "new " + instance_id
        with open(instance_id_file_path, "w") as f:
            f.write(instance_id)

    return ii


def info(message):
    logger.info(instance_info + " " + message)


def execute_command(command):
    info("executing command " + command)
    exec(command)
    info("executed  command " + command)


def invoke_lambda(function_name, payload):
    info("invoking function " + function_name + " with payload " + str(payload))
    payload_bytes = [elem.encode("hex") for elem in str(payload)]
    client = boto3.client('lambda')
    response = client.invoke(
            FunctionName=function_name,
            InvocationType="RequestResponse",
            Payload=payload_bytes)
    info("invoked  function " + function_name + ", response " + str(response))


def start(cold_seconds, hot_seconds):
    if new_instance:
        info("simulating cold strart delay " + str(cold_seconds) + " seconds")
        time.sleep(cold_seconds)
    else:
        info("simulating hot  strart delay " + str(hot_seconds) + " seconds")
        time.sleep(hot_seconds)


def handle_request(event, context):
    info("received request {}".format(event))

    instance_info = get_instance_info()
    new_instance = instance_info.startswith("new ")


    for command in event.get("commands"):
        execute_command(command)

    response = {}

    response["instance_info"] = instance_info

    info("returning response " + str(response))
    return response

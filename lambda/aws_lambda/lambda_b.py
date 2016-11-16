import logging
import time
import os
import uuid
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)
instance_id_file_path = "/tmp/instance_id"

def get_instance_info():
    instance_info = ""
    if os.path.isfile(instance_id_file_path):
        with open(instance_id_file_path) as f:
            instance_id = f.read()
        instance_info = "old " + instance_id
    else:
        instance_id = str(uuid.uuid4())
        instance_info = "new " + instance_id
        with open(instance_id_file_path, "w") as f:
            f.write(instance_id)

    return instance_info


def info(message):
    logger.info(instance_info + " " + message)


def start(cold_seconds, hot_seconds):
    if new_instance:
        info("simulating cold strart delay " + str(cold_seconds) + " seconds")
        time.sleep(cold_seconds)
    else:
        info("simulating hot  strart delay " + str(hot_seconds) + " seconds")
        time.sleep(hot_seconds)


instance_info = get_instance_info()
new_instance = instance_info.startswith("new ")

def handle_request(event, context):
    info("received request {}".format(event))

    start(event.get("cold_seconds"), event.get("hot_seconds"))

    response = {}
    response["instance_info"] = instance_info

    info("returning response " + str(response))

    return response

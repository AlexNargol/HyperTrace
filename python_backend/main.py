import grpc
import sys
import grpc
from loki_logger_handler.loki_logger_handler import LokiLoggerHandler
import logging
import os
import json
import requests
import time
from google.protobuf.json_format import MessageToJson
from pythonjsonlogger import jsonlogger
# add the generated directory to the Python path
sys.path.append('./generated')
import telemetry_pb2
import telemetry_pb2_grpc



def init_logger():
    # set up logging
    logger = logging.getLogger("custom_logger")
    logger.setLevel(logging.DEBUG)

    # create an instance of the custom handler
    custom_handler = LokiLoggerHandler(
        url="http://127.0.0.1:3100/loki/api/v1/push",
        labels={"application": "Test", "environment": "Develop"},
        label_keys={},
        timeout=10,
    )

    # create an instance of the custom handler
    logger.addHandler(custom_handler)

    return logger


def get_data(logger):
    # get gRPC server port
    channel = grpc.insecure_channel('localhost:8000')
    # get stub defined in proto file
    stub = telemetry_pb2_grpc.TelemetryServiceStub(channel)

    # get distro info
    distro_request = telemetry_pb2.DistroRequest()

    # send distro info request
    dist_response = stub.SendDistroInfo(distro_request)
    # convert response to json
    json_dist_response= MessageToJson(dist_response)
    # parse json response
    parsed_dist_response = json.loads(json_dist_response)

    # create memory request object from generated proto file
    memory_request = telemetry_pb2.MemoryRequest()

    # loop through and get memory info every 5 seconds
    while True:
        try:
            # get memory info from gRPC server
            response = stub.SendMemoryInfo(memory_request)

            # process response to json
            json_response = MessageToJson(response)
            parsed = json.loads(json_response)

            # get current time to add to log
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)

            # add time json entry for visualisation downstream
            parsed['time'] = current_time

            print(parsed)
            # send log to Loki
            logger.info("Memory Stats", extra=parsed)

            # sleep for 5 seconds
            time.sleep(5)

        except grpc.RpcError as e:
            print(f"gRPC error: {e.code()}: {e.details()}")
            break

if __name__ == "__main__":
    logger = init_logger()
    get_data(logger)


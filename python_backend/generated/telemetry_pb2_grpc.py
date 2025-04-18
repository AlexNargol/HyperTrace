# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import telemetry_pb2 as telemetry__pb2

GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in telemetry_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class TelemetryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendMemoryInfo = channel.unary_unary(
                '/telemetry.TelemetryService/SendMemoryInfo',
                request_serializer=telemetry__pb2.MemoryRequest.SerializeToString,
                response_deserializer=telemetry__pb2.MemoryInfo.FromString,
                _registered_method=True)
        self.SendDistroInfo = channel.unary_unary(
                '/telemetry.TelemetryService/SendDistroInfo',
                request_serializer=telemetry__pb2.DistroRequest.SerializeToString,
                response_deserializer=telemetry__pb2.DistroInfo.FromString,
                _registered_method=True)


class TelemetryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendMemoryInfo(self, request, context):
        """Use Empty for request
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendDistroInfo(self, request, context):
        """Use Empty for request
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TelemetryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendMemoryInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMemoryInfo,
                    request_deserializer=telemetry__pb2.MemoryRequest.FromString,
                    response_serializer=telemetry__pb2.MemoryInfo.SerializeToString,
            ),
            'SendDistroInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.SendDistroInfo,
                    request_deserializer=telemetry__pb2.DistroRequest.FromString,
                    response_serializer=telemetry__pb2.DistroInfo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'telemetry.TelemetryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('telemetry.TelemetryService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TelemetryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendMemoryInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/telemetry.TelemetryService/SendMemoryInfo',
            telemetry__pb2.MemoryRequest.SerializeToString,
            telemetry__pb2.MemoryInfo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SendDistroInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/telemetry.TelemetryService/SendDistroInfo',
            telemetry__pb2.DistroRequest.SerializeToString,
            telemetry__pb2.DistroInfo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

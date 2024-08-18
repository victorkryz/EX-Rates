# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import ex_rates_pb2 as ex__rates__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in ex_rates_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class ExRatesSvcStub(object):
    """The currency rates service defenition:
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetRates = channel.unary_unary(
                '/currates.ExRatesSvc/GetRates',
                request_serializer=ex__rates__pb2.Request.SerializeToString,
                response_deserializer=ex__rates__pb2.Rates.FromString,
                _registered_method=True)


class ExRatesSvcServicer(object):
    """The currency rates service defenition:
    """

    def GetRates(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ExRatesSvcServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetRates': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRates,
                    request_deserializer=ex__rates__pb2.Request.FromString,
                    response_serializer=ex__rates__pb2.Rates.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'currates.ExRatesSvc', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('currates.ExRatesSvc', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ExRatesSvc(object):
    """The currency rates service defenition:
    """

    @staticmethod
    def GetRates(request,
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
            '/currates.ExRatesSvc/GetRates',
            ex__rates__pb2.Request.SerializeToString,
            ex__rates__pb2.Rates.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

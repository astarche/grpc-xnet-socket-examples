from contextlib import contextmanager
from typing import Protocol, TypeVar

import grpc
import xnetgrpc.nixnetsocket_pb2_grpc as xnetsocket_grpc
import xnetgrpc.session_pb2 as session_pb
import xnetgrpc.session_pb2_grpc as session_grpc


class _XnetSocketResponse(Protocol):
    status: int
    error_num: int
    error_message: str


TResponse = TypeVar("TResponse", bound=_XnetSocketResponse)


def raise_if_error(response: TResponse) -> TResponse:
    """Raise an exception if response.status indicates an error."""
    if response.status < 0:
        raise Exception(f"Error: {response.status}, {response.error_num}: {response.error_message}")
    return response


@contextmanager
def grpc_device_session(server):
    """Create a grpc-device client and ResetServer on context exit."""
    session_utils_client = None
    try:
        channel = grpc.insecure_channel(f"{server}")
        client = xnetsocket_grpc.NiXnetSocketStub(channel)
        session_utils_client = session_grpc.SessionUtilitiesStub(channel)
        yield client
    finally:
        if session_utils_client:
            session_utils_client.ResetServer(session_pb.ResetServerRequest())

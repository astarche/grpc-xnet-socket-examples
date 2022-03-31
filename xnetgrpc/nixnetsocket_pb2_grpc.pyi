"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
from . import nixnetsocket_pb2

class NiXnetSocketStub:

    def __init__(self, channel: grpc.Channel) -> None:
        ...
    Accept: grpc.UnaryUnaryMultiCallable[nixnetsocket_pb2.AcceptRequest, nixnetsocket_pb2.AcceptResponse]
    Bind: grpc.UnaryUnaryMultiCallable[nixnetsocket_pb2.BindRequest, nixnetsocket_pb2.BindResponse]
    Close: grpc.UnaryUnaryMultiCallable[nixnetsocket_pb2.CloseRequest, nixnetsocket_pb2.CloseResponse]
    Connect: grpc.UnaryUnaryMultiCallable[nixnetsocket_pb2.ConnectRequest, nixnetsocket_pb2.ConnectResponse]
    FdIsSet: grpc.UnaryUnaryMultiCallable[nixnetsocket_pb2.FdIsSetRequest, nixnetsocket_pb2.FdIsSetResponse]
    GetAddrInfo: grpc.UnaryUnaryMultiCallable[nixnetsocket_pb2.GetAddrInfoRequest, nixnetsocket_pb2.GetAddrInfoResponse]
    GetNameInfo: grpc.UnaryUnaryMultiCallable[nixnetsocket_pb2.GetNameInfoRequest, nixnetsocket_pb2.GetNameInfoResponse]
    GetPeerName: grpc.UnaryUnaryMultiCallable[nixnetsocket_pb2.GetPeerNameRequest, nixnetsocket_pb2.GetPeerNameResponse]
    GetSockName: grpc.UnaryUnaryMultiCallable[nixnetsocket_pb2.GetSockNameRequest, nixnetsocket_pb2.GetSockNameResponse]
    GetSockOpt: grpc.UnaryUnaryMultiCallable[nixnetsocket_pb2.GetSockOptRequest, nixnetsocket_pb2.GetSockOptResponse]
    InetAddr: grpc.UnaryUnaryMultiCallable[nixnetsocket_pb2.InetAddrRequest, nixnetsocket_pb2.InetAddrResponse]
    InetAToN: grpc.UnaryUnaryMultiCallable[nixnetsocket_pb2.InetAToNRequest, nixnetsocket_pb2.InetAToNResponse]
    InetNToA: grpc.UnaryUnaryMultiCallable[nixnetsocket_pb2.InetNToARequest, nixnetsocket_pb2.InetNToAResponse]
    InetNToP: grpc.UnaryUnaryMultiCallable[nixnetsocket_pb2.InetNToPRequest, nixnetsocket_pb2.InetNToPResponse]
    InetPToN: grpc.UnaryUnaryMultiCallable[nixnetsocket_pb2.InetPToNRequest, nixnetsocket_pb2.InetPToNResponse]
    IpStackClear: grpc.UnaryUnaryMultiCallable[nixnetsocket_pb2.IpStackClearRequest, nixnetsocket_pb2.IpStackClearResponse]
    IpStackCreate: grpc.UnaryUnaryMultiCallable[nixnetsocket_pb2.IpStackCreateRequest, nixnetsocket_pb2.IpStackCreateResponse]
    IpStackGetAllStacksInfoStr: grpc.UnaryUnaryMultiCallable[nixnetsocket_pb2.IpStackGetAllStacksInfoStrRequest, nixnetsocket_pb2.IpStackGetAllStacksInfoStrResponse]
    IpStackGetInfo: grpc.UnaryUnaryMultiCallable[nixnetsocket_pb2.IpStackGetInfoRequest, nixnetsocket_pb2.IpStackGetInfoResponse]
    IpStackOpen: grpc.UnaryUnaryMultiCallable[nixnetsocket_pb2.IpStackOpenRequest, nixnetsocket_pb2.IpStackOpenResponse]
    IpStackWaitForInterface: grpc.UnaryUnaryMultiCallable[nixnetsocket_pb2.IpStackWaitForInterfaceRequest, nixnetsocket_pb2.IpStackWaitForInterfaceResponse]
    Listen: grpc.UnaryUnaryMultiCallable[nixnetsocket_pb2.ListenRequest, nixnetsocket_pb2.ListenResponse]
    Recv: grpc.UnaryUnaryMultiCallable[nixnetsocket_pb2.RecvRequest, nixnetsocket_pb2.RecvResponse]
    RecvFrom: grpc.UnaryUnaryMultiCallable[nixnetsocket_pb2.RecvFromRequest, nixnetsocket_pb2.RecvFromResponse]
    Select: grpc.UnaryUnaryMultiCallable[nixnetsocket_pb2.SelectRequest, nixnetsocket_pb2.SelectResponse]
    Send: grpc.UnaryUnaryMultiCallable[nixnetsocket_pb2.SendRequest, nixnetsocket_pb2.SendResponse]
    SendTo: grpc.UnaryUnaryMultiCallable[nixnetsocket_pb2.SendToRequest, nixnetsocket_pb2.SendToResponse]
    SetSockOpt: grpc.UnaryUnaryMultiCallable[nixnetsocket_pb2.SetSockOptRequest, nixnetsocket_pb2.SetSockOptResponse]
    Shutdown: grpc.UnaryUnaryMultiCallable[nixnetsocket_pb2.ShutdownRequest, nixnetsocket_pb2.ShutdownResponse]
    Socket: grpc.UnaryUnaryMultiCallable[nixnetsocket_pb2.SocketRequest, nixnetsocket_pb2.SocketResponse]
    StrErrR: grpc.UnaryUnaryMultiCallable[nixnetsocket_pb2.StrErrRRequest, nixnetsocket_pb2.StrErrRResponse]

class NiXnetSocketServicer(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def Accept(self, request: nixnetsocket_pb2.AcceptRequest, context: grpc.ServicerContext) -> nixnetsocket_pb2.AcceptResponse:
        ...

    @abc.abstractmethod
    def Bind(self, request: nixnetsocket_pb2.BindRequest, context: grpc.ServicerContext) -> nixnetsocket_pb2.BindResponse:
        ...

    @abc.abstractmethod
    def Close(self, request: nixnetsocket_pb2.CloseRequest, context: grpc.ServicerContext) -> nixnetsocket_pb2.CloseResponse:
        ...

    @abc.abstractmethod
    def Connect(self, request: nixnetsocket_pb2.ConnectRequest, context: grpc.ServicerContext) -> nixnetsocket_pb2.ConnectResponse:
        ...

    @abc.abstractmethod
    def FdIsSet(self, request: nixnetsocket_pb2.FdIsSetRequest, context: grpc.ServicerContext) -> nixnetsocket_pb2.FdIsSetResponse:
        ...

    @abc.abstractmethod
    def GetAddrInfo(self, request: nixnetsocket_pb2.GetAddrInfoRequest, context: grpc.ServicerContext) -> nixnetsocket_pb2.GetAddrInfoResponse:
        ...

    @abc.abstractmethod
    def GetNameInfo(self, request: nixnetsocket_pb2.GetNameInfoRequest, context: grpc.ServicerContext) -> nixnetsocket_pb2.GetNameInfoResponse:
        ...

    @abc.abstractmethod
    def GetPeerName(self, request: nixnetsocket_pb2.GetPeerNameRequest, context: grpc.ServicerContext) -> nixnetsocket_pb2.GetPeerNameResponse:
        ...

    @abc.abstractmethod
    def GetSockName(self, request: nixnetsocket_pb2.GetSockNameRequest, context: grpc.ServicerContext) -> nixnetsocket_pb2.GetSockNameResponse:
        ...

    @abc.abstractmethod
    def GetSockOpt(self, request: nixnetsocket_pb2.GetSockOptRequest, context: grpc.ServicerContext) -> nixnetsocket_pb2.GetSockOptResponse:
        ...

    @abc.abstractmethod
    def InetAddr(self, request: nixnetsocket_pb2.InetAddrRequest, context: grpc.ServicerContext) -> nixnetsocket_pb2.InetAddrResponse:
        ...

    @abc.abstractmethod
    def InetAToN(self, request: nixnetsocket_pb2.InetAToNRequest, context: grpc.ServicerContext) -> nixnetsocket_pb2.InetAToNResponse:
        ...

    @abc.abstractmethod
    def InetNToA(self, request: nixnetsocket_pb2.InetNToARequest, context: grpc.ServicerContext) -> nixnetsocket_pb2.InetNToAResponse:
        ...

    @abc.abstractmethod
    def InetNToP(self, request: nixnetsocket_pb2.InetNToPRequest, context: grpc.ServicerContext) -> nixnetsocket_pb2.InetNToPResponse:
        ...

    @abc.abstractmethod
    def InetPToN(self, request: nixnetsocket_pb2.InetPToNRequest, context: grpc.ServicerContext) -> nixnetsocket_pb2.InetPToNResponse:
        ...

    @abc.abstractmethod
    def IpStackClear(self, request: nixnetsocket_pb2.IpStackClearRequest, context: grpc.ServicerContext) -> nixnetsocket_pb2.IpStackClearResponse:
        ...

    @abc.abstractmethod
    def IpStackCreate(self, request: nixnetsocket_pb2.IpStackCreateRequest, context: grpc.ServicerContext) -> nixnetsocket_pb2.IpStackCreateResponse:
        ...

    @abc.abstractmethod
    def IpStackGetAllStacksInfoStr(self, request: nixnetsocket_pb2.IpStackGetAllStacksInfoStrRequest, context: grpc.ServicerContext) -> nixnetsocket_pb2.IpStackGetAllStacksInfoStrResponse:
        ...

    @abc.abstractmethod
    def IpStackGetInfo(self, request: nixnetsocket_pb2.IpStackGetInfoRequest, context: grpc.ServicerContext) -> nixnetsocket_pb2.IpStackGetInfoResponse:
        ...

    @abc.abstractmethod
    def IpStackOpen(self, request: nixnetsocket_pb2.IpStackOpenRequest, context: grpc.ServicerContext) -> nixnetsocket_pb2.IpStackOpenResponse:
        ...

    @abc.abstractmethod
    def IpStackWaitForInterface(self, request: nixnetsocket_pb2.IpStackWaitForInterfaceRequest, context: grpc.ServicerContext) -> nixnetsocket_pb2.IpStackWaitForInterfaceResponse:
        ...

    @abc.abstractmethod
    def Listen(self, request: nixnetsocket_pb2.ListenRequest, context: grpc.ServicerContext) -> nixnetsocket_pb2.ListenResponse:
        ...

    @abc.abstractmethod
    def Recv(self, request: nixnetsocket_pb2.RecvRequest, context: grpc.ServicerContext) -> nixnetsocket_pb2.RecvResponse:
        ...

    @abc.abstractmethod
    def RecvFrom(self, request: nixnetsocket_pb2.RecvFromRequest, context: grpc.ServicerContext) -> nixnetsocket_pb2.RecvFromResponse:
        ...

    @abc.abstractmethod
    def Select(self, request: nixnetsocket_pb2.SelectRequest, context: grpc.ServicerContext) -> nixnetsocket_pb2.SelectResponse:
        ...

    @abc.abstractmethod
    def Send(self, request: nixnetsocket_pb2.SendRequest, context: grpc.ServicerContext) -> nixnetsocket_pb2.SendResponse:
        ...

    @abc.abstractmethod
    def SendTo(self, request: nixnetsocket_pb2.SendToRequest, context: grpc.ServicerContext) -> nixnetsocket_pb2.SendToResponse:
        ...

    @abc.abstractmethod
    def SetSockOpt(self, request: nixnetsocket_pb2.SetSockOptRequest, context: grpc.ServicerContext) -> nixnetsocket_pb2.SetSockOptResponse:
        ...

    @abc.abstractmethod
    def Shutdown(self, request: nixnetsocket_pb2.ShutdownRequest, context: grpc.ServicerContext) -> nixnetsocket_pb2.ShutdownResponse:
        ...

    @abc.abstractmethod
    def Socket(self, request: nixnetsocket_pb2.SocketRequest, context: grpc.ServicerContext) -> nixnetsocket_pb2.SocketResponse:
        ...

    @abc.abstractmethod
    def StrErrR(self, request: nixnetsocket_pb2.StrErrRRequest, context: grpc.ServicerContext) -> nixnetsocket_pb2.StrErrRResponse:
        ...

def add_NiXnetSocketServicer_to_server(servicer: NiXnetSocketServicer, server: grpc.Server) -> None:
    ...
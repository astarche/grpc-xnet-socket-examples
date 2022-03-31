"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from . import nixnetsocket_pb2 as nixnetsocket__pb2

class NiXnetSocketStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Accept = channel.unary_unary('/nixnetsocket_grpc.NiXnetSocket/Accept', request_serializer=nixnetsocket__pb2.AcceptRequest.SerializeToString, response_deserializer=nixnetsocket__pb2.AcceptResponse.FromString)
        self.Bind = channel.unary_unary('/nixnetsocket_grpc.NiXnetSocket/Bind', request_serializer=nixnetsocket__pb2.BindRequest.SerializeToString, response_deserializer=nixnetsocket__pb2.BindResponse.FromString)
        self.Close = channel.unary_unary('/nixnetsocket_grpc.NiXnetSocket/Close', request_serializer=nixnetsocket__pb2.CloseRequest.SerializeToString, response_deserializer=nixnetsocket__pb2.CloseResponse.FromString)
        self.Connect = channel.unary_unary('/nixnetsocket_grpc.NiXnetSocket/Connect', request_serializer=nixnetsocket__pb2.ConnectRequest.SerializeToString, response_deserializer=nixnetsocket__pb2.ConnectResponse.FromString)
        self.FdIsSet = channel.unary_unary('/nixnetsocket_grpc.NiXnetSocket/FdIsSet', request_serializer=nixnetsocket__pb2.FdIsSetRequest.SerializeToString, response_deserializer=nixnetsocket__pb2.FdIsSetResponse.FromString)
        self.GetAddrInfo = channel.unary_unary('/nixnetsocket_grpc.NiXnetSocket/GetAddrInfo', request_serializer=nixnetsocket__pb2.GetAddrInfoRequest.SerializeToString, response_deserializer=nixnetsocket__pb2.GetAddrInfoResponse.FromString)
        self.GetNameInfo = channel.unary_unary('/nixnetsocket_grpc.NiXnetSocket/GetNameInfo', request_serializer=nixnetsocket__pb2.GetNameInfoRequest.SerializeToString, response_deserializer=nixnetsocket__pb2.GetNameInfoResponse.FromString)
        self.GetPeerName = channel.unary_unary('/nixnetsocket_grpc.NiXnetSocket/GetPeerName', request_serializer=nixnetsocket__pb2.GetPeerNameRequest.SerializeToString, response_deserializer=nixnetsocket__pb2.GetPeerNameResponse.FromString)
        self.GetSockName = channel.unary_unary('/nixnetsocket_grpc.NiXnetSocket/GetSockName', request_serializer=nixnetsocket__pb2.GetSockNameRequest.SerializeToString, response_deserializer=nixnetsocket__pb2.GetSockNameResponse.FromString)
        self.GetSockOpt = channel.unary_unary('/nixnetsocket_grpc.NiXnetSocket/GetSockOpt', request_serializer=nixnetsocket__pb2.GetSockOptRequest.SerializeToString, response_deserializer=nixnetsocket__pb2.GetSockOptResponse.FromString)
        self.InetAddr = channel.unary_unary('/nixnetsocket_grpc.NiXnetSocket/InetAddr', request_serializer=nixnetsocket__pb2.InetAddrRequest.SerializeToString, response_deserializer=nixnetsocket__pb2.InetAddrResponse.FromString)
        self.InetAToN = channel.unary_unary('/nixnetsocket_grpc.NiXnetSocket/InetAToN', request_serializer=nixnetsocket__pb2.InetAToNRequest.SerializeToString, response_deserializer=nixnetsocket__pb2.InetAToNResponse.FromString)
        self.InetNToA = channel.unary_unary('/nixnetsocket_grpc.NiXnetSocket/InetNToA', request_serializer=nixnetsocket__pb2.InetNToARequest.SerializeToString, response_deserializer=nixnetsocket__pb2.InetNToAResponse.FromString)
        self.InetNToP = channel.unary_unary('/nixnetsocket_grpc.NiXnetSocket/InetNToP', request_serializer=nixnetsocket__pb2.InetNToPRequest.SerializeToString, response_deserializer=nixnetsocket__pb2.InetNToPResponse.FromString)
        self.InetPToN = channel.unary_unary('/nixnetsocket_grpc.NiXnetSocket/InetPToN', request_serializer=nixnetsocket__pb2.InetPToNRequest.SerializeToString, response_deserializer=nixnetsocket__pb2.InetPToNResponse.FromString)
        self.IpStackClear = channel.unary_unary('/nixnetsocket_grpc.NiXnetSocket/IpStackClear', request_serializer=nixnetsocket__pb2.IpStackClearRequest.SerializeToString, response_deserializer=nixnetsocket__pb2.IpStackClearResponse.FromString)
        self.IpStackCreate = channel.unary_unary('/nixnetsocket_grpc.NiXnetSocket/IpStackCreate', request_serializer=nixnetsocket__pb2.IpStackCreateRequest.SerializeToString, response_deserializer=nixnetsocket__pb2.IpStackCreateResponse.FromString)
        self.IpStackGetAllStacksInfoStr = channel.unary_unary('/nixnetsocket_grpc.NiXnetSocket/IpStackGetAllStacksInfoStr', request_serializer=nixnetsocket__pb2.IpStackGetAllStacksInfoStrRequest.SerializeToString, response_deserializer=nixnetsocket__pb2.IpStackGetAllStacksInfoStrResponse.FromString)
        self.IpStackGetInfo = channel.unary_unary('/nixnetsocket_grpc.NiXnetSocket/IpStackGetInfo', request_serializer=nixnetsocket__pb2.IpStackGetInfoRequest.SerializeToString, response_deserializer=nixnetsocket__pb2.IpStackGetInfoResponse.FromString)
        self.IpStackOpen = channel.unary_unary('/nixnetsocket_grpc.NiXnetSocket/IpStackOpen', request_serializer=nixnetsocket__pb2.IpStackOpenRequest.SerializeToString, response_deserializer=nixnetsocket__pb2.IpStackOpenResponse.FromString)
        self.IpStackWaitForInterface = channel.unary_unary('/nixnetsocket_grpc.NiXnetSocket/IpStackWaitForInterface', request_serializer=nixnetsocket__pb2.IpStackWaitForInterfaceRequest.SerializeToString, response_deserializer=nixnetsocket__pb2.IpStackWaitForInterfaceResponse.FromString)
        self.Listen = channel.unary_unary('/nixnetsocket_grpc.NiXnetSocket/Listen', request_serializer=nixnetsocket__pb2.ListenRequest.SerializeToString, response_deserializer=nixnetsocket__pb2.ListenResponse.FromString)
        self.Recv = channel.unary_unary('/nixnetsocket_grpc.NiXnetSocket/Recv', request_serializer=nixnetsocket__pb2.RecvRequest.SerializeToString, response_deserializer=nixnetsocket__pb2.RecvResponse.FromString)
        self.RecvFrom = channel.unary_unary('/nixnetsocket_grpc.NiXnetSocket/RecvFrom', request_serializer=nixnetsocket__pb2.RecvFromRequest.SerializeToString, response_deserializer=nixnetsocket__pb2.RecvFromResponse.FromString)
        self.Select = channel.unary_unary('/nixnetsocket_grpc.NiXnetSocket/Select', request_serializer=nixnetsocket__pb2.SelectRequest.SerializeToString, response_deserializer=nixnetsocket__pb2.SelectResponse.FromString)
        self.Send = channel.unary_unary('/nixnetsocket_grpc.NiXnetSocket/Send', request_serializer=nixnetsocket__pb2.SendRequest.SerializeToString, response_deserializer=nixnetsocket__pb2.SendResponse.FromString)
        self.SendTo = channel.unary_unary('/nixnetsocket_grpc.NiXnetSocket/SendTo', request_serializer=nixnetsocket__pb2.SendToRequest.SerializeToString, response_deserializer=nixnetsocket__pb2.SendToResponse.FromString)
        self.SetSockOpt = channel.unary_unary('/nixnetsocket_grpc.NiXnetSocket/SetSockOpt', request_serializer=nixnetsocket__pb2.SetSockOptRequest.SerializeToString, response_deserializer=nixnetsocket__pb2.SetSockOptResponse.FromString)
        self.Shutdown = channel.unary_unary('/nixnetsocket_grpc.NiXnetSocket/Shutdown', request_serializer=nixnetsocket__pb2.ShutdownRequest.SerializeToString, response_deserializer=nixnetsocket__pb2.ShutdownResponse.FromString)
        self.Socket = channel.unary_unary('/nixnetsocket_grpc.NiXnetSocket/Socket', request_serializer=nixnetsocket__pb2.SocketRequest.SerializeToString, response_deserializer=nixnetsocket__pb2.SocketResponse.FromString)
        self.StrErrR = channel.unary_unary('/nixnetsocket_grpc.NiXnetSocket/StrErrR', request_serializer=nixnetsocket__pb2.StrErrRRequest.SerializeToString, response_deserializer=nixnetsocket__pb2.StrErrRResponse.FromString)

class NiXnetSocketServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Accept(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Bind(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Close(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Connect(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FdIsSet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAddrInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNameInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPeerName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSockName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSockOpt(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InetAddr(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InetAToN(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InetNToA(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InetNToP(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InetPToN(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IpStackClear(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IpStackCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IpStackGetAllStacksInfoStr(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IpStackGetInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IpStackOpen(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IpStackWaitForInterface(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Listen(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Recv(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RecvFrom(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Select(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Send(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendTo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetSockOpt(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Shutdown(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Socket(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StrErrR(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_NiXnetSocketServicer_to_server(servicer, server):
    rpc_method_handlers = {'Accept': grpc.unary_unary_rpc_method_handler(servicer.Accept, request_deserializer=nixnetsocket__pb2.AcceptRequest.FromString, response_serializer=nixnetsocket__pb2.AcceptResponse.SerializeToString), 'Bind': grpc.unary_unary_rpc_method_handler(servicer.Bind, request_deserializer=nixnetsocket__pb2.BindRequest.FromString, response_serializer=nixnetsocket__pb2.BindResponse.SerializeToString), 'Close': grpc.unary_unary_rpc_method_handler(servicer.Close, request_deserializer=nixnetsocket__pb2.CloseRequest.FromString, response_serializer=nixnetsocket__pb2.CloseResponse.SerializeToString), 'Connect': grpc.unary_unary_rpc_method_handler(servicer.Connect, request_deserializer=nixnetsocket__pb2.ConnectRequest.FromString, response_serializer=nixnetsocket__pb2.ConnectResponse.SerializeToString), 'FdIsSet': grpc.unary_unary_rpc_method_handler(servicer.FdIsSet, request_deserializer=nixnetsocket__pb2.FdIsSetRequest.FromString, response_serializer=nixnetsocket__pb2.FdIsSetResponse.SerializeToString), 'GetAddrInfo': grpc.unary_unary_rpc_method_handler(servicer.GetAddrInfo, request_deserializer=nixnetsocket__pb2.GetAddrInfoRequest.FromString, response_serializer=nixnetsocket__pb2.GetAddrInfoResponse.SerializeToString), 'GetNameInfo': grpc.unary_unary_rpc_method_handler(servicer.GetNameInfo, request_deserializer=nixnetsocket__pb2.GetNameInfoRequest.FromString, response_serializer=nixnetsocket__pb2.GetNameInfoResponse.SerializeToString), 'GetPeerName': grpc.unary_unary_rpc_method_handler(servicer.GetPeerName, request_deserializer=nixnetsocket__pb2.GetPeerNameRequest.FromString, response_serializer=nixnetsocket__pb2.GetPeerNameResponse.SerializeToString), 'GetSockName': grpc.unary_unary_rpc_method_handler(servicer.GetSockName, request_deserializer=nixnetsocket__pb2.GetSockNameRequest.FromString, response_serializer=nixnetsocket__pb2.GetSockNameResponse.SerializeToString), 'GetSockOpt': grpc.unary_unary_rpc_method_handler(servicer.GetSockOpt, request_deserializer=nixnetsocket__pb2.GetSockOptRequest.FromString, response_serializer=nixnetsocket__pb2.GetSockOptResponse.SerializeToString), 'InetAddr': grpc.unary_unary_rpc_method_handler(servicer.InetAddr, request_deserializer=nixnetsocket__pb2.InetAddrRequest.FromString, response_serializer=nixnetsocket__pb2.InetAddrResponse.SerializeToString), 'InetAToN': grpc.unary_unary_rpc_method_handler(servicer.InetAToN, request_deserializer=nixnetsocket__pb2.InetAToNRequest.FromString, response_serializer=nixnetsocket__pb2.InetAToNResponse.SerializeToString), 'InetNToA': grpc.unary_unary_rpc_method_handler(servicer.InetNToA, request_deserializer=nixnetsocket__pb2.InetNToARequest.FromString, response_serializer=nixnetsocket__pb2.InetNToAResponse.SerializeToString), 'InetNToP': grpc.unary_unary_rpc_method_handler(servicer.InetNToP, request_deserializer=nixnetsocket__pb2.InetNToPRequest.FromString, response_serializer=nixnetsocket__pb2.InetNToPResponse.SerializeToString), 'InetPToN': grpc.unary_unary_rpc_method_handler(servicer.InetPToN, request_deserializer=nixnetsocket__pb2.InetPToNRequest.FromString, response_serializer=nixnetsocket__pb2.InetPToNResponse.SerializeToString), 'IpStackClear': grpc.unary_unary_rpc_method_handler(servicer.IpStackClear, request_deserializer=nixnetsocket__pb2.IpStackClearRequest.FromString, response_serializer=nixnetsocket__pb2.IpStackClearResponse.SerializeToString), 'IpStackCreate': grpc.unary_unary_rpc_method_handler(servicer.IpStackCreate, request_deserializer=nixnetsocket__pb2.IpStackCreateRequest.FromString, response_serializer=nixnetsocket__pb2.IpStackCreateResponse.SerializeToString), 'IpStackGetAllStacksInfoStr': grpc.unary_unary_rpc_method_handler(servicer.IpStackGetAllStacksInfoStr, request_deserializer=nixnetsocket__pb2.IpStackGetAllStacksInfoStrRequest.FromString, response_serializer=nixnetsocket__pb2.IpStackGetAllStacksInfoStrResponse.SerializeToString), 'IpStackGetInfo': grpc.unary_unary_rpc_method_handler(servicer.IpStackGetInfo, request_deserializer=nixnetsocket__pb2.IpStackGetInfoRequest.FromString, response_serializer=nixnetsocket__pb2.IpStackGetInfoResponse.SerializeToString), 'IpStackOpen': grpc.unary_unary_rpc_method_handler(servicer.IpStackOpen, request_deserializer=nixnetsocket__pb2.IpStackOpenRequest.FromString, response_serializer=nixnetsocket__pb2.IpStackOpenResponse.SerializeToString), 'IpStackWaitForInterface': grpc.unary_unary_rpc_method_handler(servicer.IpStackWaitForInterface, request_deserializer=nixnetsocket__pb2.IpStackWaitForInterfaceRequest.FromString, response_serializer=nixnetsocket__pb2.IpStackWaitForInterfaceResponse.SerializeToString), 'Listen': grpc.unary_unary_rpc_method_handler(servicer.Listen, request_deserializer=nixnetsocket__pb2.ListenRequest.FromString, response_serializer=nixnetsocket__pb2.ListenResponse.SerializeToString), 'Recv': grpc.unary_unary_rpc_method_handler(servicer.Recv, request_deserializer=nixnetsocket__pb2.RecvRequest.FromString, response_serializer=nixnetsocket__pb2.RecvResponse.SerializeToString), 'RecvFrom': grpc.unary_unary_rpc_method_handler(servicer.RecvFrom, request_deserializer=nixnetsocket__pb2.RecvFromRequest.FromString, response_serializer=nixnetsocket__pb2.RecvFromResponse.SerializeToString), 'Select': grpc.unary_unary_rpc_method_handler(servicer.Select, request_deserializer=nixnetsocket__pb2.SelectRequest.FromString, response_serializer=nixnetsocket__pb2.SelectResponse.SerializeToString), 'Send': grpc.unary_unary_rpc_method_handler(servicer.Send, request_deserializer=nixnetsocket__pb2.SendRequest.FromString, response_serializer=nixnetsocket__pb2.SendResponse.SerializeToString), 'SendTo': grpc.unary_unary_rpc_method_handler(servicer.SendTo, request_deserializer=nixnetsocket__pb2.SendToRequest.FromString, response_serializer=nixnetsocket__pb2.SendToResponse.SerializeToString), 'SetSockOpt': grpc.unary_unary_rpc_method_handler(servicer.SetSockOpt, request_deserializer=nixnetsocket__pb2.SetSockOptRequest.FromString, response_serializer=nixnetsocket__pb2.SetSockOptResponse.SerializeToString), 'Shutdown': grpc.unary_unary_rpc_method_handler(servicer.Shutdown, request_deserializer=nixnetsocket__pb2.ShutdownRequest.FromString, response_serializer=nixnetsocket__pb2.ShutdownResponse.SerializeToString), 'Socket': grpc.unary_unary_rpc_method_handler(servicer.Socket, request_deserializer=nixnetsocket__pb2.SocketRequest.FromString, response_serializer=nixnetsocket__pb2.SocketResponse.SerializeToString), 'StrErrR': grpc.unary_unary_rpc_method_handler(servicer.StrErrR, request_deserializer=nixnetsocket__pb2.StrErrRRequest.FromString, response_serializer=nixnetsocket__pb2.StrErrRResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('nixnetsocket_grpc.NiXnetSocket', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class NiXnetSocket(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Accept(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nixnetsocket_grpc.NiXnetSocket/Accept', nixnetsocket__pb2.AcceptRequest.SerializeToString, nixnetsocket__pb2.AcceptResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Bind(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nixnetsocket_grpc.NiXnetSocket/Bind', nixnetsocket__pb2.BindRequest.SerializeToString, nixnetsocket__pb2.BindResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Close(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nixnetsocket_grpc.NiXnetSocket/Close', nixnetsocket__pb2.CloseRequest.SerializeToString, nixnetsocket__pb2.CloseResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Connect(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nixnetsocket_grpc.NiXnetSocket/Connect', nixnetsocket__pb2.ConnectRequest.SerializeToString, nixnetsocket__pb2.ConnectResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FdIsSet(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nixnetsocket_grpc.NiXnetSocket/FdIsSet', nixnetsocket__pb2.FdIsSetRequest.SerializeToString, nixnetsocket__pb2.FdIsSetResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAddrInfo(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nixnetsocket_grpc.NiXnetSocket/GetAddrInfo', nixnetsocket__pb2.GetAddrInfoRequest.SerializeToString, nixnetsocket__pb2.GetAddrInfoResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetNameInfo(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nixnetsocket_grpc.NiXnetSocket/GetNameInfo', nixnetsocket__pb2.GetNameInfoRequest.SerializeToString, nixnetsocket__pb2.GetNameInfoResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPeerName(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nixnetsocket_grpc.NiXnetSocket/GetPeerName', nixnetsocket__pb2.GetPeerNameRequest.SerializeToString, nixnetsocket__pb2.GetPeerNameResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSockName(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nixnetsocket_grpc.NiXnetSocket/GetSockName', nixnetsocket__pb2.GetSockNameRequest.SerializeToString, nixnetsocket__pb2.GetSockNameResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSockOpt(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nixnetsocket_grpc.NiXnetSocket/GetSockOpt', nixnetsocket__pb2.GetSockOptRequest.SerializeToString, nixnetsocket__pb2.GetSockOptResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InetAddr(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nixnetsocket_grpc.NiXnetSocket/InetAddr', nixnetsocket__pb2.InetAddrRequest.SerializeToString, nixnetsocket__pb2.InetAddrResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InetAToN(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nixnetsocket_grpc.NiXnetSocket/InetAToN', nixnetsocket__pb2.InetAToNRequest.SerializeToString, nixnetsocket__pb2.InetAToNResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InetNToA(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nixnetsocket_grpc.NiXnetSocket/InetNToA', nixnetsocket__pb2.InetNToARequest.SerializeToString, nixnetsocket__pb2.InetNToAResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InetNToP(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nixnetsocket_grpc.NiXnetSocket/InetNToP', nixnetsocket__pb2.InetNToPRequest.SerializeToString, nixnetsocket__pb2.InetNToPResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InetPToN(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nixnetsocket_grpc.NiXnetSocket/InetPToN', nixnetsocket__pb2.InetPToNRequest.SerializeToString, nixnetsocket__pb2.InetPToNResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def IpStackClear(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nixnetsocket_grpc.NiXnetSocket/IpStackClear', nixnetsocket__pb2.IpStackClearRequest.SerializeToString, nixnetsocket__pb2.IpStackClearResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def IpStackCreate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nixnetsocket_grpc.NiXnetSocket/IpStackCreate', nixnetsocket__pb2.IpStackCreateRequest.SerializeToString, nixnetsocket__pb2.IpStackCreateResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def IpStackGetAllStacksInfoStr(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nixnetsocket_grpc.NiXnetSocket/IpStackGetAllStacksInfoStr', nixnetsocket__pb2.IpStackGetAllStacksInfoStrRequest.SerializeToString, nixnetsocket__pb2.IpStackGetAllStacksInfoStrResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def IpStackGetInfo(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nixnetsocket_grpc.NiXnetSocket/IpStackGetInfo', nixnetsocket__pb2.IpStackGetInfoRequest.SerializeToString, nixnetsocket__pb2.IpStackGetInfoResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def IpStackOpen(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nixnetsocket_grpc.NiXnetSocket/IpStackOpen', nixnetsocket__pb2.IpStackOpenRequest.SerializeToString, nixnetsocket__pb2.IpStackOpenResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def IpStackWaitForInterface(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nixnetsocket_grpc.NiXnetSocket/IpStackWaitForInterface', nixnetsocket__pb2.IpStackWaitForInterfaceRequest.SerializeToString, nixnetsocket__pb2.IpStackWaitForInterfaceResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Listen(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nixnetsocket_grpc.NiXnetSocket/Listen', nixnetsocket__pb2.ListenRequest.SerializeToString, nixnetsocket__pb2.ListenResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Recv(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nixnetsocket_grpc.NiXnetSocket/Recv', nixnetsocket__pb2.RecvRequest.SerializeToString, nixnetsocket__pb2.RecvResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RecvFrom(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nixnetsocket_grpc.NiXnetSocket/RecvFrom', nixnetsocket__pb2.RecvFromRequest.SerializeToString, nixnetsocket__pb2.RecvFromResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Select(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nixnetsocket_grpc.NiXnetSocket/Select', nixnetsocket__pb2.SelectRequest.SerializeToString, nixnetsocket__pb2.SelectResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Send(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nixnetsocket_grpc.NiXnetSocket/Send', nixnetsocket__pb2.SendRequest.SerializeToString, nixnetsocket__pb2.SendResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendTo(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nixnetsocket_grpc.NiXnetSocket/SendTo', nixnetsocket__pb2.SendToRequest.SerializeToString, nixnetsocket__pb2.SendToResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetSockOpt(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nixnetsocket_grpc.NiXnetSocket/SetSockOpt', nixnetsocket__pb2.SetSockOptRequest.SerializeToString, nixnetsocket__pb2.SetSockOptResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Shutdown(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nixnetsocket_grpc.NiXnetSocket/Shutdown', nixnetsocket__pb2.ShutdownRequest.SerializeToString, nixnetsocket__pb2.ShutdownResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Socket(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nixnetsocket_grpc.NiXnetSocket/Socket', nixnetsocket__pb2.SocketRequest.SerializeToString, nixnetsocket__pb2.SocketResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StrErrR(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nixnetsocket_grpc.NiXnetSocket/StrErrR', nixnetsocket__pb2.StrErrRRequest.SerializeToString, nixnetsocket__pb2.StrErrRResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
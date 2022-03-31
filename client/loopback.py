"""Example XNET Automotive Ethernet client using loopback TCP over IPv4."""
import click
import xnetgrpc.nixnetsocket_pb2 as xnetsocket
from client._shared import raise_if_error, grpc_device_session

CONFIG = """
{
   "schema":"file:///NIXNET_Documentation/xnetIpStackSchema-03.json",
   "xnetInterfaces":[
      {
         "MACs":[
            {
               "VLANs":[
                  {
                     "IPv4":{
                        "DAD":false,
                        "mode":"static",
                        "staticAddresses":[
                           {
                              "address":"10.0.0.0",
                              "subnetMask":"255.0.0.0"
                           }
                        ]
                     },
                     "IPv6":{
                        "mode":"enabled"
                     },
                     "isTagged":false,
                     "name":""
                  }
               ],
               "address":"generated",
               "name":""
            }
         ],
         "name":"ENET1"
      }
   ]
}"""


DATA = b"HelloWorld"


@click.command()
@click.option(
    "-s",
    "--server",
    prompt="Grpc-device server",
    help="Address of the XNET device running grpc-device server.",
)
def _loopback(server: str):
    with grpc_device_session(server) as client:
        stack = raise_if_error(client.IpStackCreate(xnetsocket.IpStackCreateRequest(config=CONFIG)))
        listener = raise_if_error(
            client.Socket(
                xnetsocket.SocketRequest(
                    stack_ref=stack.stack_ref,
                    domain=xnetsocket.ADDRESS_FAMILY_INET,
                    protocol=xnetsocket.IP_PROTOCOL_TCP,
                    type=xnetsocket.SOCKET_PROTOCOL_TYPE_STREAM,
                )
            )
        )
        client_socket = raise_if_error(
            client.Socket(
                xnetsocket.SocketRequest(
                    stack_ref=stack.stack_ref,
                    domain=xnetsocket.ADDRESS_FAMILY_INET,
                    protocol=xnetsocket.IP_PROTOCOL_TCP,
                    type=xnetsocket.SOCKET_PROTOCOL_TYPE_STREAM,
                )
            )
        )
        pton = raise_if_error(
            client.InetPToN(
                xnetsocket.InetPToNRequest(
                    stack_ref=stack.stack_ref,
                    af=xnetsocket.ADDRESS_FAMILY_INET,
                    src="127.0.0.1",
                )
            )
        )
        addr_ipv4 = xnetsocket.SockAddrIn(addr=pton.dst.ipv4)
        bind_addr = xnetsocket.SockAddr(ipv4=addr_ipv4)
        raise_if_error(client.Bind(xnetsocket.BindRequest(socket=listener.socket, name=bind_addr)))
        listener_sock_name = raise_if_error(
            client.GetSockName(xnetsocket.GetSockNameRequest(socket=listener.socket))
        )
        raise_if_error(client.Listen(xnetsocket.ListenRequest(socket=listener.socket, backlog=10)))
        raise_if_error(
            client.Connect(
                xnetsocket.ConnectRequest(socket=client_socket.socket, name=listener_sock_name.addr)
            )
        )
        server_socket = raise_if_error(
            client.Accept(xnetsocket.AcceptRequest(socket=listener.socket))
        )

        raise_if_error(
            client.Send(xnetsocket.SendRequest(socket=client_socket.socket, dataptr=DATA))
        )
        recv = raise_if_error(
            client.Recv(xnetsocket.RecvRequest(socket=server_socket.socket, size=len(DATA)))
        )

        print(recv.mem)


if __name__ == "__main__":
    _loopback()

"""Example XNET Automotive Ethernet client using UDP over IPv4 with 2 ENET ports."""

import click
import xnetgrpc.nixnetsocket_pb2 as xnetsocket
import xnetgrpc.nixnetsocket_pb2_grpc as xnetsocket_grpc
import xnetgrpc.session_pb2 as session_pb
from client._shared import raise_if_error, grpc_device_session

ENET1_CONFIG = """
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
                              "address":"10.0.0.1",
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


ENET4_CONFIG = """
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
                              "address":"10.0.0.2",
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
         "name":"ENET4"
      }
   ]
}"""


TX_DATA = b"HelloUdpWorld"


def _lookup_ipv4_addr(
    client: xnetsocket_grpc.NiXnetSocketStub, stack: session_pb.Session, address: str
) -> xnetsocket.SockAddr:
    pton = raise_if_error(
        client.InetPToN(
            xnetsocket.InetPToNRequest(
                stack_ref=stack,
                af=xnetsocket.ADDRESS_FAMILY_INET,
                src=address,
            )
        )
    )
    addr_ipv4 = xnetsocket.SockAddrIn(addr=pton.dst.ipv4, port=5544)
    return xnetsocket.SockAddr(ipv4=addr_ipv4)


def _create_ip_mreq_sock_opt_data(
    addr: xnetsocket.SockAddr, multicast_addr: xnetsocket.SockAddr
) -> xnetsocket.SockOptData:
    ip_mreq = xnetsocket.IPMReq(
        imr_interface=addr.ipv4.addr, imr_multiaddr=multicast_addr.ipv4.addr
    )
    return xnetsocket.SockOptData(data_ip_mreq=ip_mreq)


@click.command()
@click.option(
    "-s",
    "--server",
    prompt="Grpc-device server",
    help="Address of the XNET device running grpc-device server.",
)
def _udp(server: str):
    with grpc_device_session(server) as client:
        enet1 = raise_if_error(
            client.IpStackCreate(xnetsocket.IpStackCreateRequest(config=ENET1_CONFIG))
        )
        enet4 = raise_if_error(
            client.IpStackCreate(xnetsocket.IpStackCreateRequest(config=ENET4_CONFIG))
        )

        multicast_addr = _lookup_ipv4_addr(client, enet1.stack_ref, "233.252.0.1")

        rx = raise_if_error(
            client.Socket(
                xnetsocket.SocketRequest(
                    stack_ref=enet1.stack_ref,
                    domain=xnetsocket.ADDRESS_FAMILY_INET,
                    protocol=xnetsocket.IP_PROTOCOL_UDP,
                    type=xnetsocket.SOCKET_PROTOCOL_TYPE_DGRAM,
                )
            )
        )
        rx_addr = _lookup_ipv4_addr(client, enet1.stack_ref, "10.0.0.1")
        raise_if_error(client.Bind(xnetsocket.BindRequest(socket=rx.socket, name=rx_addr)))
        raise_if_error(
            client.SetSockOpt(
                xnetsocket.SetSockOptRequest(
                    socket=rx.socket,
                    level_raw=0,
                    optname=xnetsocket.OPT_NAME_IP_ADD_MEMBERSHIP,
                    opt_data=_create_ip_mreq_sock_opt_data(rx_addr, multicast_addr),
                )
            )
        )
        tx = raise_if_error(
            client.Socket(
                xnetsocket.SocketRequest(
                    stack_ref=enet4.stack_ref,
                    domain=xnetsocket.ADDRESS_FAMILY_INET,
                    protocol=xnetsocket.IP_PROTOCOL_UDP,
                    type=xnetsocket.SOCKET_PROTOCOL_TYPE_DGRAM,
                )
            )
        )
        tx_addr = _lookup_ipv4_addr(client, enet1.stack_ref, "10.0.0.2")
        raise_if_error(client.Bind(xnetsocket.BindRequest(socket=tx.socket, name=tx_addr)))
        raise_if_error(
            client.SetSockOpt(
                xnetsocket.SetSockOptRequest(
                    socket=tx.socket,
                    level_raw=0,
                    optname=xnetsocket.OPT_NAME_IP_ADD_MEMBERSHIP,
                    opt_data=_create_ip_mreq_sock_opt_data(tx_addr, multicast_addr),
                )
            )
        )

        raise_if_error(
            client.SendTo(
                xnetsocket.SendToRequest(socket=tx.socket, dataptr=TX_DATA, to=multicast_addr)
            )
        )

        recv = raise_if_error(
            client.Recv(xnetsocket.RecvRequest(socket=rx.socket, size=len(TX_DATA)))
        )

        print(recv.mem)


if __name__ == "__main__":
    _udp()

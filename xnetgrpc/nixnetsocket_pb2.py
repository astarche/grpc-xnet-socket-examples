"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from . import session_pb2 as session__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12nixnetsocket.proto\x12\x11nixnetsocket_grpc\x1a\rsession.proto\x1a\x1egoogle/protobuf/duration.proto"w\n\tIPAddress\x120\n\x06family\x18\x01 \x01(\x0e2 .nixnetsocket_grpc.AddressFamily\x12\x0f\n\x07address\x18\x02 \x01(\t\x12\x10\n\x08net_mask\x18\x03 \x01(\t\x12\x15\n\rprefix_length\x18\x04 \x01(\r"S\n\x0eGatewayAddress\x120\n\x06family\x18\x01 \x01(\x0e2 .nixnetsocket_grpc.AddressFamily\x12\x0f\n\x07address\x18\x02 \x01(\t"\xae\x02\n\x10VirtualInterface\x12\x1b\n\x13xnet_interface_name\x18\x01 \x01(\t\x12\x11\n\tvlan_name\x18\x02 \x01(\t\x12\x13\n\x0bmac_address\x18\x03 \x01(\t\x12\x0f\n\x07mac_mtu\x18\x04 \x01(\r\x12@\n\x12operational_status\x18\x05 \x01(\x0e2$.nixnetsocket_grpc.OperationalStatus\x12\x10\n\x08if_index\x18\x06 \x01(\r\x122\n\x0cip_addresses\x18\x07 \x03(\x0b2\x1c.nixnetsocket_grpc.IPAddress\x12<\n\x11gateway_addresses\x18\x08 \x03(\x0b2!.nixnetsocket_grpc.GatewayAddress"\x17\n\x07In6Addr\x12\x0c\n\x04addr\x18\x01 \x01(\x0c"\x16\n\x06InAddr\x12\x0c\n\x04addr\x18\x01 \x01(\r"e\n\x04Addr\x12)\n\x04ipv4\x18\x01 \x01(\x0b2\x19.nixnetsocket_grpc.InAddrH\x00\x12*\n\x04ipv6\x18\x02 \x01(\x0b2\x1a.nixnetsocket_grpc.In6AddrH\x00B\x06\n\x04addr"C\n\nSockAddrIn\x12\x0c\n\x04port\x18\x01 \x01(\r\x12\'\n\x04addr\x18\x02 \x01(\x0b2\x19.nixnetsocket_grpc.InAddr"j\n\x0bSockAddrIn6\x12\x0c\n\x04port\x18\x01 \x01(\r\x12\x11\n\tflow_info\x18\x02 \x01(\r\x12(\n\x04addr\x18\x03 \x01(\x0b2\x1a.nixnetsocket_grpc.In6Addr\x12\x10\n\x08scope_id\x18\x04 \x01(\r"q\n\x08SockAddr\x12-\n\x04ipv4\x18\x01 \x01(\x0b2\x1d.nixnetsocket_grpc.SockAddrInH\x00\x12.\n\x04ipv6\x18\x02 \x01(\x0b2\x1e.nixnetsocket_grpc.SockAddrIn6H\x00B\x06\n\x04addr"\xb3\x02\n\x08AddrInfo\x128\n\x0bflags_array\x18\x01 \x03(\x0e2#.nixnetsocket_grpc.GetAddrInfoFlags\x12\x11\n\tflags_raw\x18\x02 \x01(\x05\x120\n\x06family\x18\x03 \x01(\x0e2 .nixnetsocket_grpc.AddressFamily\x128\n\tsock_type\x18\x04 \x01(\x0e2%.nixnetsocket_grpc.SocketProtocolType\x12/\n\x08protocol\x18\x05 \x01(\x0e2\x1d.nixnetsocket_grpc.IPProtocol\x12)\n\x04addr\x18\x06 \x01(\x0b2\x1b.nixnetsocket_grpc.SockAddr\x12\x12\n\ncanon_name\x18\x07 \x01(\t"\xf8\x01\n\x0cAddrInfoHint\x128\n\x0bflags_array\x18\x01 \x03(\x0e2#.nixnetsocket_grpc.GetAddrInfoFlags\x12\x11\n\tflags_raw\x18\x02 \x01(\x05\x120\n\x06family\x18\x03 \x01(\x0e2 .nixnetsocket_grpc.AddressFamily\x128\n\tsock_type\x18\x04 \x01(\x0e2%.nixnetsocket_grpc.SocketProtocolType\x12/\n\x08protocol\x18\x05 \x01(\x0e2\x1d.nixnetsocket_grpc.IPProtocol"+\n\x06Linger\x12\x0f\n\x07l_onoff\x18\x01 \x01(\x05\x12\x10\n\x08l_linger\x18\x02 \x01(\x05"l\n\x06IPMReq\x120\n\rimr_multiaddr\x18\x01 \x01(\x0b2\x19.nixnetsocket_grpc.InAddr\x120\n\rimr_interface\x18\x02 \x01(\x0b2\x19.nixnetsocket_grpc.InAddr"Z\n\x08IPv6MReq\x124\n\x10ipv6mr_multiaddr\x18\x01 \x01(\x0b2\x1a.nixnetsocket_grpc.In6Addr\x12\x18\n\x10ipv6mr_interface\x18\x02 \x01(\x05"\xf3\x01\n\x0bSockOptData\x12\x14\n\ndata_int32\x18\x01 \x01(\x05H\x00\x12\x13\n\tdata_bool\x18\x02 \x01(\x08H\x00\x12\x15\n\x0bdata_string\x18\x03 \x01(\tH\x00\x120\n\x0bdata_linger\x18\x04 \x01(\x0b2\x19.nixnetsocket_grpc.LingerH\x00\x121\n\x0cdata_ip_mreq\x18\x05 \x01(\x0b2\x19.nixnetsocket_grpc.IPMReqH\x00\x125\n\x0edata_ipv6_mreq\x18\x06 \x01(\x0b2\x1b.nixnetsocket_grpc.IPv6MReqH\x00B\x06\n\x04data"M\n\rAcceptRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12&\n\x06socket\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session"\x9d\x01\n\x0eAcceptResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12)\n\x04addr\x18\x02 \x01(\x0b2\x1b.nixnetsocket_grpc.SockAddr\x12&\n\x06socket\x18\x03 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rerror_message\x18\x04 \x01(\t\x12\x11\n\terror_num\x18\x05 \x01(\x05"`\n\x0bBindRequest\x12&\n\x06socket\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12)\n\x04name\x18\x02 \x01(\x0b2\x1b.nixnetsocket_grpc.SockAddr"H\n\x0cBindResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rerror_message\x18\x02 \x01(\t\x12\x11\n\terror_num\x18\x03 \x01(\x05"6\n\x0cCloseRequest\x12&\n\x06socket\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"I\n\rCloseResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rerror_message\x18\x02 \x01(\t\x12\x11\n\terror_num\x18\x03 \x01(\x05"c\n\x0eConnectRequest\x12&\n\x06socket\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12)\n\x04name\x18\x02 \x01(\x0b2\x1b.nixnetsocket_grpc.SockAddr"K\n\x0fConnectResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rerror_message\x18\x02 \x01(\t\x12\x11\n\terror_num\x18\x03 \x01(\x05"Y\n\x0eFdIsSetRequest\x12"\n\x02fd\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12#\n\x03set\x18\x02 \x03(\x0b2\x16.nidevice_grpc.Session"[\n\x0fFdIsSetResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0e\n\x06is_set\x18\x02 \x01(\x05\x12\x15\n\rerror_message\x18\x03 \x01(\t\x12\x11\n\terror_num\x18\x04 \x01(\x05"\x8e\x01\n\x12GetAddrInfoRequest\x12)\n\tstack_ref\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0c\n\x04node\x18\x02 \x01(\t\x12\x0f\n\x07service\x18\x03 \x01(\t\x12.\n\x05hints\x18\x04 \x01(\x0b2\x1f.nixnetsocket_grpc.AddrInfoHint"y\n\x13GetAddrInfoResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12(\n\x03res\x18\x02 \x03(\x0b2\x1b.nixnetsocket_grpc.AddrInfo\x12\x15\n\rerror_message\x18\x03 \x01(\t\x12\x11\n\terror_num\x18\x04 \x01(\x05"\xd9\x01\n\x12GetNameInfoRequest\x12)\n\tstack_ref\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12)\n\x04addr\x18\x02 \x01(\x0b2\x1b.nixnetsocket_grpc.SockAddr\x12\x0f\n\x07hostlen\x18\x03 \x01(\x05\x12\x0f\n\x07servlen\x18\x04 \x01(\x05\x128\n\x0bflags_array\x18\x05 \x03(\x0e2#.nixnetsocket_grpc.GetNameInfoFlags\x12\x11\n\tflags_raw\x18\x06 \x01(\x05"k\n\x13GetNameInfoResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\x0c\n\x04serv\x18\x03 \x01(\t\x12\x15\n\rerror_message\x18\x04 \x01(\t\x12\x11\n\terror_num\x18\x05 \x01(\x05"<\n\x12GetPeerNameRequest\x12&\n\x06socket\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"z\n\x13GetPeerNameResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12)\n\x04addr\x18\x02 \x01(\x0b2\x1b.nixnetsocket_grpc.SockAddr\x12\x15\n\rerror_message\x18\x03 \x01(\t\x12\x11\n\terror_num\x18\x04 \x01(\x05"<\n\x12GetSockNameRequest\x12&\n\x06socket\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"z\n\x13GetSockNameResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12)\n\x04addr\x18\x02 \x01(\x0b2\x1b.nixnetsocket_grpc.SockAddr\x12\x15\n\rerror_message\x18\x03 \x01(\t\x12\x11\n\terror_num\x18\x04 \x01(\x05"\xeb\x01\n\x11GetSockOptRequest\x12&\n\x06socket\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x125\n\x05level\x18\x02 \x01(\x0e2$.nixnetsocket_grpc.SocketOptionLevelH\x00\x12\x13\n\tlevel_raw\x18\x03 \x01(\x05H\x00\x12-\n\x07optname\x18\x04 \x01(\x0e2\x1a.nixnetsocket_grpc.OptNameH\x01\x12\x15\n\x0boptname_raw\x18\x05 \x01(\x05H\x01B\x0c\n\nlevel_enumB\x0e\n\x0coptname_enum"~\n\x12GetSockOptResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12.\n\x06optval\x18\x02 \x01(\x0b2\x1e.nixnetsocket_grpc.SockOptData\x12\x15\n\rerror_message\x18\x03 \x01(\t\x12\x11\n\terror_num\x18\x04 \x01(\x05"H\n\x0fInetAddrRequest\x12)\n\tstack_ref\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\n\n\x02cp\x18\x02 \x01(\t"Z\n\x10InetAddrResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04addr\x18\x02 \x01(\r\x12\x15\n\rerror_message\x18\x03 \x01(\t\x12\x11\n\terror_num\x18\x04 \x01(\x05"H\n\x0fInetAToNRequest\x12)\n\tstack_ref\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\n\n\x02cp\x18\x02 \x01(\t"u\n\x10InetAToNResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\'\n\x04name\x18\x02 \x01(\x0b2\x19.nixnetsocket_grpc.InAddr\x12\x15\n\rerror_message\x18\x03 \x01(\t\x12\x11\n\terror_num\x18\x04 \x01(\x05"h\n\x0fInetNToARequest\x12)\n\tstack_ref\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12*\n\x07in_addr\x18\x02 \x01(\x0b2\x19.nixnetsocket_grpc.InAddr"]\n\x10InetNToAResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07address\x18\x02 \x01(\t\x12\x15\n\rerror_message\x18\x03 \x01(\t\x12\x11\n\terror_num\x18\x04 \x01(\x05"b\n\x0fInetNToPRequest\x12)\n\tstack_ref\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12$\n\x03src\x18\x02 \x01(\x0b2\x17.nixnetsocket_grpc.Addr"]\n\x10InetNToPResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07address\x18\x02 \x01(\t\x12\x15\n\rerror_message\x18\x03 \x01(\t\x12\x11\n\terror_num\x18\x04 \x01(\x05"\x96\x01\n\x0fInetPToNRequest\x12)\n\tstack_ref\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12.\n\x02af\x18\x02 \x01(\x0e2 .nixnetsocket_grpc.AddressFamilyH\x00\x12\x10\n\x06af_raw\x18\x03 \x01(\x05H\x00\x12\x0b\n\x03src\x18\x04 \x01(\tB\t\n\x07af_enum"r\n\x10InetPToNResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12$\n\x03dst\x18\x02 \x01(\x0b2\x17.nixnetsocket_grpc.Addr\x12\x15\n\rerror_message\x18\x03 \x01(\t\x12\x11\n\terror_num\x18\x04 \x01(\x05"@\n\x13IpStackClearRequest\x12)\n\tstack_ref\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"P\n\x14IpStackClearResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rerror_message\x18\x02 \x01(\t\x12\x11\n\terror_num\x18\x03 \x01(\x05"P\n\x14IpStackCreateRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12\x12\n\nstack_name\x18\x02 \x01(\t\x12\x0e\n\x06config\x18\x03 \x01(\t"|\n\x15IpStackCreateResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12)\n\tstack_ref\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rerror_message\x18\x03 \x01(\t\x12\x11\n\terror_num\x18\x04 \x01(\x05"\x86\x01\n!IpStackGetAllStacksInfoStrRequest\x12<\n\x06format\x18\x01 \x01(\x0e2*.nixnetsocket_grpc.IPStackInfoStringFormatH\x00\x12\x14\n\nformat_raw\x18\x02 \x01(\rH\x00B\r\n\x0bformat_enum"l\n"IpStackGetAllStacksInfoStrResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04info\x18\x02 \x01(\t\x12\x15\n\rerror_message\x18\x03 \x01(\t\x12\x11\n\terror_num\x18\x04 \x01(\x05"B\n\x15IpStackGetInfoRequest\x12)\n\tstack_ref\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\x93\x01\n\x16IpStackGetInfoResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12?\n\x12virtual_interfaces\x18\x02 \x03(\x0b2#.nixnetsocket_grpc.VirtualInterface\x12\x15\n\rerror_message\x18\x03 \x01(\t\x12\x11\n\terror_num\x18\x04 \x01(\x05">\n\x12IpStackOpenRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12\x12\n\nstack_name\x18\x02 \x01(\t"z\n\x13IpStackOpenResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12)\n\tstack_ref\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rerror_message\x18\x03 \x01(\t\x12\x11\n\terror_num\x18\x04 \x01(\x05"x\n\x1eIpStackWaitForInterfaceRequest\x12)\n\tstack_ref\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x17\n\x0flocal_interface\x18\x02 \x01(\t\x12\x12\n\ntimeout_ms\x18\x03 \x01(\x05"[\n\x1fIpStackWaitForInterfaceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rerror_message\x18\x02 \x01(\t\x12\x11\n\terror_num\x18\x03 \x01(\x05"H\n\rListenRequest\x12&\n\x06socket\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07backlog\x18\x02 \x01(\x05"J\n\x0eListenResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rerror_message\x18\x02 \x01(\t\x12\x11\n\terror_num\x18\x03 \x01(\x05"\x89\x01\n\x0bRecvRequest\x12&\n\x06socket\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0c\n\x04size\x18\x02 \x01(\x05\x121\n\x0bflags_array\x18\x03 \x03(\x0e2\x1c.nixnetsocket_grpc.RecvFlags\x12\x11\n\tflags_raw\x18\x04 \x01(\x05"U\n\x0cRecvResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0b\n\x03mem\x18\x02 \x01(\x0c\x12\x15\n\rerror_message\x18\x03 \x01(\t\x12\x11\n\terror_num\x18\x04 \x01(\x05"\x8d\x01\n\x0fRecvFromRequest\x12&\n\x06socket\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0c\n\x04size\x18\x02 \x01(\x05\x121\n\x0bflags_array\x18\x03 \x03(\x0e2\x1c.nixnetsocket_grpc.RecvFlags\x12\x11\n\tflags_raw\x18\x04 \x01(\x05"\x89\x01\n\x10RecvFromResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0b\n\x03mem\x18\x02 \x01(\x0c\x12.\n\tfrom_addr\x18\x03 \x01(\x0b2\x1b.nixnetsocket_grpc.SockAddr\x12\x15\n\rerror_message\x18\x04 \x01(\t\x12\x11\n\terror_num\x18\x05 \x01(\x05"\xb9\x01\n\rSelectRequest\x12\'\n\x07readfds\x18\x01 \x03(\x0b2\x16.nidevice_grpc.Session\x12(\n\x08writefds\x18\x02 \x03(\x0b2\x16.nidevice_grpc.Session\x12)\n\texceptfds\x18\x03 \x03(\x0b2\x16.nidevice_grpc.Session\x12*\n\x07timeout\x18\x04 \x01(\x0b2\x19.google.protobuf.Duration"J\n\x0eSelectResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rerror_message\x18\x02 \x01(\t\x12\x11\n\terror_num\x18\x03 \x01(\x05"Y\n\x0bSendRequest\x12&\n\x06socket\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07dataptr\x18\x02 \x01(\x0c\x12\x11\n\tflags_raw\x18\x03 \x01(\x05"H\n\x0cSendResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rerror_message\x18\x02 \x01(\t\x12\x11\n\terror_num\x18\x03 \x01(\x05"\x84\x01\n\rSendToRequest\x12&\n\x06socket\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07dataptr\x18\x02 \x01(\x0c\x12\x11\n\tflags_raw\x18\x03 \x01(\x05\x12\'\n\x02to\x18\x04 \x01(\x0b2\x1b.nixnetsocket_grpc.SockAddr"J\n\x0eSendToResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rerror_message\x18\x02 \x01(\t\x12\x11\n\terror_num\x18\x03 \x01(\x05"\x9d\x02\n\x11SetSockOptRequest\x12&\n\x06socket\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x125\n\x05level\x18\x02 \x01(\x0e2$.nixnetsocket_grpc.SocketOptionLevelH\x00\x12\x13\n\tlevel_raw\x18\x03 \x01(\x05H\x00\x12-\n\x07optname\x18\x04 \x01(\x0e2\x1a.nixnetsocket_grpc.OptNameH\x01\x12\x15\n\x0boptname_raw\x18\x05 \x01(\x05H\x01\x120\n\x08opt_data\x18\x06 \x01(\x0b2\x1e.nixnetsocket_grpc.SockOptDataB\x0c\n\nlevel_enumB\x0e\n\x0coptname_enum"N\n\x12SetSockOptResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rerror_message\x18\x02 \x01(\t\x12\x11\n\terror_num\x18\x03 \x01(\x05"\x84\x01\n\x0fShutdownRequest\x12&\n\x06socket\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12*\n\x03how\x18\x02 \x01(\x0e2\x1b.nixnetsocket_grpc.ShutdownH\x00\x12\x11\n\x07how_raw\x18\x03 \x01(\x05H\x00B\n\n\x08how_enum"L\n\x10ShutdownResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rerror_message\x18\x02 \x01(\t\x12\x11\n\terror_num\x18\x03 \x01(\x05"\xdd\x02\n\rSocketRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12)\n\tstack_ref\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session\x122\n\x06domain\x18\x03 \x01(\x0e2 .nixnetsocket_grpc.AddressFamilyH\x00\x12\x14\n\ndomain_raw\x18\x04 \x01(\x05H\x00\x125\n\x04type\x18\x05 \x01(\x0e2%.nixnetsocket_grpc.SocketProtocolTypeH\x01\x12\x12\n\x08type_raw\x18\x06 \x01(\x05H\x01\x121\n\x08protocol\x18\x07 \x01(\x0e2\x1d.nixnetsocket_grpc.IPProtocolH\x02\x12\x16\n\x0cprotocol_raw\x18\x08 \x01(\x05H\x02B\r\n\x0bdomain_enumB\x0b\n\ttype_enumB\x0f\n\rprotocol_enum"r\n\x0eSocketResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12&\n\x06socket\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rerror_message\x18\x03 \x01(\t\x12\x11\n\terror_num\x18\x04 \x01(\x05"1\n\x0eStrErrRRequest\x12\x0e\n\x06errnum\x18\x01 \x01(\x05\x12\x0f\n\x07buf_len\x18\x02 \x01(\x04"0\n\x0fStrErrRResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05error\x18\x02 \x01(\t*?\n\x15NiXnetSocketAttribute\x12&\n"NIXNETSOCKET_ATTRIBUTE_UNSPECIFIED\x10\x00*b\n\rAddressFamily\x12\x1e\n\x1aADDRESS_FAMILY_UNSPECIFIED\x10\x00\x12\x17\n\x13ADDRESS_FAMILY_INET\x10\x02\x12\x18\n\x14ADDRESS_FAMILY_INET6\x10\n*\xe7\x03\n\x10GetAddrInfoFlags\x12#\n\x1fGET_ADDR_INFO_FLAGS_UNSPECIFIED\x10\x00\x12\x1f\n\x1bGET_ADDR_INFO_FLAGS_PASSIVE\x10\x01\x12!\n\x1dGET_ADDR_INFO_FLAGS_CANONNAME\x10\x02\x12#\n\x1fGET_ADDR_INFO_FLAGS_NUMERICHOST\x10\x04\x12#\n\x1fGET_ADDR_INFO_FLAGS_NUMERICSERV\x10\x08\x12 \n\x1cGET_ADDR_INFO_FLAGS_V4MAPPED\x10\x10\x12\x1b\n\x17GET_ADDR_INFO_FLAGS_ALL\x10 \x12"\n\x1eGET_ADDR_INFO_FLAGS_ADDRCONFIG\x10@\x12#\n\x1eGET_ADDR_INFO_FLAGS_LOCALQUERY\x10\x80\x01\x12"\n\x1dGET_ADDR_INFO_FLAGS_PREFER_V4\x10\x80\x02\x12&\n!GET_ADDR_INFO_FLAGS_UNICAST_REPLY\x10\x80\x04\x12%\n GET_ADDR_INFO_FLAGS_SHARED_RRSET\x10\x80\x08\x12%\n GET_ADDR_INFO_FLAGS_BYPASS_CACHE\x10\x80\x10*\xe2\x01\n\x10GetNameInfoFlags\x12#\n\x1fGET_NAME_INFO_FLAGS_UNSPECIFIED\x10\x00\x12\x1e\n\x1aGET_NAME_INFO_FLAGS_NOFQDN\x10\x01\x12#\n\x1fGET_NAME_INFO_FLAGS_NUMERICHOST\x10\x02\x12 \n\x1cGET_NAME_INFO_FLAGS_NAMEREQD\x10\x04\x12#\n\x1fGET_NAME_INFO_FLAGS_NUMERICSERV\x10\x08\x12\x1d\n\x19GET_NAME_INFO_FLAGS_DGRAM\x10\x10*`\n\nIPProtocol\x12\x12\n\x0eIP_PROTOCOL_IP\x10\x00\x12\x13\n\x0fIP_PROTOCOL_TCP\x10\x06\x12\x13\n\x0fIP_PROTOCOL_UDP\x10\x08\x12\x14\n\x10IP_PROTOCOL_IPV6\x10\x0c*]\n\x17IPStackInfoStringFormat\x12 \n\x1cIPSTACK_INFO_STR_FORMAT_JSON\x10\x00\x12 \n\x1cIPSTACK_INFO_STR_FORMAT_TEXT\x10\x01*K\n\x11OperationalStatus\x12\x1b\n\x17OPERATIONAL_STATUS_DOWN\x10\x00\x12\x19\n\x15OPERATIONAL_STATUS_UP\x10\x01*\xef\x04\n\x07OptName\x12\x18\n\x14OPT_NAME_UNSPECIFIED\x10\x00\x12\x18\n\x14OPT_NAME_TCP_NODELAY\x10\x01\x12\x1e\n\x1aOPT_NAME_IP_ADD_MEMBERSHIP\x10\x03\x12\x1f\n\x1bOPT_NAME_IP_DROP_MEMBERSHIP\x10\x04\x12\x1c\n\x18OPT_NAME_IP_MULTICAST_IF\x10\x05\x12\x1d\n\x19OPT_NAME_IP_MULTICAST_TTL\x10\x06\x12\x1c\n\x18OPT_NAME_IPV6_JOIN_GROUP\x10\x0c\x12\x1d\n\x19OPT_NAME_IPV6_LEAVE_GROUP\x10\r\x12 \n\x1cOPT_NAME_IPV6_ADD_MEMBERSHIP\x10\x0c\x12!\n\x1dOPT_NAME_IPV6_DROP_MEMBERSHIP\x10\r\x12\x1e\n\x1aOPT_NAME_IPV6_MULTICAST_IF\x10\x0e\x12 \n\x1cOPT_NAME_IPV6_MULTICAST_HOPS\x10\x0f\x12\x18\n\x14OPT_NAME_IPV6_V6ONLY\x10\x10\x12\x17\n\x12OPT_NAME_SO_RXDATA\x10\x81\x02\x12\x17\n\x12OPT_NAME_SO_RCVBUF\x10\x82\x02\x12\x17\n\x12OPT_NAME_SO_SNDBUF\x10\x83\x02\x12\x19\n\x14OPT_NAME_SO_NONBLOCK\x10\x84\x02\x12\x1d\n\x18OPT_NAME_SO_BINDTODEVICE\x10\x85\x02\x12\x16\n\x11OPT_NAME_SO_ERROR\x10\x86\x02\x12\x17\n\x12OPT_NAME_SO_LINGER\x10\x87\x02\x12\x1a\n\x15OPT_NAME_SO_REUSEADDR\x10\x88\x02\x1a\x02\x10\x01*@\n\tRecvFlags\x12\x1a\n\x16RECV_FLAGS_UNSPECIFIED\x10\x00\x12\x17\n\x13RECV_FLAGS_MSG_PEEK\x10\x01*?\n\x08Shutdown\x12\x0f\n\x0bSHUTDOWN_RD\x10\x00\x12\x0f\n\x0bSHUTDOWN_WR\x10\x01\x12\x11\n\rSHUTDOWN_RDWR\x10\x02*X\n\x11SocketOptionLevel\x12#\n\x1fSOCKET_OPTION_LEVEL_UNSPECIFIED\x10\x00\x12\x1e\n\x1aSOCKET_OPTION_LEVEL_SOCKET\x10\r*{\n\x12SocketProtocolType\x12$\n SOCKET_PROTOCOL_TYPE_UNSPECIFIED\x10\x00\x12\x1f\n\x1bSOCKET_PROTOCOL_TYPE_STREAM\x10\x01\x12\x1e\n\x1aSOCKET_PROTOCOL_TYPE_DGRAM\x10\x022\xd0\x15\n\x0cNiXnetSocket\x12M\n\x06Accept\x12 .nixnetsocket_grpc.AcceptRequest\x1a!.nixnetsocket_grpc.AcceptResponse\x12G\n\x04Bind\x12\x1e.nixnetsocket_grpc.BindRequest\x1a\x1f.nixnetsocket_grpc.BindResponse\x12J\n\x05Close\x12\x1f.nixnetsocket_grpc.CloseRequest\x1a .nixnetsocket_grpc.CloseResponse\x12P\n\x07Connect\x12!.nixnetsocket_grpc.ConnectRequest\x1a".nixnetsocket_grpc.ConnectResponse\x12P\n\x07FdIsSet\x12!.nixnetsocket_grpc.FdIsSetRequest\x1a".nixnetsocket_grpc.FdIsSetResponse\x12\\\n\x0bGetAddrInfo\x12%.nixnetsocket_grpc.GetAddrInfoRequest\x1a&.nixnetsocket_grpc.GetAddrInfoResponse\x12\\\n\x0bGetNameInfo\x12%.nixnetsocket_grpc.GetNameInfoRequest\x1a&.nixnetsocket_grpc.GetNameInfoResponse\x12\\\n\x0bGetPeerName\x12%.nixnetsocket_grpc.GetPeerNameRequest\x1a&.nixnetsocket_grpc.GetPeerNameResponse\x12\\\n\x0bGetSockName\x12%.nixnetsocket_grpc.GetSockNameRequest\x1a&.nixnetsocket_grpc.GetSockNameResponse\x12Y\n\nGetSockOpt\x12$.nixnetsocket_grpc.GetSockOptRequest\x1a%.nixnetsocket_grpc.GetSockOptResponse\x12S\n\x08InetAddr\x12".nixnetsocket_grpc.InetAddrRequest\x1a#.nixnetsocket_grpc.InetAddrResponse\x12S\n\x08InetAToN\x12".nixnetsocket_grpc.InetAToNRequest\x1a#.nixnetsocket_grpc.InetAToNResponse\x12S\n\x08InetNToA\x12".nixnetsocket_grpc.InetNToARequest\x1a#.nixnetsocket_grpc.InetNToAResponse\x12S\n\x08InetNToP\x12".nixnetsocket_grpc.InetNToPRequest\x1a#.nixnetsocket_grpc.InetNToPResponse\x12S\n\x08InetPToN\x12".nixnetsocket_grpc.InetPToNRequest\x1a#.nixnetsocket_grpc.InetPToNResponse\x12_\n\x0cIpStackClear\x12&.nixnetsocket_grpc.IpStackClearRequest\x1a\'.nixnetsocket_grpc.IpStackClearResponse\x12b\n\rIpStackCreate\x12\'.nixnetsocket_grpc.IpStackCreateRequest\x1a(.nixnetsocket_grpc.IpStackCreateResponse\x12\x89\x01\n\x1aIpStackGetAllStacksInfoStr\x124.nixnetsocket_grpc.IpStackGetAllStacksInfoStrRequest\x1a5.nixnetsocket_grpc.IpStackGetAllStacksInfoStrResponse\x12e\n\x0eIpStackGetInfo\x12(.nixnetsocket_grpc.IpStackGetInfoRequest\x1a).nixnetsocket_grpc.IpStackGetInfoResponse\x12\\\n\x0bIpStackOpen\x12%.nixnetsocket_grpc.IpStackOpenRequest\x1a&.nixnetsocket_grpc.IpStackOpenResponse\x12\x80\x01\n\x17IpStackWaitForInterface\x121.nixnetsocket_grpc.IpStackWaitForInterfaceRequest\x1a2.nixnetsocket_grpc.IpStackWaitForInterfaceResponse\x12M\n\x06Listen\x12 .nixnetsocket_grpc.ListenRequest\x1a!.nixnetsocket_grpc.ListenResponse\x12G\n\x04Recv\x12\x1e.nixnetsocket_grpc.RecvRequest\x1a\x1f.nixnetsocket_grpc.RecvResponse\x12S\n\x08RecvFrom\x12".nixnetsocket_grpc.RecvFromRequest\x1a#.nixnetsocket_grpc.RecvFromResponse\x12M\n\x06Select\x12 .nixnetsocket_grpc.SelectRequest\x1a!.nixnetsocket_grpc.SelectResponse\x12G\n\x04Send\x12\x1e.nixnetsocket_grpc.SendRequest\x1a\x1f.nixnetsocket_grpc.SendResponse\x12M\n\x06SendTo\x12 .nixnetsocket_grpc.SendToRequest\x1a!.nixnetsocket_grpc.SendToResponse\x12Y\n\nSetSockOpt\x12$.nixnetsocket_grpc.SetSockOptRequest\x1a%.nixnetsocket_grpc.SetSockOptResponse\x12S\n\x08Shutdown\x12".nixnetsocket_grpc.ShutdownRequest\x1a#.nixnetsocket_grpc.ShutdownResponse\x12M\n\x06Socket\x12 .nixnetsocket_grpc.SocketRequest\x1a!.nixnetsocket_grpc.SocketResponse\x12P\n\x07StrErrR\x12!.nixnetsocket_grpc.StrErrRRequest\x1a".nixnetsocket_grpc.StrErrRResponseBP\n\x16com.ni.grpc.xnetsocketB\x0cNiXnetSocketP\x01\xaa\x02%NationalInstruments.Grpc.NiXnetSocketb\x06proto3')
_NIXNETSOCKETATTRIBUTE = DESCRIPTOR.enum_types_by_name['NiXnetSocketAttribute']
NiXnetSocketAttribute = enum_type_wrapper.EnumTypeWrapper(_NIXNETSOCKETATTRIBUTE)
_ADDRESSFAMILY = DESCRIPTOR.enum_types_by_name['AddressFamily']
AddressFamily = enum_type_wrapper.EnumTypeWrapper(_ADDRESSFAMILY)
_GETADDRINFOFLAGS = DESCRIPTOR.enum_types_by_name['GetAddrInfoFlags']
GetAddrInfoFlags = enum_type_wrapper.EnumTypeWrapper(_GETADDRINFOFLAGS)
_GETNAMEINFOFLAGS = DESCRIPTOR.enum_types_by_name['GetNameInfoFlags']
GetNameInfoFlags = enum_type_wrapper.EnumTypeWrapper(_GETNAMEINFOFLAGS)
_IPPROTOCOL = DESCRIPTOR.enum_types_by_name['IPProtocol']
IPProtocol = enum_type_wrapper.EnumTypeWrapper(_IPPROTOCOL)
_IPSTACKINFOSTRINGFORMAT = DESCRIPTOR.enum_types_by_name['IPStackInfoStringFormat']
IPStackInfoStringFormat = enum_type_wrapper.EnumTypeWrapper(_IPSTACKINFOSTRINGFORMAT)
_OPERATIONALSTATUS = DESCRIPTOR.enum_types_by_name['OperationalStatus']
OperationalStatus = enum_type_wrapper.EnumTypeWrapper(_OPERATIONALSTATUS)
_OPTNAME = DESCRIPTOR.enum_types_by_name['OptName']
OptName = enum_type_wrapper.EnumTypeWrapper(_OPTNAME)
_RECVFLAGS = DESCRIPTOR.enum_types_by_name['RecvFlags']
RecvFlags = enum_type_wrapper.EnumTypeWrapper(_RECVFLAGS)
_SHUTDOWN = DESCRIPTOR.enum_types_by_name['Shutdown']
Shutdown = enum_type_wrapper.EnumTypeWrapper(_SHUTDOWN)
_SOCKETOPTIONLEVEL = DESCRIPTOR.enum_types_by_name['SocketOptionLevel']
SocketOptionLevel = enum_type_wrapper.EnumTypeWrapper(_SOCKETOPTIONLEVEL)
_SOCKETPROTOCOLTYPE = DESCRIPTOR.enum_types_by_name['SocketProtocolType']
SocketProtocolType = enum_type_wrapper.EnumTypeWrapper(_SOCKETPROTOCOLTYPE)
NIXNETSOCKET_ATTRIBUTE_UNSPECIFIED = 0
ADDRESS_FAMILY_UNSPECIFIED = 0
ADDRESS_FAMILY_INET = 2
ADDRESS_FAMILY_INET6 = 10
GET_ADDR_INFO_FLAGS_UNSPECIFIED = 0
GET_ADDR_INFO_FLAGS_PASSIVE = 1
GET_ADDR_INFO_FLAGS_CANONNAME = 2
GET_ADDR_INFO_FLAGS_NUMERICHOST = 4
GET_ADDR_INFO_FLAGS_NUMERICSERV = 8
GET_ADDR_INFO_FLAGS_V4MAPPED = 16
GET_ADDR_INFO_FLAGS_ALL = 32
GET_ADDR_INFO_FLAGS_ADDRCONFIG = 64
GET_ADDR_INFO_FLAGS_LOCALQUERY = 128
GET_ADDR_INFO_FLAGS_PREFER_V4 = 256
GET_ADDR_INFO_FLAGS_UNICAST_REPLY = 512
GET_ADDR_INFO_FLAGS_SHARED_RRSET = 1024
GET_ADDR_INFO_FLAGS_BYPASS_CACHE = 2048
GET_NAME_INFO_FLAGS_UNSPECIFIED = 0
GET_NAME_INFO_FLAGS_NOFQDN = 1
GET_NAME_INFO_FLAGS_NUMERICHOST = 2
GET_NAME_INFO_FLAGS_NAMEREQD = 4
GET_NAME_INFO_FLAGS_NUMERICSERV = 8
GET_NAME_INFO_FLAGS_DGRAM = 16
IP_PROTOCOL_IP = 0
IP_PROTOCOL_TCP = 6
IP_PROTOCOL_UDP = 8
IP_PROTOCOL_IPV6 = 12
IPSTACK_INFO_STR_FORMAT_JSON = 0
IPSTACK_INFO_STR_FORMAT_TEXT = 1
OPERATIONAL_STATUS_DOWN = 0
OPERATIONAL_STATUS_UP = 1
OPT_NAME_UNSPECIFIED = 0
OPT_NAME_TCP_NODELAY = 1
OPT_NAME_IP_ADD_MEMBERSHIP = 3
OPT_NAME_IP_DROP_MEMBERSHIP = 4
OPT_NAME_IP_MULTICAST_IF = 5
OPT_NAME_IP_MULTICAST_TTL = 6
OPT_NAME_IPV6_JOIN_GROUP = 12
OPT_NAME_IPV6_LEAVE_GROUP = 13
OPT_NAME_IPV6_ADD_MEMBERSHIP = 12
OPT_NAME_IPV6_DROP_MEMBERSHIP = 13
OPT_NAME_IPV6_MULTICAST_IF = 14
OPT_NAME_IPV6_MULTICAST_HOPS = 15
OPT_NAME_IPV6_V6ONLY = 16
OPT_NAME_SO_RXDATA = 257
OPT_NAME_SO_RCVBUF = 258
OPT_NAME_SO_SNDBUF = 259
OPT_NAME_SO_NONBLOCK = 260
OPT_NAME_SO_BINDTODEVICE = 261
OPT_NAME_SO_ERROR = 262
OPT_NAME_SO_LINGER = 263
OPT_NAME_SO_REUSEADDR = 264
RECV_FLAGS_UNSPECIFIED = 0
RECV_FLAGS_MSG_PEEK = 1
SHUTDOWN_RD = 0
SHUTDOWN_WR = 1
SHUTDOWN_RDWR = 2
SOCKET_OPTION_LEVEL_UNSPECIFIED = 0
SOCKET_OPTION_LEVEL_SOCKET = 13
SOCKET_PROTOCOL_TYPE_UNSPECIFIED = 0
SOCKET_PROTOCOL_TYPE_STREAM = 1
SOCKET_PROTOCOL_TYPE_DGRAM = 2
_IPADDRESS = DESCRIPTOR.message_types_by_name['IPAddress']
_GATEWAYADDRESS = DESCRIPTOR.message_types_by_name['GatewayAddress']
_VIRTUALINTERFACE = DESCRIPTOR.message_types_by_name['VirtualInterface']
_IN6ADDR = DESCRIPTOR.message_types_by_name['In6Addr']
_INADDR = DESCRIPTOR.message_types_by_name['InAddr']
_ADDR = DESCRIPTOR.message_types_by_name['Addr']
_SOCKADDRIN = DESCRIPTOR.message_types_by_name['SockAddrIn']
_SOCKADDRIN6 = DESCRIPTOR.message_types_by_name['SockAddrIn6']
_SOCKADDR = DESCRIPTOR.message_types_by_name['SockAddr']
_ADDRINFO = DESCRIPTOR.message_types_by_name['AddrInfo']
_ADDRINFOHINT = DESCRIPTOR.message_types_by_name['AddrInfoHint']
_LINGER = DESCRIPTOR.message_types_by_name['Linger']
_IPMREQ = DESCRIPTOR.message_types_by_name['IPMReq']
_IPV6MREQ = DESCRIPTOR.message_types_by_name['IPv6MReq']
_SOCKOPTDATA = DESCRIPTOR.message_types_by_name['SockOptData']
_ACCEPTREQUEST = DESCRIPTOR.message_types_by_name['AcceptRequest']
_ACCEPTRESPONSE = DESCRIPTOR.message_types_by_name['AcceptResponse']
_BINDREQUEST = DESCRIPTOR.message_types_by_name['BindRequest']
_BINDRESPONSE = DESCRIPTOR.message_types_by_name['BindResponse']
_CLOSEREQUEST = DESCRIPTOR.message_types_by_name['CloseRequest']
_CLOSERESPONSE = DESCRIPTOR.message_types_by_name['CloseResponse']
_CONNECTREQUEST = DESCRIPTOR.message_types_by_name['ConnectRequest']
_CONNECTRESPONSE = DESCRIPTOR.message_types_by_name['ConnectResponse']
_FDISSETREQUEST = DESCRIPTOR.message_types_by_name['FdIsSetRequest']
_FDISSETRESPONSE = DESCRIPTOR.message_types_by_name['FdIsSetResponse']
_GETADDRINFOREQUEST = DESCRIPTOR.message_types_by_name['GetAddrInfoRequest']
_GETADDRINFORESPONSE = DESCRIPTOR.message_types_by_name['GetAddrInfoResponse']
_GETNAMEINFOREQUEST = DESCRIPTOR.message_types_by_name['GetNameInfoRequest']
_GETNAMEINFORESPONSE = DESCRIPTOR.message_types_by_name['GetNameInfoResponse']
_GETPEERNAMEREQUEST = DESCRIPTOR.message_types_by_name['GetPeerNameRequest']
_GETPEERNAMERESPONSE = DESCRIPTOR.message_types_by_name['GetPeerNameResponse']
_GETSOCKNAMEREQUEST = DESCRIPTOR.message_types_by_name['GetSockNameRequest']
_GETSOCKNAMERESPONSE = DESCRIPTOR.message_types_by_name['GetSockNameResponse']
_GETSOCKOPTREQUEST = DESCRIPTOR.message_types_by_name['GetSockOptRequest']
_GETSOCKOPTRESPONSE = DESCRIPTOR.message_types_by_name['GetSockOptResponse']
_INETADDRREQUEST = DESCRIPTOR.message_types_by_name['InetAddrRequest']
_INETADDRRESPONSE = DESCRIPTOR.message_types_by_name['InetAddrResponse']
_INETATONREQUEST = DESCRIPTOR.message_types_by_name['InetAToNRequest']
_INETATONRESPONSE = DESCRIPTOR.message_types_by_name['InetAToNResponse']
_INETNTOAREQUEST = DESCRIPTOR.message_types_by_name['InetNToARequest']
_INETNTOARESPONSE = DESCRIPTOR.message_types_by_name['InetNToAResponse']
_INETNTOPREQUEST = DESCRIPTOR.message_types_by_name['InetNToPRequest']
_INETNTOPRESPONSE = DESCRIPTOR.message_types_by_name['InetNToPResponse']
_INETPTONREQUEST = DESCRIPTOR.message_types_by_name['InetPToNRequest']
_INETPTONRESPONSE = DESCRIPTOR.message_types_by_name['InetPToNResponse']
_IPSTACKCLEARREQUEST = DESCRIPTOR.message_types_by_name['IpStackClearRequest']
_IPSTACKCLEARRESPONSE = DESCRIPTOR.message_types_by_name['IpStackClearResponse']
_IPSTACKCREATEREQUEST = DESCRIPTOR.message_types_by_name['IpStackCreateRequest']
_IPSTACKCREATERESPONSE = DESCRIPTOR.message_types_by_name['IpStackCreateResponse']
_IPSTACKGETALLSTACKSINFOSTRREQUEST = DESCRIPTOR.message_types_by_name['IpStackGetAllStacksInfoStrRequest']
_IPSTACKGETALLSTACKSINFOSTRRESPONSE = DESCRIPTOR.message_types_by_name['IpStackGetAllStacksInfoStrResponse']
_IPSTACKGETINFOREQUEST = DESCRIPTOR.message_types_by_name['IpStackGetInfoRequest']
_IPSTACKGETINFORESPONSE = DESCRIPTOR.message_types_by_name['IpStackGetInfoResponse']
_IPSTACKOPENREQUEST = DESCRIPTOR.message_types_by_name['IpStackOpenRequest']
_IPSTACKOPENRESPONSE = DESCRIPTOR.message_types_by_name['IpStackOpenResponse']
_IPSTACKWAITFORINTERFACEREQUEST = DESCRIPTOR.message_types_by_name['IpStackWaitForInterfaceRequest']
_IPSTACKWAITFORINTERFACERESPONSE = DESCRIPTOR.message_types_by_name['IpStackWaitForInterfaceResponse']
_LISTENREQUEST = DESCRIPTOR.message_types_by_name['ListenRequest']
_LISTENRESPONSE = DESCRIPTOR.message_types_by_name['ListenResponse']
_RECVREQUEST = DESCRIPTOR.message_types_by_name['RecvRequest']
_RECVRESPONSE = DESCRIPTOR.message_types_by_name['RecvResponse']
_RECVFROMREQUEST = DESCRIPTOR.message_types_by_name['RecvFromRequest']
_RECVFROMRESPONSE = DESCRIPTOR.message_types_by_name['RecvFromResponse']
_SELECTREQUEST = DESCRIPTOR.message_types_by_name['SelectRequest']
_SELECTRESPONSE = DESCRIPTOR.message_types_by_name['SelectResponse']
_SENDREQUEST = DESCRIPTOR.message_types_by_name['SendRequest']
_SENDRESPONSE = DESCRIPTOR.message_types_by_name['SendResponse']
_SENDTOREQUEST = DESCRIPTOR.message_types_by_name['SendToRequest']
_SENDTORESPONSE = DESCRIPTOR.message_types_by_name['SendToResponse']
_SETSOCKOPTREQUEST = DESCRIPTOR.message_types_by_name['SetSockOptRequest']
_SETSOCKOPTRESPONSE = DESCRIPTOR.message_types_by_name['SetSockOptResponse']
_SHUTDOWNREQUEST = DESCRIPTOR.message_types_by_name['ShutdownRequest']
_SHUTDOWNRESPONSE = DESCRIPTOR.message_types_by_name['ShutdownResponse']
_SOCKETREQUEST = DESCRIPTOR.message_types_by_name['SocketRequest']
_SOCKETRESPONSE = DESCRIPTOR.message_types_by_name['SocketResponse']
_STRERRRREQUEST = DESCRIPTOR.message_types_by_name['StrErrRRequest']
_STRERRRRESPONSE = DESCRIPTOR.message_types_by_name['StrErrRResponse']
IPAddress = _reflection.GeneratedProtocolMessageType('IPAddress', (_message.Message,), {'DESCRIPTOR': _IPADDRESS, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(IPAddress)
GatewayAddress = _reflection.GeneratedProtocolMessageType('GatewayAddress', (_message.Message,), {'DESCRIPTOR': _GATEWAYADDRESS, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(GatewayAddress)
VirtualInterface = _reflection.GeneratedProtocolMessageType('VirtualInterface', (_message.Message,), {'DESCRIPTOR': _VIRTUALINTERFACE, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(VirtualInterface)
In6Addr = _reflection.GeneratedProtocolMessageType('In6Addr', (_message.Message,), {'DESCRIPTOR': _IN6ADDR, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(In6Addr)
InAddr = _reflection.GeneratedProtocolMessageType('InAddr', (_message.Message,), {'DESCRIPTOR': _INADDR, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(InAddr)
Addr = _reflection.GeneratedProtocolMessageType('Addr', (_message.Message,), {'DESCRIPTOR': _ADDR, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(Addr)
SockAddrIn = _reflection.GeneratedProtocolMessageType('SockAddrIn', (_message.Message,), {'DESCRIPTOR': _SOCKADDRIN, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(SockAddrIn)
SockAddrIn6 = _reflection.GeneratedProtocolMessageType('SockAddrIn6', (_message.Message,), {'DESCRIPTOR': _SOCKADDRIN6, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(SockAddrIn6)
SockAddr = _reflection.GeneratedProtocolMessageType('SockAddr', (_message.Message,), {'DESCRIPTOR': _SOCKADDR, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(SockAddr)
AddrInfo = _reflection.GeneratedProtocolMessageType('AddrInfo', (_message.Message,), {'DESCRIPTOR': _ADDRINFO, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(AddrInfo)
AddrInfoHint = _reflection.GeneratedProtocolMessageType('AddrInfoHint', (_message.Message,), {'DESCRIPTOR': _ADDRINFOHINT, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(AddrInfoHint)
Linger = _reflection.GeneratedProtocolMessageType('Linger', (_message.Message,), {'DESCRIPTOR': _LINGER, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(Linger)
IPMReq = _reflection.GeneratedProtocolMessageType('IPMReq', (_message.Message,), {'DESCRIPTOR': _IPMREQ, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(IPMReq)
IPv6MReq = _reflection.GeneratedProtocolMessageType('IPv6MReq', (_message.Message,), {'DESCRIPTOR': _IPV6MREQ, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(IPv6MReq)
SockOptData = _reflection.GeneratedProtocolMessageType('SockOptData', (_message.Message,), {'DESCRIPTOR': _SOCKOPTDATA, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(SockOptData)
AcceptRequest = _reflection.GeneratedProtocolMessageType('AcceptRequest', (_message.Message,), {'DESCRIPTOR': _ACCEPTREQUEST, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(AcceptRequest)
AcceptResponse = _reflection.GeneratedProtocolMessageType('AcceptResponse', (_message.Message,), {'DESCRIPTOR': _ACCEPTRESPONSE, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(AcceptResponse)
BindRequest = _reflection.GeneratedProtocolMessageType('BindRequest', (_message.Message,), {'DESCRIPTOR': _BINDREQUEST, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(BindRequest)
BindResponse = _reflection.GeneratedProtocolMessageType('BindResponse', (_message.Message,), {'DESCRIPTOR': _BINDRESPONSE, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(BindResponse)
CloseRequest = _reflection.GeneratedProtocolMessageType('CloseRequest', (_message.Message,), {'DESCRIPTOR': _CLOSEREQUEST, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(CloseRequest)
CloseResponse = _reflection.GeneratedProtocolMessageType('CloseResponse', (_message.Message,), {'DESCRIPTOR': _CLOSERESPONSE, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(CloseResponse)
ConnectRequest = _reflection.GeneratedProtocolMessageType('ConnectRequest', (_message.Message,), {'DESCRIPTOR': _CONNECTREQUEST, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(ConnectRequest)
ConnectResponse = _reflection.GeneratedProtocolMessageType('ConnectResponse', (_message.Message,), {'DESCRIPTOR': _CONNECTRESPONSE, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(ConnectResponse)
FdIsSetRequest = _reflection.GeneratedProtocolMessageType('FdIsSetRequest', (_message.Message,), {'DESCRIPTOR': _FDISSETREQUEST, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(FdIsSetRequest)
FdIsSetResponse = _reflection.GeneratedProtocolMessageType('FdIsSetResponse', (_message.Message,), {'DESCRIPTOR': _FDISSETRESPONSE, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(FdIsSetResponse)
GetAddrInfoRequest = _reflection.GeneratedProtocolMessageType('GetAddrInfoRequest', (_message.Message,), {'DESCRIPTOR': _GETADDRINFOREQUEST, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(GetAddrInfoRequest)
GetAddrInfoResponse = _reflection.GeneratedProtocolMessageType('GetAddrInfoResponse', (_message.Message,), {'DESCRIPTOR': _GETADDRINFORESPONSE, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(GetAddrInfoResponse)
GetNameInfoRequest = _reflection.GeneratedProtocolMessageType('GetNameInfoRequest', (_message.Message,), {'DESCRIPTOR': _GETNAMEINFOREQUEST, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(GetNameInfoRequest)
GetNameInfoResponse = _reflection.GeneratedProtocolMessageType('GetNameInfoResponse', (_message.Message,), {'DESCRIPTOR': _GETNAMEINFORESPONSE, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(GetNameInfoResponse)
GetPeerNameRequest = _reflection.GeneratedProtocolMessageType('GetPeerNameRequest', (_message.Message,), {'DESCRIPTOR': _GETPEERNAMEREQUEST, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(GetPeerNameRequest)
GetPeerNameResponse = _reflection.GeneratedProtocolMessageType('GetPeerNameResponse', (_message.Message,), {'DESCRIPTOR': _GETPEERNAMERESPONSE, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(GetPeerNameResponse)
GetSockNameRequest = _reflection.GeneratedProtocolMessageType('GetSockNameRequest', (_message.Message,), {'DESCRIPTOR': _GETSOCKNAMEREQUEST, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(GetSockNameRequest)
GetSockNameResponse = _reflection.GeneratedProtocolMessageType('GetSockNameResponse', (_message.Message,), {'DESCRIPTOR': _GETSOCKNAMERESPONSE, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(GetSockNameResponse)
GetSockOptRequest = _reflection.GeneratedProtocolMessageType('GetSockOptRequest', (_message.Message,), {'DESCRIPTOR': _GETSOCKOPTREQUEST, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(GetSockOptRequest)
GetSockOptResponse = _reflection.GeneratedProtocolMessageType('GetSockOptResponse', (_message.Message,), {'DESCRIPTOR': _GETSOCKOPTRESPONSE, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(GetSockOptResponse)
InetAddrRequest = _reflection.GeneratedProtocolMessageType('InetAddrRequest', (_message.Message,), {'DESCRIPTOR': _INETADDRREQUEST, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(InetAddrRequest)
InetAddrResponse = _reflection.GeneratedProtocolMessageType('InetAddrResponse', (_message.Message,), {'DESCRIPTOR': _INETADDRRESPONSE, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(InetAddrResponse)
InetAToNRequest = _reflection.GeneratedProtocolMessageType('InetAToNRequest', (_message.Message,), {'DESCRIPTOR': _INETATONREQUEST, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(InetAToNRequest)
InetAToNResponse = _reflection.GeneratedProtocolMessageType('InetAToNResponse', (_message.Message,), {'DESCRIPTOR': _INETATONRESPONSE, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(InetAToNResponse)
InetNToARequest = _reflection.GeneratedProtocolMessageType('InetNToARequest', (_message.Message,), {'DESCRIPTOR': _INETNTOAREQUEST, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(InetNToARequest)
InetNToAResponse = _reflection.GeneratedProtocolMessageType('InetNToAResponse', (_message.Message,), {'DESCRIPTOR': _INETNTOARESPONSE, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(InetNToAResponse)
InetNToPRequest = _reflection.GeneratedProtocolMessageType('InetNToPRequest', (_message.Message,), {'DESCRIPTOR': _INETNTOPREQUEST, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(InetNToPRequest)
InetNToPResponse = _reflection.GeneratedProtocolMessageType('InetNToPResponse', (_message.Message,), {'DESCRIPTOR': _INETNTOPRESPONSE, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(InetNToPResponse)
InetPToNRequest = _reflection.GeneratedProtocolMessageType('InetPToNRequest', (_message.Message,), {'DESCRIPTOR': _INETPTONREQUEST, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(InetPToNRequest)
InetPToNResponse = _reflection.GeneratedProtocolMessageType('InetPToNResponse', (_message.Message,), {'DESCRIPTOR': _INETPTONRESPONSE, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(InetPToNResponse)
IpStackClearRequest = _reflection.GeneratedProtocolMessageType('IpStackClearRequest', (_message.Message,), {'DESCRIPTOR': _IPSTACKCLEARREQUEST, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(IpStackClearRequest)
IpStackClearResponse = _reflection.GeneratedProtocolMessageType('IpStackClearResponse', (_message.Message,), {'DESCRIPTOR': _IPSTACKCLEARRESPONSE, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(IpStackClearResponse)
IpStackCreateRequest = _reflection.GeneratedProtocolMessageType('IpStackCreateRequest', (_message.Message,), {'DESCRIPTOR': _IPSTACKCREATEREQUEST, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(IpStackCreateRequest)
IpStackCreateResponse = _reflection.GeneratedProtocolMessageType('IpStackCreateResponse', (_message.Message,), {'DESCRIPTOR': _IPSTACKCREATERESPONSE, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(IpStackCreateResponse)
IpStackGetAllStacksInfoStrRequest = _reflection.GeneratedProtocolMessageType('IpStackGetAllStacksInfoStrRequest', (_message.Message,), {'DESCRIPTOR': _IPSTACKGETALLSTACKSINFOSTRREQUEST, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(IpStackGetAllStacksInfoStrRequest)
IpStackGetAllStacksInfoStrResponse = _reflection.GeneratedProtocolMessageType('IpStackGetAllStacksInfoStrResponse', (_message.Message,), {'DESCRIPTOR': _IPSTACKGETALLSTACKSINFOSTRRESPONSE, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(IpStackGetAllStacksInfoStrResponse)
IpStackGetInfoRequest = _reflection.GeneratedProtocolMessageType('IpStackGetInfoRequest', (_message.Message,), {'DESCRIPTOR': _IPSTACKGETINFOREQUEST, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(IpStackGetInfoRequest)
IpStackGetInfoResponse = _reflection.GeneratedProtocolMessageType('IpStackGetInfoResponse', (_message.Message,), {'DESCRIPTOR': _IPSTACKGETINFORESPONSE, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(IpStackGetInfoResponse)
IpStackOpenRequest = _reflection.GeneratedProtocolMessageType('IpStackOpenRequest', (_message.Message,), {'DESCRIPTOR': _IPSTACKOPENREQUEST, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(IpStackOpenRequest)
IpStackOpenResponse = _reflection.GeneratedProtocolMessageType('IpStackOpenResponse', (_message.Message,), {'DESCRIPTOR': _IPSTACKOPENRESPONSE, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(IpStackOpenResponse)
IpStackWaitForInterfaceRequest = _reflection.GeneratedProtocolMessageType('IpStackWaitForInterfaceRequest', (_message.Message,), {'DESCRIPTOR': _IPSTACKWAITFORINTERFACEREQUEST, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(IpStackWaitForInterfaceRequest)
IpStackWaitForInterfaceResponse = _reflection.GeneratedProtocolMessageType('IpStackWaitForInterfaceResponse', (_message.Message,), {'DESCRIPTOR': _IPSTACKWAITFORINTERFACERESPONSE, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(IpStackWaitForInterfaceResponse)
ListenRequest = _reflection.GeneratedProtocolMessageType('ListenRequest', (_message.Message,), {'DESCRIPTOR': _LISTENREQUEST, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(ListenRequest)
ListenResponse = _reflection.GeneratedProtocolMessageType('ListenResponse', (_message.Message,), {'DESCRIPTOR': _LISTENRESPONSE, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(ListenResponse)
RecvRequest = _reflection.GeneratedProtocolMessageType('RecvRequest', (_message.Message,), {'DESCRIPTOR': _RECVREQUEST, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(RecvRequest)
RecvResponse = _reflection.GeneratedProtocolMessageType('RecvResponse', (_message.Message,), {'DESCRIPTOR': _RECVRESPONSE, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(RecvResponse)
RecvFromRequest = _reflection.GeneratedProtocolMessageType('RecvFromRequest', (_message.Message,), {'DESCRIPTOR': _RECVFROMREQUEST, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(RecvFromRequest)
RecvFromResponse = _reflection.GeneratedProtocolMessageType('RecvFromResponse', (_message.Message,), {'DESCRIPTOR': _RECVFROMRESPONSE, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(RecvFromResponse)
SelectRequest = _reflection.GeneratedProtocolMessageType('SelectRequest', (_message.Message,), {'DESCRIPTOR': _SELECTREQUEST, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(SelectRequest)
SelectResponse = _reflection.GeneratedProtocolMessageType('SelectResponse', (_message.Message,), {'DESCRIPTOR': _SELECTRESPONSE, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(SelectResponse)
SendRequest = _reflection.GeneratedProtocolMessageType('SendRequest', (_message.Message,), {'DESCRIPTOR': _SENDREQUEST, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(SendRequest)
SendResponse = _reflection.GeneratedProtocolMessageType('SendResponse', (_message.Message,), {'DESCRIPTOR': _SENDRESPONSE, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(SendResponse)
SendToRequest = _reflection.GeneratedProtocolMessageType('SendToRequest', (_message.Message,), {'DESCRIPTOR': _SENDTOREQUEST, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(SendToRequest)
SendToResponse = _reflection.GeneratedProtocolMessageType('SendToResponse', (_message.Message,), {'DESCRIPTOR': _SENDTORESPONSE, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(SendToResponse)
SetSockOptRequest = _reflection.GeneratedProtocolMessageType('SetSockOptRequest', (_message.Message,), {'DESCRIPTOR': _SETSOCKOPTREQUEST, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(SetSockOptRequest)
SetSockOptResponse = _reflection.GeneratedProtocolMessageType('SetSockOptResponse', (_message.Message,), {'DESCRIPTOR': _SETSOCKOPTRESPONSE, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(SetSockOptResponse)
ShutdownRequest = _reflection.GeneratedProtocolMessageType('ShutdownRequest', (_message.Message,), {'DESCRIPTOR': _SHUTDOWNREQUEST, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(ShutdownRequest)
ShutdownResponse = _reflection.GeneratedProtocolMessageType('ShutdownResponse', (_message.Message,), {'DESCRIPTOR': _SHUTDOWNRESPONSE, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(ShutdownResponse)
SocketRequest = _reflection.GeneratedProtocolMessageType('SocketRequest', (_message.Message,), {'DESCRIPTOR': _SOCKETREQUEST, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(SocketRequest)
SocketResponse = _reflection.GeneratedProtocolMessageType('SocketResponse', (_message.Message,), {'DESCRIPTOR': _SOCKETRESPONSE, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(SocketResponse)
StrErrRRequest = _reflection.GeneratedProtocolMessageType('StrErrRRequest', (_message.Message,), {'DESCRIPTOR': _STRERRRREQUEST, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(StrErrRRequest)
StrErrRResponse = _reflection.GeneratedProtocolMessageType('StrErrRResponse', (_message.Message,), {'DESCRIPTOR': _STRERRRRESPONSE, '__module__': 'nixnetsocket_pb2'})
_sym_db.RegisterMessage(StrErrRResponse)
_NIXNETSOCKET = DESCRIPTOR.services_by_name['NiXnetSocket']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x16com.ni.grpc.xnetsocketB\x0cNiXnetSocketP\x01\xaa\x02%NationalInstruments.Grpc.NiXnetSocket'
    _OPTNAME._options = None
    _OPTNAME._serialized_options = b'\x10\x01'
    _NIXNETSOCKETATTRIBUTE._serialized_start = 9035
    _NIXNETSOCKETATTRIBUTE._serialized_end = 9098
    _ADDRESSFAMILY._serialized_start = 9100
    _ADDRESSFAMILY._serialized_end = 9198
    _GETADDRINFOFLAGS._serialized_start = 9201
    _GETADDRINFOFLAGS._serialized_end = 9688
    _GETNAMEINFOFLAGS._serialized_start = 9691
    _GETNAMEINFOFLAGS._serialized_end = 9917
    _IPPROTOCOL._serialized_start = 9919
    _IPPROTOCOL._serialized_end = 10015
    _IPSTACKINFOSTRINGFORMAT._serialized_start = 10017
    _IPSTACKINFOSTRINGFORMAT._serialized_end = 10110
    _OPERATIONALSTATUS._serialized_start = 10112
    _OPERATIONALSTATUS._serialized_end = 10187
    _OPTNAME._serialized_start = 10190
    _OPTNAME._serialized_end = 10813
    _RECVFLAGS._serialized_start = 10815
    _RECVFLAGS._serialized_end = 10879
    _SHUTDOWN._serialized_start = 10881
    _SHUTDOWN._serialized_end = 10944
    _SOCKETOPTIONLEVEL._serialized_start = 10946
    _SOCKETOPTIONLEVEL._serialized_end = 11034
    _SOCKETPROTOCOLTYPE._serialized_start = 11036
    _SOCKETPROTOCOLTYPE._serialized_end = 11159
    _IPADDRESS._serialized_start = 88
    _IPADDRESS._serialized_end = 207
    _GATEWAYADDRESS._serialized_start = 209
    _GATEWAYADDRESS._serialized_end = 292
    _VIRTUALINTERFACE._serialized_start = 295
    _VIRTUALINTERFACE._serialized_end = 597
    _IN6ADDR._serialized_start = 599
    _IN6ADDR._serialized_end = 622
    _INADDR._serialized_start = 624
    _INADDR._serialized_end = 646
    _ADDR._serialized_start = 648
    _ADDR._serialized_end = 749
    _SOCKADDRIN._serialized_start = 751
    _SOCKADDRIN._serialized_end = 818
    _SOCKADDRIN6._serialized_start = 820
    _SOCKADDRIN6._serialized_end = 926
    _SOCKADDR._serialized_start = 928
    _SOCKADDR._serialized_end = 1041
    _ADDRINFO._serialized_start = 1044
    _ADDRINFO._serialized_end = 1351
    _ADDRINFOHINT._serialized_start = 1354
    _ADDRINFOHINT._serialized_end = 1602
    _LINGER._serialized_start = 1604
    _LINGER._serialized_end = 1647
    _IPMREQ._serialized_start = 1649
    _IPMREQ._serialized_end = 1757
    _IPV6MREQ._serialized_start = 1759
    _IPV6MREQ._serialized_end = 1849
    _SOCKOPTDATA._serialized_start = 1852
    _SOCKOPTDATA._serialized_end = 2095
    _ACCEPTREQUEST._serialized_start = 2097
    _ACCEPTREQUEST._serialized_end = 2174
    _ACCEPTRESPONSE._serialized_start = 2177
    _ACCEPTRESPONSE._serialized_end = 2334
    _BINDREQUEST._serialized_start = 2336
    _BINDREQUEST._serialized_end = 2432
    _BINDRESPONSE._serialized_start = 2434
    _BINDRESPONSE._serialized_end = 2506
    _CLOSEREQUEST._serialized_start = 2508
    _CLOSEREQUEST._serialized_end = 2562
    _CLOSERESPONSE._serialized_start = 2564
    _CLOSERESPONSE._serialized_end = 2637
    _CONNECTREQUEST._serialized_start = 2639
    _CONNECTREQUEST._serialized_end = 2738
    _CONNECTRESPONSE._serialized_start = 2740
    _CONNECTRESPONSE._serialized_end = 2815
    _FDISSETREQUEST._serialized_start = 2817
    _FDISSETREQUEST._serialized_end = 2906
    _FDISSETRESPONSE._serialized_start = 2908
    _FDISSETRESPONSE._serialized_end = 2999
    _GETADDRINFOREQUEST._serialized_start = 3002
    _GETADDRINFOREQUEST._serialized_end = 3144
    _GETADDRINFORESPONSE._serialized_start = 3146
    _GETADDRINFORESPONSE._serialized_end = 3267
    _GETNAMEINFOREQUEST._serialized_start = 3270
    _GETNAMEINFOREQUEST._serialized_end = 3487
    _GETNAMEINFORESPONSE._serialized_start = 3489
    _GETNAMEINFORESPONSE._serialized_end = 3596
    _GETPEERNAMEREQUEST._serialized_start = 3598
    _GETPEERNAMEREQUEST._serialized_end = 3658
    _GETPEERNAMERESPONSE._serialized_start = 3660
    _GETPEERNAMERESPONSE._serialized_end = 3782
    _GETSOCKNAMEREQUEST._serialized_start = 3784
    _GETSOCKNAMEREQUEST._serialized_end = 3844
    _GETSOCKNAMERESPONSE._serialized_start = 3846
    _GETSOCKNAMERESPONSE._serialized_end = 3968
    _GETSOCKOPTREQUEST._serialized_start = 3971
    _GETSOCKOPTREQUEST._serialized_end = 4206
    _GETSOCKOPTRESPONSE._serialized_start = 4208
    _GETSOCKOPTRESPONSE._serialized_end = 4334
    _INETADDRREQUEST._serialized_start = 4336
    _INETADDRREQUEST._serialized_end = 4408
    _INETADDRRESPONSE._serialized_start = 4410
    _INETADDRRESPONSE._serialized_end = 4500
    _INETATONREQUEST._serialized_start = 4502
    _INETATONREQUEST._serialized_end = 4574
    _INETATONRESPONSE._serialized_start = 4576
    _INETATONRESPONSE._serialized_end = 4693
    _INETNTOAREQUEST._serialized_start = 4695
    _INETNTOAREQUEST._serialized_end = 4799
    _INETNTOARESPONSE._serialized_start = 4801
    _INETNTOARESPONSE._serialized_end = 4894
    _INETNTOPREQUEST._serialized_start = 4896
    _INETNTOPREQUEST._serialized_end = 4994
    _INETNTOPRESPONSE._serialized_start = 4996
    _INETNTOPRESPONSE._serialized_end = 5089
    _INETPTONREQUEST._serialized_start = 5092
    _INETPTONREQUEST._serialized_end = 5242
    _INETPTONRESPONSE._serialized_start = 5244
    _INETPTONRESPONSE._serialized_end = 5358
    _IPSTACKCLEARREQUEST._serialized_start = 5360
    _IPSTACKCLEARREQUEST._serialized_end = 5424
    _IPSTACKCLEARRESPONSE._serialized_start = 5426
    _IPSTACKCLEARRESPONSE._serialized_end = 5506
    _IPSTACKCREATEREQUEST._serialized_start = 5508
    _IPSTACKCREATEREQUEST._serialized_end = 5588
    _IPSTACKCREATERESPONSE._serialized_start = 5590
    _IPSTACKCREATERESPONSE._serialized_end = 5714
    _IPSTACKGETALLSTACKSINFOSTRREQUEST._serialized_start = 5717
    _IPSTACKGETALLSTACKSINFOSTRREQUEST._serialized_end = 5851
    _IPSTACKGETALLSTACKSINFOSTRRESPONSE._serialized_start = 5853
    _IPSTACKGETALLSTACKSINFOSTRRESPONSE._serialized_end = 5961
    _IPSTACKGETINFOREQUEST._serialized_start = 5963
    _IPSTACKGETINFOREQUEST._serialized_end = 6029
    _IPSTACKGETINFORESPONSE._serialized_start = 6032
    _IPSTACKGETINFORESPONSE._serialized_end = 6179
    _IPSTACKOPENREQUEST._serialized_start = 6181
    _IPSTACKOPENREQUEST._serialized_end = 6243
    _IPSTACKOPENRESPONSE._serialized_start = 6245
    _IPSTACKOPENRESPONSE._serialized_end = 6367
    _IPSTACKWAITFORINTERFACEREQUEST._serialized_start = 6369
    _IPSTACKWAITFORINTERFACEREQUEST._serialized_end = 6489
    _IPSTACKWAITFORINTERFACERESPONSE._serialized_start = 6491
    _IPSTACKWAITFORINTERFACERESPONSE._serialized_end = 6582
    _LISTENREQUEST._serialized_start = 6584
    _LISTENREQUEST._serialized_end = 6656
    _LISTENRESPONSE._serialized_start = 6658
    _LISTENRESPONSE._serialized_end = 6732
    _RECVREQUEST._serialized_start = 6735
    _RECVREQUEST._serialized_end = 6872
    _RECVRESPONSE._serialized_start = 6874
    _RECVRESPONSE._serialized_end = 6959
    _RECVFROMREQUEST._serialized_start = 6962
    _RECVFROMREQUEST._serialized_end = 7103
    _RECVFROMRESPONSE._serialized_start = 7106
    _RECVFROMRESPONSE._serialized_end = 7243
    _SELECTREQUEST._serialized_start = 7246
    _SELECTREQUEST._serialized_end = 7431
    _SELECTRESPONSE._serialized_start = 7433
    _SELECTRESPONSE._serialized_end = 7507
    _SENDREQUEST._serialized_start = 7509
    _SENDREQUEST._serialized_end = 7598
    _SENDRESPONSE._serialized_start = 7600
    _SENDRESPONSE._serialized_end = 7672
    _SENDTOREQUEST._serialized_start = 7675
    _SENDTOREQUEST._serialized_end = 7807
    _SENDTORESPONSE._serialized_start = 7809
    _SENDTORESPONSE._serialized_end = 7883
    _SETSOCKOPTREQUEST._serialized_start = 7886
    _SETSOCKOPTREQUEST._serialized_end = 8171
    _SETSOCKOPTRESPONSE._serialized_start = 8173
    _SETSOCKOPTRESPONSE._serialized_end = 8251
    _SHUTDOWNREQUEST._serialized_start = 8254
    _SHUTDOWNREQUEST._serialized_end = 8386
    _SHUTDOWNRESPONSE._serialized_start = 8388
    _SHUTDOWNRESPONSE._serialized_end = 8464
    _SOCKETREQUEST._serialized_start = 8467
    _SOCKETREQUEST._serialized_end = 8816
    _SOCKETRESPONSE._serialized_start = 8818
    _SOCKETRESPONSE._serialized_end = 8932
    _STRERRRREQUEST._serialized_start = 8934
    _STRERRRREQUEST._serialized_end = 8983
    _STRERRRRESPONSE._serialized_start = 8985
    _STRERRRRESPONSE._serialized_end = 9033
    _NIXNETSOCKET._serialized_start = 11162
    _NIXNETSOCKET._serialized_end = 13930
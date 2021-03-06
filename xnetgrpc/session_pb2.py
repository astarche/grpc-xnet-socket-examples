# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: session.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rsession.proto\x12\rnidevice_grpc\"2\n\x07Session\x12\x0e\n\x04name\x18\x01 \x01(\tH\x00\x12\x0c\n\x02id\x18\x02 \x01(\rH\x00\x42\t\n\x07session\"V\n\x10\x44\x65viceProperties\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05model\x18\x02 \x01(\t\x12\x0e\n\x06vendor\x18\x03 \x01(\t\x12\x15\n\rserial_number\x18\x04 \x01(\t\"\x19\n\x17\x45numerateDevicesRequest\"L\n\x18\x45numerateDevicesResponse\x12\x30\n\x07\x64\x65vices\x18\x01 \x03(\x0b\x32\x1f.nidevice_grpc.DeviceProperties\";\n\x0eReserveRequest\x12\x16\n\x0ereservation_id\x18\x01 \x01(\t\x12\x11\n\tclient_id\x18\x02 \x01(\t\"&\n\x0fReserveResponse\x12\x13\n\x0bis_reserved\x18\x01 \x01(\x08\"F\n\x19IsReservedByClientRequest\x12\x16\n\x0ereservation_id\x18\x01 \x01(\t\x12\x11\n\tclient_id\x18\x02 \x01(\t\"1\n\x1aIsReservedByClientResponse\x12\x13\n\x0bis_reserved\x18\x01 \x01(\x08\"=\n\x10UnreserveRequest\x12\x16\n\x0ereservation_id\x18\x01 \x01(\t\x12\x11\n\tclient_id\x18\x02 \x01(\t\"*\n\x11UnreserveResponse\x12\x15\n\ris_unreserved\x18\x01 \x01(\x08\"\x14\n\x12ResetServerRequest\".\n\x13ResetServerResponse\x12\x17\n\x0fis_server_reset\x18\x01 \x01(\x08\x32\xd2\x03\n\x10SessionUtilities\x12\x63\n\x10\x45numerateDevices\x12&.nidevice_grpc.EnumerateDevicesRequest\x1a\'.nidevice_grpc.EnumerateDevicesResponse\x12H\n\x07Reserve\x12\x1d.nidevice_grpc.ReserveRequest\x1a\x1e.nidevice_grpc.ReserveResponse\x12i\n\x12IsReservedByClient\x12(.nidevice_grpc.IsReservedByClientRequest\x1a).nidevice_grpc.IsReservedByClientResponse\x12N\n\tUnreserve\x12\x1f.nidevice_grpc.UnreserveRequest\x1a .nidevice_grpc.UnreserveResponse\x12T\n\x0bResetServer\x12!.nidevice_grpc.ResetServerRequest\x1a\".nidevice_grpc.ResetServerResponseBB\n\x12\x63om.ni.grpc.deviceB\x08NiDeviceP\x01\xaa\x02\x1fNationalInstruments.Grpc.Deviceb\x06proto3')



_SESSION = DESCRIPTOR.message_types_by_name['Session']
_DEVICEPROPERTIES = DESCRIPTOR.message_types_by_name['DeviceProperties']
_ENUMERATEDEVICESREQUEST = DESCRIPTOR.message_types_by_name['EnumerateDevicesRequest']
_ENUMERATEDEVICESRESPONSE = DESCRIPTOR.message_types_by_name['EnumerateDevicesResponse']
_RESERVEREQUEST = DESCRIPTOR.message_types_by_name['ReserveRequest']
_RESERVERESPONSE = DESCRIPTOR.message_types_by_name['ReserveResponse']
_ISRESERVEDBYCLIENTREQUEST = DESCRIPTOR.message_types_by_name['IsReservedByClientRequest']
_ISRESERVEDBYCLIENTRESPONSE = DESCRIPTOR.message_types_by_name['IsReservedByClientResponse']
_UNRESERVEREQUEST = DESCRIPTOR.message_types_by_name['UnreserveRequest']
_UNRESERVERESPONSE = DESCRIPTOR.message_types_by_name['UnreserveResponse']
_RESETSERVERREQUEST = DESCRIPTOR.message_types_by_name['ResetServerRequest']
_RESETSERVERRESPONSE = DESCRIPTOR.message_types_by_name['ResetServerResponse']
Session = _reflection.GeneratedProtocolMessageType('Session', (_message.Message,), {
  'DESCRIPTOR' : _SESSION,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:nidevice_grpc.Session)
  })
_sym_db.RegisterMessage(Session)

DeviceProperties = _reflection.GeneratedProtocolMessageType('DeviceProperties', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEPROPERTIES,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:nidevice_grpc.DeviceProperties)
  })
_sym_db.RegisterMessage(DeviceProperties)

EnumerateDevicesRequest = _reflection.GeneratedProtocolMessageType('EnumerateDevicesRequest', (_message.Message,), {
  'DESCRIPTOR' : _ENUMERATEDEVICESREQUEST,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:nidevice_grpc.EnumerateDevicesRequest)
  })
_sym_db.RegisterMessage(EnumerateDevicesRequest)

EnumerateDevicesResponse = _reflection.GeneratedProtocolMessageType('EnumerateDevicesResponse', (_message.Message,), {
  'DESCRIPTOR' : _ENUMERATEDEVICESRESPONSE,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:nidevice_grpc.EnumerateDevicesResponse)
  })
_sym_db.RegisterMessage(EnumerateDevicesResponse)

ReserveRequest = _reflection.GeneratedProtocolMessageType('ReserveRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESERVEREQUEST,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:nidevice_grpc.ReserveRequest)
  })
_sym_db.RegisterMessage(ReserveRequest)

ReserveResponse = _reflection.GeneratedProtocolMessageType('ReserveResponse', (_message.Message,), {
  'DESCRIPTOR' : _RESERVERESPONSE,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:nidevice_grpc.ReserveResponse)
  })
_sym_db.RegisterMessage(ReserveResponse)

IsReservedByClientRequest = _reflection.GeneratedProtocolMessageType('IsReservedByClientRequest', (_message.Message,), {
  'DESCRIPTOR' : _ISRESERVEDBYCLIENTREQUEST,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:nidevice_grpc.IsReservedByClientRequest)
  })
_sym_db.RegisterMessage(IsReservedByClientRequest)

IsReservedByClientResponse = _reflection.GeneratedProtocolMessageType('IsReservedByClientResponse', (_message.Message,), {
  'DESCRIPTOR' : _ISRESERVEDBYCLIENTRESPONSE,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:nidevice_grpc.IsReservedByClientResponse)
  })
_sym_db.RegisterMessage(IsReservedByClientResponse)

UnreserveRequest = _reflection.GeneratedProtocolMessageType('UnreserveRequest', (_message.Message,), {
  'DESCRIPTOR' : _UNRESERVEREQUEST,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:nidevice_grpc.UnreserveRequest)
  })
_sym_db.RegisterMessage(UnreserveRequest)

UnreserveResponse = _reflection.GeneratedProtocolMessageType('UnreserveResponse', (_message.Message,), {
  'DESCRIPTOR' : _UNRESERVERESPONSE,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:nidevice_grpc.UnreserveResponse)
  })
_sym_db.RegisterMessage(UnreserveResponse)

ResetServerRequest = _reflection.GeneratedProtocolMessageType('ResetServerRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESETSERVERREQUEST,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:nidevice_grpc.ResetServerRequest)
  })
_sym_db.RegisterMessage(ResetServerRequest)

ResetServerResponse = _reflection.GeneratedProtocolMessageType('ResetServerResponse', (_message.Message,), {
  'DESCRIPTOR' : _RESETSERVERRESPONSE,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:nidevice_grpc.ResetServerResponse)
  })
_sym_db.RegisterMessage(ResetServerResponse)

_SESSIONUTILITIES = DESCRIPTOR.services_by_name['SessionUtilities']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\022com.ni.grpc.deviceB\010NiDeviceP\001\252\002\037NationalInstruments.Grpc.Device'
  _SESSION._serialized_start=32
  _SESSION._serialized_end=82
  _DEVICEPROPERTIES._serialized_start=84
  _DEVICEPROPERTIES._serialized_end=170
  _ENUMERATEDEVICESREQUEST._serialized_start=172
  _ENUMERATEDEVICESREQUEST._serialized_end=197
  _ENUMERATEDEVICESRESPONSE._serialized_start=199
  _ENUMERATEDEVICESRESPONSE._serialized_end=275
  _RESERVEREQUEST._serialized_start=277
  _RESERVEREQUEST._serialized_end=336
  _RESERVERESPONSE._serialized_start=338
  _RESERVERESPONSE._serialized_end=376
  _ISRESERVEDBYCLIENTREQUEST._serialized_start=378
  _ISRESERVEDBYCLIENTREQUEST._serialized_end=448
  _ISRESERVEDBYCLIENTRESPONSE._serialized_start=450
  _ISRESERVEDBYCLIENTRESPONSE._serialized_end=499
  _UNRESERVEREQUEST._serialized_start=501
  _UNRESERVEREQUEST._serialized_end=562
  _UNRESERVERESPONSE._serialized_start=564
  _UNRESERVERESPONSE._serialized_end=606
  _RESETSERVERREQUEST._serialized_start=608
  _RESETSERVERREQUEST._serialized_end=628
  _RESETSERVERRESPONSE._serialized_start=630
  _RESETSERVERRESPONSE._serialized_end=676
  _SESSIONUTILITIES._serialized_start=679
  _SESSIONUTILITIES._serialized_end=1145
# @@protoc_insertion_point(module_scope)

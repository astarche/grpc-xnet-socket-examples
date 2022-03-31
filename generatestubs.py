from os import system

system(
    rf"poetry run python -m grpc_tools.protoc --python_out=xnetgrpc --grpc_python_out=xnetgrpc --mypy_out=xnetgrpc --mypy_grpc_out=xnetgrpc --proto_path=proto nixnetsocket.proto session.proto"
)

system(
    rf"poetry run protol --create-package --in-place --python-out xnetgrpc protoc --proto-path proto proto/session.proto proto/nixnetsocket.proto"
)

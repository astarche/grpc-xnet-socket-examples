from subprocess import run

run(
    rf"python -m grpc_tools.protoc --python_out=xnetgrpc --grpc_python_out=xnetgrpc --mypy_out=xnetgrpc --mypy_grpc_out=xnetgrpc --proto_path=proto nixnetsocket.proto session.proto",
    shell=True,
    check=True,
)

run(
    rf"protol --create-package --in-place --python-out xnetgrpc protoc --proto-path proto proto/session.proto proto/nixnetsocket.proto",
    shell=True,
    check=True,
)

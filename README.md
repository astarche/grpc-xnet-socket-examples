# grpc-xnet-socket-examples

Example code for the XNET Automotive Ethernet Socket API from [grpc-device](https://github.com/ni/grpc-device).

# Instructions

## Prerequisites

1. Install python
2. [Get Poetry](https://python-poetry.org/docs/)
   - Recommended: Set [virtualenvs.in-project](https://python-poetry.org/docs/configuration/#virtualenvsin-project) to true.
3. Install [NI-XNET driver](https://www.ni.com/en-us/support/downloads/drivers/download.ni-xnet.html#442810).
4. Download grpc-device server from latest builds, or from releases >=1.5
   - In pre-release 1.5 builds add `"code_readiness": "nextrelease",` to `server_config.json`
5. Run `ni_grpc_device_server.exe`

## Clone the project and install dependencies

```
git clone https://github.com/astarche/grpc-xnet-socket-examples
cd grpc-xnet-socket-examples
poetry install
```

## Run the examples

```
poetry run python -m client.loopback -s localhost:31763
poetry run python -m client.udp -s localhost:31763
```

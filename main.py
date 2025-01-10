from fastapi import FastAPI
import uvicorn
from uvicorn import Config, Server
from Router.python import router as python_router
from Router.index import router as index_router
from Router.windows import router as windows_router
from Service.exploit_socket import socket_server
import threading
import signal
import sys
import socket
import atexit
import asyncio

app = FastAPI()
app.include_router(index_router)
app.include_router(python_router)
app.include_router(windows_router)

def additional_cleanup():
    print("Performing additional cleanup tasks...")
    from Service.exploit_socket import close_all_clients
    close_all_clients()

# def signal_handler(sig, frame):
#     print("Shutting down server...")
#     # Do not close the global socket
#     socket_thread.join(timeout=1)
#     sys.exit(0)

atexit.register(additional_cleanup)

async def run_uvicorn():
    config = Config("main:app", host="0.0.0.0", port=44444, workers=4, log_config="logging_config.json")
    server = Server(config)
    await server.serve()

async def main():
    socket_server_task = asyncio.create_task(socket_server("0.0.0.0", 12345))
    uvicorn_task = asyncio.create_task(run_uvicorn())
    await asyncio.gather(socket_server_task, uvicorn_task)

if __name__ == '__main__':
    asyncio.run(main())
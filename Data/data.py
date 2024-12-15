from pydantic import BaseModel

class PayloadInfo(BaseModel):
    platform: str
    arch: str = None
    LHOST: str
    LPORT: int
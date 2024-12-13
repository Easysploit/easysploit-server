from pydantic import BaseModel

class PayloadInfo(BaseModel):
    platform: str
    LHOST: str
    LPORT: int
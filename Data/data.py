from pydantic import BaseModel

class PayloadInfo(BaseModel):
    LHOST: str
    LPORT: int
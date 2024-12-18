from fastapi import FastAPI
import uvicorn
from Router.payload import router as payload_router
from Router.index import router as index_router

# FastAPI 애플리케이션 생성
app = FastAPI()
app.include_router(index_router)
app.include_router(payload_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=44444, workers=4)
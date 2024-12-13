from fastapi import FastAPI
import uvicorn
from Router.payload import router

# FastAPI 애플리케이션 생성
app = FastAPI()
app.include_router(router)

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=1500, workers=4)
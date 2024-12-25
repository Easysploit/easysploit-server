from fastapi import FastAPI
import uvicorn
from Router.python import router as python_router
from Router.index import router as index_router
from Router.windows import router as windows_router

# FastAPI 애플리케이션 생성
app = FastAPI()
app.include_router(index_router)
app.include_router(python_router)
app.include_router(windows_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=44444, workers=4)
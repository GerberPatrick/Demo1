from fastapi import FastAPI
from Web import parameter

app = FastAPI()

app.include_router(parameter.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

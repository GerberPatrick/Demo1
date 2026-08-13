from fastapi import FastAPI
from Web import parameter

app = FastAPI() #FastAPI Instanz erstellen

app.include_router(parameter.router) #Router einbinden 

if __name__ == "__main__": #Main Funktion
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True) #Uvicorn Server starten

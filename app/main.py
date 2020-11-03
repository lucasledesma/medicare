
from fastapi import FastAPI,Depends
from pydantic import BaseModel
from .db import database
from .providers import router
from fastapi.middleware.cors import CORSMiddleware
from .config import get_settings

app = FastAPI(title = get_settings().app_name)

app.include_router(
    router,
    prefix="/providers",
)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()    

@app.get("/info")
async def info():
    return {
        "app_name": get_settings().app_name,
    }    
 


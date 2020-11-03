
from fastapi import FastAPI,Depends
from pydantic import BaseModel
from db import database
from controller import router
from fastapi.middleware.cors import CORSMiddleware
import config

app = FastAPI(title = config.get_settings().app_name)

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
        "app_name": config.get_settings().app_name,
    }    
 


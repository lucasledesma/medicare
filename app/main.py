
from fastapi import FastAPI
from pydantic import BaseModel
from db import database
from controller import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title = "Medicare")

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

 


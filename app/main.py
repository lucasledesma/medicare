
from fastapi import FastAPI,Depends
from .database import engine,SessionLocal
from .config import get_settings
from .init import init_db
import logging
from .providers import router
from . import models
import os

models.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title=get_settings().app_name,
    description="This API provides access to Medicare Providers Payment and Utilization Data"
)

app.include_router(
    router,
    prefix="/providers",
)

@app.get("/info")
async def info():
    return {
        "app_name": get_settings().app_name,
        "environment": get_settings().environment,
    }


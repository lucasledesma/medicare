
from fastapi import FastAPI
from .database import engine
from .providers import router
from .config import get_settings
from . import models

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
    }

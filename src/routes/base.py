from fastapi import FastAPI, APIRouter
import os
base_router = APIRouter()

@base_router.get("/")
async def Welcome():
    app_name = os.getenv("APP_NAME")
    return {"hi":"FastAPI is very easy",
            "APP_NAME":app_name}
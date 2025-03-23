from fastapi import FastAPI
from app.api.routes import router as order_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Beer Bar API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(order_router, prefix="/api", tags=["order"])
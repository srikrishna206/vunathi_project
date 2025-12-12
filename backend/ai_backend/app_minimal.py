from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import logging

logger = logging.getLogger(__name__)

app = FastAPI(title="Novaya AI Backend", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Novaya AI Backend is running"}

@app.get("/docs")
async def docs():
    return {"message": "API documentation available at /docs"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

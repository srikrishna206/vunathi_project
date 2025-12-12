from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
import logging

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Novaya AI Backend",
    description="AI-powered educational assistant for Novaya LMS",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Enhanced CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://34.224.216.146:3000", "http://localhost:3000", "*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["*", "Authorization", "Content-Type", "Accept", "Origin"],
    expose_headers=["*"]
)

# Handle OPTIONS requests globally
@app.options("/{path:path}")
async def options_handler(path: str):
    return JSONResponse(
        content={"message": "CORS preflight"},
        headers={
            "Access-Control-Allow-Origin": "http://34.224.216.146:3000",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS, PATCH",
            "Access-Control-Allow-Headers": "Authorization, Content-Type, Accept, Origin",
            "Access-Control-Allow-Credentials": "true"
        }
    )

@app.get("/")
async def root():
    return {
        "message": "Novaya AI Backend is running",
        "status": "healthy",
        "version": "1.0.0"
    }

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "ai-backend"}

@app.get("/info")
async def info():
    return {
        "name": "Novaya AI Backend",
        "version": "1.0.0",
        "description": "AI-powered educational assistant",
        "endpoints": {
            "docs": "/docs",
            "health": "/health",
            "info": "/info",
            "classes": "/classes"
        }
    }

# Classes endpoint for frontend compatibility
@app.get("/classes")
async def get_classes():
    """
    Return classes data for frontend - QuickPractice component
    """
    return [
        {
            "id": 1,
            "name": "Mathematics",
            "grade": "Grade 5",
            "subject": "math",
            "color": "#FF6B6B",
            "icon": "calculator",
            "description": "Learn numbers, algebra, and geometry"
        },
        {
            "id": 2,
            "name": "Science", 
            "grade": "Grade 5",
            "subject": "science",
            "color": "#4ECDC4",
            "icon": "flask",
            "description": "Explore physics, chemistry, and biology"
        },
        {
            "id": 3,
            "name": "English",
            "grade": "Grade 5", 
            "subject": "english",
            "color": "#45B7D1",
            "icon": "book",
            "description": "Improve reading, writing, and communication"
        },
        {
            "id": 4,
            "name": "Social Studies",
            "grade": "Grade 5",
            "subject": "social",
            "color": "#96CEB4",
            "icon": "globe",
            "description": "Discover history, geography, and civics"
        },
        {
            "id": 5,
            "name": "Computer Science",
            "grade": "Grade 5",
            "subject": "computer",
            "color": "#FFEAA7",
            "icon": "laptop",
            "description": "Learn coding and digital skills"
        }
    ]

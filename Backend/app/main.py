from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import router as todo_router

app = FastAPI(
    title="Todo API",
    description="Simple Todo List API with in-memory storage",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(todo_router)


@app.get("/")
def root():
    return {"message": "Todo API is running!", "version": "1.0.0"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}

from fastapi import FastAPI
from app.routes.documents import router as document_router

app = FastAPI(
    title = "KnowledgeBox",
    description = "Personal AI Knowledge Assistant",
    version="1.0.0"
)
app.include_router(document_router)

@app.get("/")
def home():
    return {
        "message" : "Welcome to KnowledgeBox!"
    }

@app.get("/health")
def health():
    return {
        "status" : "healthy"
    }
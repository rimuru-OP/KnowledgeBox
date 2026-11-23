from fastapi import FastAPI

app = FastAPI(
    title = "KnowledgeBox",
    description = "Personal AI Knowledge Assistant",
    version="1.0.0"
)

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
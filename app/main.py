from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="AI Business Workflow Orchestrator")

app.include_router(router)

@app.get("/")
def home():
    return {"message": "AI Workflow API Running"}
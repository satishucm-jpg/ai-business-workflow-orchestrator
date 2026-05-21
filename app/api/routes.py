from fastapi import APIRouter
from pydantic import BaseModel
from app.workflow.graph import run_workflow

router = APIRouter()

class WorkflowRequest(BaseModel):
    task: str

@router.post("/run-workflow")
def execute_workflow(request: WorkflowRequest):
    result = run_workflow(request.task)
    return result
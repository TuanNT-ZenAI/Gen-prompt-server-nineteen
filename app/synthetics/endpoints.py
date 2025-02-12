from fastapi import APIRouter
from pydantic import BaseModel
from .synthetic_generation_funcs import generate_synthetic_data
router = APIRouter()

class TaskName(BaseModel):
    task: str

async def get_synthetic_data(
    data: TaskName
):
    return await generate_synthetic_data(data.task)

router.add_api_route(
    path="/get-synthetic-data",
    tags=["synthetic"],
    endpoint=get_synthetic_data,
    methods=["POST"],
)
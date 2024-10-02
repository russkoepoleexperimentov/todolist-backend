from fastapi import APIRouter, Depends

from ..depends import get_task_service
from ..schemas.task import *

router = APIRouter(prefix="/task")


@router.get(".getlist", response_model=list[TaskOutSchema])
def get_all_tasks(service=Depends(get_task_service)):
    return service.read_all()


@router.get(".get", response_model=TaskOutSchema)
def get_task(id: int, service=Depends(get_task_service)):
    return service.read(id)


@router.post(".create", response_model=TaskOutSchema)
def create_task(schema: TaskCreateSchema, service=Depends(get_task_service)):
    return service.create(schema)


@router.put(".update", response_model=TaskOutSchema)
def update_task(schema: TaskUpdateSchema, service=Depends(get_task_service)):
    return service.update(schema)


@router.delete(".delete", response_model=TaskOutSchema)
def delete_task(id: int, service=Depends(get_task_service)):
    return service.delete(id)
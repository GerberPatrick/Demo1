from fastapi import APIRouter
from Model.parameter import Parameter
import Dummy.parameter as service

router = APIRouter(prefix = "/parameter")

@router.get("/")
def get_parameters() -> list[Parameter]:
    return service.get_parameters()

@router.get("/{name}")
def get_parameter(name: str) -> Parameter | None:
    return service.get_parameter(name)

@router.post("/")
def create_parameter(parameter: Parameter) -> Parameter:
    return service.create_parameter(parameter)

@router.patch("/")
def update_parameter(parameter: Parameter) -> Parameter:
    return service.update_parameter(parameter)

@router.put("/")
def replace_parameter(parameter: Parameter) -> Parameter:
    return service.replace_parameter(parameter)

@router.delete("/{name}")
def delete_parameter(name: str):
    return None

from Model.parameter import Parameter
import Dummy.parameter as data

def get_parameters() -> list[Parameter]:
    return data.get_parameters()

def get_parameter(name: str) -> Parameter | None:
    return data.get_parameter(name)

def create_parameter(parameter: Parameter) -> Parameter:
    return data.create_parameter(parameter)

def update_parameter(id: int, parameter: Parameter) -> Parameter:
    return data.update_parameter(id, parameter)

def replace_parameter(id: int, parameter: Parameter) -> Parameter:
    return data.replace_parameter(id, parameter)

def delete_parameter(id: int, parameter: Parameter) -> bool:
    return data.delete_parameter(id)

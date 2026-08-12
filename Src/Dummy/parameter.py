from Model.parameter import Parameter

_parameters = \
[
    Parameter(id=1, name="Glucose", unit="mg/dl", value=10.0),
    Parameter(id=2, name="Iron", unit="mg/dl", value=6.5),
    Parameter(id=3, name="CRP", unit="mg/dl", value=0.1),
]

def get_parameters() -> list[Parameter]:
    return _parameters

def get_parameter(name: str) -> Parameter | None:
    for _parameter in _parameters:
        if _parameter.name == name:
            return _parameter
    return None

def create_parameter(parameter: Parameter) -> Parameter:
    return parameter

def update_parameter(parameter: Parameter) -> Parameter:
    return parameter

def replace_parameter(parameter: Parameter) -> Parameter:
    return parameter

def delete_parameter(parameter: Parameter) -> bool:
    return None  

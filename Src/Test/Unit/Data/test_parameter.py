import os
import pytest
from Model.parameter import Parameter
from Error.errors import MissingParameterError, DuplicateParameterError

os.environ["DATABASE_NAME"] = ":memory:" #Datenbank in der Speicher-Datei
from Data import parameter
#Test-Funktionen für die CRUD Operationen -> Data-Layer
@pytest.fixture
def sample_parameter() -> Parameter:
    return Parameter(id=1, name="Glucose", unit="mg/dl", value=6.0)

def test_create_parameter(sample_parameter: Parameter):
    resp = parameter.create_parameter(sample_parameter)
    assert resp == sample_parameter

def test_create_duplicate_parameter(sample_parameter: Parameter):
    with pytest.raises(DuplicateParameterError):
        parameter.create_parameter(sample_parameter)

def test_get_parameter(sample_parameter: Parameter):
    resp = parameter.get_parameter(sample_parameter.name)
    assert resp == sample_parameter

def test_get_parameters(sample_parameter: Parameter):
    resp = parameter.get_parameters()
    assert sample_parameter in resp
    assert len(resp) == 3

def test_get_parameter_missing():
    with pytest.raises(MissingParameterError):
        parameter.get_parameter("Missing")

def test_update_parameter(sample_parameter: Parameter):
    parameter.name = "Iron"
    resp = parameter.update_parameter(sample_parameter.name, sample_parameter)
    assert resp == sample_parameter

def test_update_parameter_missing():
    sample: Parameter = Parameter(id=2, name="Protein", unit="mg/dl", value=20.0)
    with pytest.raises(MissingParameterError):
        parameter.update_parameter(sample.name, sample)

def test_replace_parameter(sample_parameter: Parameter):
    resp = parameter.replace_parameter(sample_parameter.name, sample_parameter)
    assert resp == sample_parameter

def test_replace_parameter_missing(sample_parameter: Parameter):
    sample: Parameter = Parameter(id=2, name="Protein", unit="mg/dl", value=20.0)
    with pytest.raises(MissingParameterError):
        parameter.replace_parameter(sample.name, sample)

def test_delete_parameter(sample_parameter: Parameter):
    resp = parameter.delete_parameter(sample_parameter.name)
    assert resp is None

def test_delete_parameter_missing(sample_parameter: Parameter):
    with pytest.raises(MissingParameterError):
        parameter.delete_parameter(sample_parameter.name)

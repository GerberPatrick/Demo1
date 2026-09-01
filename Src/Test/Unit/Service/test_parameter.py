import os
import pytest
from pydantic import ValidationError
from Model.parameter import Parameter, Create, Update, Replace
from Error.errors import MissingParameterError, DuplicateParameterError

os.environ["DATABASE_NAME"] = ":memory:"
from Data import init as db
from Data import parameter
from Service import parameter as code

CREATE_TABLE = \
(
    "CREATE TABLE IF NOT EXISTS PARAMETER("
    "id INTEGER PRIMARY KEY, name UNIQUE, unit TEXT, value REAL)"
)

@pytest.fixture(autouse=True)
def isolated_db():
    db.init(name=":memory:", reset=True)
    parameter.connection = db.connection
    parameter.cursor = db.cursor
    parameter.cursor.execute(CREATE_TABLE)
    
#Test-Funktionen für die CRUD Operationen -> Service-Layer
@pytest.fixture
def glucose() -> Parameter:
    return code.create_parameter(Create(name="Glucose", unit="mg/dl", value=10.0))

def test_create_parameter():
    body = Create(name="Glucose", unit="mg/dl", value=10.0)
    resp = code.create_parameter(body)
    assert resp.name == "Glucose"
    assert resp.unit == "mg/dl"
    assert resp.value == 10.0
    assert isinstance(resp.id, int)

def test_get_parameter(glucose: Parameter):
    resp = code.get_parameter("Glucose")
    assert resp == glucose

def test_get_parameters(glucose: Parameter):
    resp = code.get_parameters()
    assert glucose in resp
    assert len(resp) == 1

def test_update_parameter(glucose: Parameter):
    body = Update(value=12.0)
    resp = code.update_parameter("Glucose", body)
    assert resp.value == 12.0
    assert resp.unit == "mg/dl"
    assert resp.name == "Glucose"
    assert resp.id == glucose.id

def test_replace_parameter(glucose: Parameter):
    body = Replace(name="Glucose", unit="mmol/l", value=8.0)
    resp = code.replace_parameter("Glucose", body)
    assert resp.unit == "mmol/l"
    assert resp.value == 8.0
    assert resp.id == glucose.id

def test_delete_parameter(glucose: Parameter):
    resp = code.delete_parameter(glucose.name)
    assert resp is None
    with pytest.raises(MissingParameterError):
        code.get_parameter(glucose.name)

def test_create_duplicate_parameter(glucose: Parameter):
    with pytest.raises(DuplicateParameterError):
        code.create_parameter(Create(name="Glucose", unit="mg/dl", value=10.0))

def test_get_parameter_missing():
    with pytest.raises(MissingParameterError):
        code.get_parameter("Missing")

def test_update_parameter_missing():
    with pytest.raises(MissingParameterError):
        code.update_parameter("Missing", Update(value=1.0))

def test_update_rejects_name_field():
    with pytest.raises(ValidationError):
        Update(name="Iron")

def test_replace_parameter_missing():
    with pytest.raises(MissingParameterError):
        code.replace_parameter("Missing", Replace(name="Missing", unit="mg/dl", value=1.0))

def test_replace_parameter_name_mismatch(glucose: Parameter):
    with pytest.raises(ValueError, match="does not match"):
        code.replace_parameter("Glucose", Replace(name="Iron", unit="mg/dl", value=1.0))

def test_delete_parameter_missing():
    with pytest.raises(MissingParameterError):
        code.delete_parameter("Missing")

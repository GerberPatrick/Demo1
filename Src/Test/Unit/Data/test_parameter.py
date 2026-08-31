import os
import pytest
from Model.parameter import Parameter, Create
from Error.errors import MissingParameterError, DuplicateParameterError

os.environ["DATABASE_NAME"] = ":memory:" #Datenbank in der Speicher-Datei
from Data import init as db
from Data import parameter

CREATE_TABLE = \
(
    "CREATE TABLE IF NOT EXISTS PARAMETER("
    "id INTEGER PRIMARY KEY, name UNIQUE, unit TEXT, value REAL)"
)

#Test-Funktionen für die CRUD Operationen -> Data-Layer
@pytest.fixture(autouse=True)
def isolated_db():
    db.init(name=":memory:", reset=True)
    parameter.connection = db.connection
    parameter.cursor = db.cursor
    parameter.cursor.execute(CREATE_TABLE)

@pytest.fixture
def glucose() -> Parameter:
    return parameter.create_parameter(Create(name="Glucose", unit="mg/dl", value=6.0))

def test_create_parameter():
    body = Create(name="Glucose", unit="mg/dl", value=6.0)
    resp = parameter.create_parameter(body)
    assert resp.name == "Glucose"
    assert resp.unit == "mg/dl"
    assert resp.value == 6.0
    assert isinstance(resp.id, int)

def test_create_duplicate_parameter(glucose: Parameter):
    body = Create(name="Glucose", unit="mg/dl", value=6.0)
    with pytest.raises(DuplicateParameterError):
        parameter.create_parameter(body)

def test_get_parameter(glucose: Parameter):
    resp = parameter.get_parameter(glucose.name)
    assert resp == glucose

def test_get_parameters(glucose: Parameter):
    resp = parameter.get_parameters()
    assert glucose in resp
    assert len(resp) == 1

def test_get_parameters_empty():
    assert parameter.get_parameters() == []

def test_get_parameter_missing():
    with pytest.raises(MissingParameterError):
        parameter.get_parameter("Missing")

def test_replace_parameter(glucose: Parameter):
    replaced = Parameter(id=glucose.id, name="Glucose", unit="mmol/l", value=8.0)
    resp = parameter.replace_parameter(glucose.name, replaced)
    assert resp == replaced

def test_replace_parameter_missing():
    sample = Parameter(id=2, name="Protein", unit="mg/dl", value=20.0)
    with pytest.raises(MissingParameterError):
        parameter.replace_parameter(sample.name, sample)

def test_delete_parameter(glucose: Parameter):
    resp = parameter.delete_parameter(glucose.name)
    assert resp is None
    with pytest.raises(MissingParameterError):
        parameter.get_parameter(glucose.name)
        
def test_delete_parameter_missing():
    with pytest.raises(MissingParameterError):
        parameter.delete_parameter("Missing")

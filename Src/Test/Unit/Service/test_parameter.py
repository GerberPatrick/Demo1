import os
import pytest
from Model.parameter import Parameter, Create, Update, Replace

os.environ["DATABASE_NAME"] = ":memory:"
from Data import init as db
from Data import parameter
from Service import parameter as code

CREATE_TABLE = \
(
    "CREATE TABLE IF NOT EXISTS PARAMETER("
    "id INTEGER PRIMARY KEY, name UNIQUE, unit TEXT, value REAL)"
)

@pytest.fixture(scope="module", autouse=True)
def isolated_db():
    db.init(name=":memory:", reset=True)
    parameter.connection = db.connection
    parameter.cursor = db.cursor
    parameter.cursor.execute(CREATE_TABLE)
    
#Test-Funktionen für die CRUD Operationen -> Service-Layer
@pytest.fixture
def sample() -> Parameter:
    return Parameter(id=1, name="Glucose", unit="mg/dl", value=10.0)

def test_create_parameter():
    body = Create(name="Glucose", unit="mg/dl", value=10.0)
    resp = code.create_parameter(body)
    assert resp.name == "Glucose"
    assert resp.unit == "mg/dl"
    assert resp.value == 10.0
    assert isinstance(resp.id, int)

def test_get_parameter(sample: Parameter):
    resp = code.get_parameter("Glucose")
    assert resp == sample

def test_get_parameters(sample: Parameter):
    resp = code.get_parameters()
    assert sample in resp
    assert len(resp) == 1

def test_update_parameter(sample: Parameter):
    body = Update(value=12.0)
    resp = code.update_parameter("Glucose", body)
    assert resp.value == 12.0
    assert resp.unit == "mg/dl"
    assert resp.name == "Glucose"
    assert resp.id == sample.id

def test_replace_parameter(sample: Parameter):
    body = Replace(name="Glucose", unit="mmol/l", value=8.0)
    resp = code.replace_parameter("Glucose", body)
    assert resp.unit == "mmol/l"
    assert resp.value == 8.0
    assert resp.id == sample.id

def test_delete_parameter():
    resp = code.delete_parameter("Glucose")
    assert resp is None

from Model.parameter import Parameter
from Service import parameter as code

sample = Parameter(id=1, name="Glucose", unit="mg/dl", value=10.0)

def test_create_parameter():
    resp = code.create_parameter(sample)
    assert resp == sample

def test_get_parameter():
    resp = code.get_parameter("Glucose")
    assert resp == sample

from Model.parameter import Parameter
from Service import parameter as code

sample = Parameter(id=1, name="Glucose", unit="mg/dl", value=10.0)

def test_create_parameter(): 
    resp = code.create_parameter(sample) 
    assert resp == sample

def test_get_parameter():
    resp = code.get_parameter("Glucose")
    assert resp == sample

def test_get_parameters():
    resp = code.get_parameters()
    assert sample in resp
    assert len(resp) == 3

def test_update_parameter():
    resp = code.update_parameter(sample)
    assert resp == sample

def test_replace_parameter():
    resp = code.replace_parameter(sample)
    assert resp == sample

def test_delete_parameter():
    resp = code.delete_parameter("Glucose")
    assert resp == None

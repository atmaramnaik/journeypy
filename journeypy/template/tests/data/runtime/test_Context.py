import pytest
from journeypy.template.data.runtime.Context import Context
def test_pour_to_list_when_source_is_equal_to_target():
    l1=[{"name":"atmaram"}]
    l2=[{"place":"pune"}]
    Context.pour_to_list(l1,l2)
    obj={"name":"atmaram","place":"pune"}
    assert obj in l1

def test_pour_to_list_when_source_is_less_than_target():
    l1=[{"name":"atmaram"},{"name":"yogesh"}]
    l2=[{"place":"pune"}]
    Context.pour_to_list(l1,l2)
    obj1={"name":"atmaram","place":"pune"}
    obj2={"name":"yogesh"}
    assert obj1 in l1
    assert obj2 in l1

def test_pour_to_list_when_source_is_greater_than_target():
    l1 = [{"place": "pune"}]
    l2=[{"name":"atmaram"},{"name":"yogesh"}]
    Context.pour_to_list(l1,l2)
    obj1={"name":"atmaram","place":"pune"}
    obj2={"name":"yogesh"}
    assert obj1 in l1
    assert obj2 in l1
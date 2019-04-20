import pytest
from journeypy.template.dsl import text,string,strExp,var
from journeypy.template.data.runtime.Context import Context
from journeypy.template.data.value.Values import StringHolder
from journeypy.template.io.IOs import MockIO
def test_process_method_when_value_in_context():
    context=Context()
    strHolder=StringHolder()
    strHolder.value=""
    mockIO=MockIO("123",strHolder)
    template=text(string("Hello"),strExp(var("name")))
    context.currentContext["name"]="Atmaram"
    assert template.process(context,mockIO).value == "HelloAtmaram","test failed"
    assert strHolder.value=="","test failed"

def test_process_method_when_value_not_in_context():
    context=Context()
    strHolder=StringHolder()
    strHolder.value=""
    mockIO=MockIO("Atmaram",strHolder)
    template=text(string("Hello"),strExp(var("name").ofType(str)))
    assert template.process(context,mockIO).value == "HelloAtmaram","test failed"
    assert strHolder.value=="Please provide value for name of type String\n","test failed"
from journeypy.template.dsl import text,string,strExp,var
from journeypy.core.data.runtime.Context import Context
from journeypy.core.data.value.Values import StringHolder
from journeypy.core.io.IOs import mock_consoleio
def test_process_method_when_value_in_context(capsys):
    context=Context()
    mockIO=mock_consoleio("123")
    template=text(string("Hello"),strExp(var("name")))
    context.currentContext["name"]="Atmaram"
    assert template.process(context,mockIO).value == "HelloAtmaram","test failed"
    out, err = capsys.readouterr()
    assert out=="","test failed"

def test_process_method_when_value_not_in_context(capsys):
    context = Context()
    mockIO=mock_consoleio("Atmaram")
    template = text(string("Hello"),strExp(var("name").ofType(str)))
    assert template.process(context,mockIO).value == "HelloAtmaram","test failed"
    out, err = capsys.readouterr()
    assert out=="Please provide value for name of type String\n","test failed"
from journeypy.template.dsl import text,string,str_exp,var
from journeypy.core.data.runtime import Context
from journeypy.core.io import mock_console_io


def test_process_method_when_value_in_context(capsys):
    context = Context()
    mock_io = mock_console_io("123")
    template = text(string("Hello"), str_exp(var("name")))
    context.currentContext["name"] = "Atmaram"
    assert template.process(context,mock_io).value == "HelloAtmaram", "test failed"
    out, err = capsys.readouterr()
    assert out == "", "test failed"


def test_process_method_when_value_not_in_context(capsys):
    context = Context()
    mock_io = mock_console_io("Atmaram")
    template = text(string("Hello"), str_exp(var("name").of_type(str)))
    assert template.process(context, mock_io).value == "HelloAtmaram", "test failed"
    out, err = capsys.readouterr()
    assert out == "Please provide value for name of type String\n", "test failed"

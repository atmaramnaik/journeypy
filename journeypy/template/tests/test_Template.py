from journeypy.template import Template
from journeypy.core.data.runtime import Context
from journeypy.core.io import mock_console_io
from journeypy.core.data.variable import MapVariable


def test_process_method():
    context = Context()
    template = Template()
    mock_io = mock_console_io('123')
    assert template.process(context, mock_io).value is None, "test failed"


def test_get_required_variables_method():
    context = Context()
    template = Template()
    mock_io = mock_console_io('123')
    val = template.get_required_variables(context, mock_io)
    assert type(val) == MapVariable
    assert len(val.variable_map) == 0


def test_get_required_variables_method_when_io_none():
    context = Context()
    template = Template()
    val = template.get_required_variables(context, None)
    assert type(val) == MapVariable
    assert len(val.variable_map) == 0

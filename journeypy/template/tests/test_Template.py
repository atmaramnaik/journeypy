from journeypy.template import Template
from journeypy.core.data.runtime import Context
from journeypy.core.io import mock_console_io


def test_process_method():
    context = Context()
    template = Template()
    mock_io = mock_console_io('123')
    assert template.process(context, mock_io).value is None, "test failed"

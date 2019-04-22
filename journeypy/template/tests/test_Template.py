from journeypy.template.Template import Template
from journeypy.core.data.runtime.Context import Context
from journeypy.core.io.IOs import mock_console_io


def test_process_method():
    context = Context()
    template = Template()
    mock_io = mock_console_io('123')
    assert template.process(context, mock_io).value is None, "test failed"

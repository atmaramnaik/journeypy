import pytest
from journeypy.template.template.Template import Template
from journeypy.template.data.runtime.Context import Context
from journeypy.template.io.IOs import MockIO
from journeypy.template.data.value.Values import StringHolder
def test_process_method():
    context=Context()
    template=Template()
    strHolder=StringHolder()
    strHolder.value=""
    mockIO = MockIO('123',strHolder)
    assert template.process(context,mockIO).value == None,"test failed"
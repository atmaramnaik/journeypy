from journeypy.template.Template import Template
from journeypy.core.data.runtime.Context import Context
from journeypy.core.io.IOs import MockIO
from journeypy.core.data.value.Values import StringHolder
def test_process_method():
    context=Context()
    template=Template()
    strHolder=StringHolder()
    strHolder.value=""
    mockIO = MockIO('123',strHolder)
    assert template.process(context,mockIO).value == None,"test failed"
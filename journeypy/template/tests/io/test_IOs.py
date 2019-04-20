from journeypy.template.io.IOs import ConsoleWriter
from journeypy.template.io.IOs import ConsoleReader
from journeypy.template.io.IOs import ConsoleIO
from journeypy.template.io.IOs import MockOut
from journeypy.template.io.IOs import MockIn
from journeypy.template.io.IOs import MockIO
from journeypy.template.data.value.Values import StringHolder,IntegerHolder
def test_console_writer_write_string_method():
    writer = ConsoleWriter()
    strHolder=StringHolder()
    strHolder.value=""
    out=MockOut(strHolder)
    writer.out=out
    writer.write_string("Hello")
    assert strHolder.value=="Hello","test failed"

def test_console_writer_write_obj_method():
    writer = ConsoleWriter()
    strHolder = StringHolder()
    strHolder.value = ""
    out=MockOut(strHolder)
    writer.out=out
    intHolder=IntegerHolder()
    intHolder.de_serialize("123")
    writer.write_data(intHolder)
    assert strHolder.value=="123","test failed"

def test_console_reader_read_method_for_integer():
    strHolder = StringHolder()
    strHolder.value = ""
    mockio = MockIO(input="123", output=strHolder)
    obj = mockio.reader.read(IntegerHolder)
    assert obj.value==123,"test failed"
    assert strHolder.value =='',"test failed"

def test_console_reader_read_method_for_string():
    strHolder = StringHolder()
    strHolder.value = ""
    mockio = MockIO(input="123", output=strHolder)
    obj=mockio.reader.read(StringHolder)
    assert obj.value=='123',"test failed"
    assert strHolder.value =='',"test failed"


from journeypy.core.io.IOs import ConsoleWriter, ConsoleIO, MockIn
from journeypy.core.io.IOs import mock_consoleio
from journeypy.core.data.value.Values import StringHolder,IntegerHolder

def test_console_writer_write_string_method(capsys):
    writer = ConsoleWriter()
    writer.write_string("Hello")
    out, err = capsys.readouterr()
    assert out == "Hello", "test failed"


def test_console_writer_write_obj_method(capsys):
    writer = ConsoleWriter()
    intHolder=IntegerHolder()
    intHolder.de_serialize("123")
    writer.write_data(intHolder)
    out, err = capsys.readouterr()
    assert out == "123", "test failed"


def test_console_reader_read_method_for_integer(capsys):
    mockio = mock_consoleio(input="123")
    obj = mockio.reader.read(IntegerHolder)
    assert obj.value == 123, "test failed"
    out, err = capsys.readouterr()
    assert out == '', "test failed"


def test_console_reader_read_method_for_string(capsys):
    mockio = mock_consoleio(input="123")
    obj=mockio.reader.read(StringHolder)
    out, err = capsys.readouterr()
    assert obj.value == '123', "test failed"
    assert out == '', "test failed"


def test_console_io_writer_write_data(capsys):
    io = ConsoleIO()
    int_holder = IntegerHolder()
    int_holder.de_serialize("123")
    io.writer.write_data(int_holder)
    out, err = capsys.readouterr()
    assert out == '123', "test failed"


def test_console_io_writer_write_string(capsys):
    io = ConsoleIO()
    io.writer.write_string("Hello")
    out, err = capsys.readouterr()
    assert out == 'Hello', "test failed"


def test_console_io_reader_read(monkeypatch):
    io = ConsoleIO()
    mock_in = MockIn("123")
    io.reader.sin = mock_in
    int_holder = io.reader.read(IntegerHolder)
    assert int_holder.value == 123, "test failed"

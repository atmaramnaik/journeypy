import sys
from journeypy.core.data.value.Values import ValueHolder, StringHolder


class Reader(object):
    def read(self, data_type):
        pass

    def get_writer(self):
        pass

    def set_writer(self, writer):
        pass

    def start_reading(self):
        pass

    def done_reading(self):
        pass

    def is_reading(self):
        pass


class Writer(object):

    def write_data(self, obj):
        pass

    def write_string(self, string):
        pass

    def get_reader(self):
        pass

    def set_reader(self, reader):
        pass

    def start_writing(self):
        pass

    def done_writing(self):
        pass

    def is_writing(self):
        pass


class IO(object):
    def __init__(self, writer, reader):
        self.writer = writer
        self.reader = reader
        self.writer.set_reader(self.reader)
        self.reader.set_writer(self.writer)


class ConsoleWriter(Writer):

    def write_data(self,obj):
        if isinstance(obj, ValueHolder):
            sys.stdout.write(obj.serialize())

    def write_string(self, string):
        sys.stdout.write(string)

    def get_reader(self):
        return self.reader

    def set_reader(self, reader):
        self.reader = reader

    def start_writing(self):
        pass

    def done_writing(self):
        pass

    def is_writing(self):
        return False


class ConsoleReader(Reader):
    sin = sys.stdin

    def read(self, data_value_holder_type):
        obj = data_value_holder_type()
        obj.de_serialize(self.sin.readline())
        return obj

    def get_writer(self):
        return self.writer

    def set_writer(self,writer):
        self.writer = writer

    def start_reading(self):
        pass

    def done_reading(self):
        pass

    def is_reading(self):
        return False;


class ConsoleIO(IO):
    def __init__(self, writer=ConsoleWriter(), reader=ConsoleReader()):
        super(ConsoleIO, self).__init__(writer, reader)


class MockIn(object):
    str = ''

    def __init__(self,str):
        self.str = str

    def readline(self):
        return self.str


def mock_console_io(input_data=''):
    mock_in = MockIn(input_data)
    writer = ConsoleWriter()
    reader = ConsoleReader()
    reader.sin = mock_in
    return ConsoleIO(writer,reader)

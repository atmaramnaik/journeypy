import sys
from journeypy.journey import SequenceStep, LoopStep
from journeypy.core.data.runtime import Context
from journeypy.template.dsl import *
from journeypy.core.io import mock_console_io


def test_sequence_step_call(capsys):
    def step1(context, io):
        sys.stdout.write("Hello")

    def step2(context, io):
        sys.stdout.write("World")

    ss = SequenceStep().with_step(step1).with_step(step2)

    ss(None, None)
    out, err = capsys.readouterr()
    assert out == "HelloWorld"


def test_loop_step_call_when_data_present(capsys):
    context = Context()
    io = mock_console_io("Hello")
    context.currentContext["names"] = [{"name":"Atmaram"}, {"name": "Yogesh"}]

    def step1(context_step, io_step):
        template = text(str_exp(var("name")))
        template.process(context_step, io_step)

    loop_step = LoopStep("names",step1)

    loop_step(context, None)
    out, err = capsys.readouterr()
    assert out == ""


def test_loop_step_call_when_data_not_present(capsys):
    context = Context()
    io = mock_console_io("2\nHello\nWorld\n")

    def step1(context_step, io_step):
        template = text(str_exp(var("name").of_type(str)))
        template.process(context_step, io_step)

    loop_step = LoopStep("names", step1)

    loop_step(context, io)
    out, err = capsys.readouterr()
    assert out == "Enter size of list as IntegerPlease provide value for name of type String\nPlease provide value for name of type String\n"

import sys
from journeypy.journey import Journey, JourneyManager
from journeypy.core.data.runtime import Context
from journeypy.template.dsl import *
from journeypy.core.io import mock_console_io


def step1(step_context, io_step):
    sys.stdout.write("Hello")


def step2(step_context, io_step):
    sys.stdout.write("World")


def test_journey_manager_start_multiple_matches(capsys):
    io = mock_console_io("1\n")

    journey1 = Journey(step1).named("Hello World").with_step(step2).responding(text(string("Done Hello")))
    journey2 = Journey(step1).named("Hello Keep Rotating").with_step(step2).responding(text(string("Done Hello")))

    journey_manager = JourneyManager()
    journey_manager.add(journey1)
    journey_manager.add(journey2)
    journey_manager.start("Hello", io)
    out, err = capsys.readouterr()
    assert out == 'What do you want to do: \n1) Hello World\n2) Hello Keep Rotating\nEnter Selection as Number: I think you want to Hello World\nHelloWorldDone Hello\n'


def test_journey_manager_start_single_match(capsys):
    io = mock_console_io("")

    journey1 = Journey(step1).named("Hello World").with_step(step2).responding(text(string("Done Hello")))
    journey2 = Journey(step1).named("Hello Keep Rotating").with_step(step2).responding(text(string("Done Hello")))

    journey_manager = JourneyManager()
    journey_manager.add(journey1)
    journey_manager.add(journey2)
    journey_manager.start("keep", io)
    out, err = capsys.readouterr()
    assert out == 'I think you want to Hello Keep Rotating\nHelloWorldDone Hello\n'


def test_journey_execute(capsys):
    context = Context()
    io = mock_console_io("2\nHello\nWorld\n")
    journey = Journey().named("Hello World").with_step(step1).with_step(step2).responding(text(string("Done Hello")))
    journey.execute(context, io)
    out, err = capsys.readouterr()
    assert out == 'I think you want to Hello World\nHelloWorldDone Hello\n'


def test_journey_execute_initialized_with_step(capsys):
    context = Context()
    io = mock_console_io("2\nHello\nWorld\n")

    journey = Journey(step1).named("Hello World").with_step(step2).responding(text(string("Done Hello")))

    journey.execute(context, io)
    out, err = capsys.readouterr()
    assert out == 'I think you want to Hello World\nHelloWorldDone Hello\n'




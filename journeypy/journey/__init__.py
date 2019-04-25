from journeypy.core.data.value import IntegerHolder
from journeypy.core.data.runtime import Context
import sys

class SequenceStep(list):

    def with_step(self, step):
        self.append(step)
        return self

    def __call__(self, *args, **kwargs):
        for step in self:
            step(*args, **kwargs)


class LoopStep(object):

    def __init__(self, variable, step):
        self.variable = variable
        self.step = step

    def do_operation(self, context, io):
        lst = context.get(self.variable)
        if issubclass(type(lst), list):
            for i in range(len(lst)):
                self.step(context.get_from_list_item(self.variable,i), io)

    def ensure(self, context, io):
        try:
            context.get(self.variable)
        except KeyError as e:
            data_list = []
            io.writer.write_string("Enter size of list as Integer")
            int_holder = io.reader.read(IntegerHolder)

            for i in range(int_holder.value):
                data_list.append({})
            data_to_add = {self.variable: data_list}
            context.pour(data_to_add)

    def __call__(self, *args, **kwargs):
        self.ensure(*args, **kwargs)
        self.do_operation(*args, **kwargs)


class Journey(SequenceStep):
    def __init__(self, step=None):
        self.name = ''
        self.response = None
        if step is not None:
            self.append(step)

    def named(self, name):
        self.name = name
        return self

    def responding(self, text_template):
        self.response = text_template
        return self

    def execute(self, context, io):
        io.writer.write_string("I think you want to "+self.name+"\n")
        self(context, io)
        if self.response is not None:
            final_response = self.response.process(context, io).value
            io.writer.write_string(final_response+"\n")

        io.writer.done_writing()


class JourneyManager(object):
    def __init__(self):
        self.js = []

    def add(self, journey):
        self.js.append(journey)
        return self

    def __match(self, input_string, io):
        splited_input = input_string.split(" ")

        def map_fun(journey):
            rank = 0
            for word in splited_input:
                if word.lower() in journey.name.lower():
                    rank += 1
            return rank
        ranks = list(map(map_fun, self.js))

        top_rank = max(ranks)
        indices = [i for i, x in enumerate(ranks) if x == top_rank]
        filtered_journey = [self.js[i] for i in indices]

        int_command = 0
        if len(filtered_journey) > 1:
            io.writer.write_string("What do you want to do: \n")
            for i in range(len(filtered_journey)):
                io.writer.write_string(str(i + 1) + ") "+filtered_journey[i].name + "\n")
            io.writer.write_string("Enter Selection as Number: ")
            int_command = io.reader.read(IntegerHolder).value - 1
        if len(filtered_journey) == 0:
            io.writer.write_string("No Matching Journey\n")
            return None

        return filtered_journey[int_command]

    def start(self, input_string, io):
        journey = self.__match(input_string, io)
        if journey is not None:
            journey.execute(Context(), io)




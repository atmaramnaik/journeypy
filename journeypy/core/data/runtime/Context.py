class Context(object):
    currentContext = {}

    def __init__(self):
        self.currentContext = {}
        self.ref=self.currentContext

    def get(self, key):
        return self.currentContext[key]

    def pour(self, data):
        Context.pour_to(self.ref, data)
        Context.pour_to(self.currentContext, data)

    @staticmethod
    def __pour_to_map(map_target, map_source):
        for key in map_source:
            if key in map_target:
                Context.pour_to(map_target[key],map_source[key])
            else:
                map_target[key]=map_source[key]

    @staticmethod
    def __pour_to_list(list_target, list_source):
        if len(list_target)>len(list_source):
            for i in range(len(list_source)):
                Context.pour_to(list_target[i],list_source[i])
        else:
            for i in range(len(list_target)):
                Context.pour_to(list_target[i],list_source[i])

            for i in range(len(list_target),len(list_source)):
                list_target.append(list_source[i])

    @staticmethod
    def pour_to(target, source):
        if isinstance(target,dict) and isinstance(source,dict):
            Context.__pour_to_map(target,source)
        elif isinstance(target,list) and isinstance(source,list):
            Context.__pour_to_list(target,source)



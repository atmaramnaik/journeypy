import json
class Serializable(object):
    def de_serialize(self,str):
        pass

    def serialize(self):
        pass


class ValueHolderEntry(object):
    def __init__(self, t, vh):
        self.t = t
        self.vh = vh

    def __eq__(self, other):
        if self.t == other.t:
            return True
        elif issubclass(self.t, other.t) or issubclass(other.t,self.t):
            return False
        else:
            return True

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if issubclass(self.t,other.t):
            return True
        return False

    def __le__(self, other):
        if self < other or self == other:
            return True
        return False

    def __gt__(self, other):
        if issubclass(other.t,self.t):
            return True
        return False

    def __ge__(self, other):
        if self > other or self == other:
            return True
        return False


class ValueHolder(Serializable):
    type = None
    value = None
    __valueHolderList = []

    def __str__(self):
        return self.serialize()

    def __add__(self, other):
        if isinstance(other, str):
            return str(self) + other
        else:
            return str(self) + str(other)

    def __radd__(self, other):
        if isinstance(other,str):
            return other + str(self)
        else:
            return str(other)+str(self)


    @staticmethod
    def get_appropriate_value_holder(typeProvided):
        for vhe in ValueHolder.__valueHolderList:
            if issubclass(typeProvided,vhe.t):
                return vhe.vh

    @staticmethod
    def get_new_value_holder_for(data):
        valueholder=ValueHolder.get_appropriate_value_holder(type(data))()
        valueholder.value=data
        return valueholder

    @classmethod
    def register(cls,type):
        def real_decorator(scls):
            ValueHolder.__valueHolderList.append(ValueHolderEntry(type, scls))
            ValueHolder.__valueHolderList.sort()
            return scls

        return real_decorator


@ValueHolder.register(int)
class IntegerHolder(ValueHolder):
    def __init__(self):
        self.value=None

    def de_serialize(self, str):
        self.value=int(str)

    def serialize(self):
        return str(self.value)

    def __add__(self, other):
        if isinstance(other,str):
            return str(self) + other
        elif isinstance(other,IntegerHolder):
            retHolder=IntegerHolder()
            retHolder.value=self.value+other.value
            return retHolder
        elif isinstance(other,int):
            retHolder = IntegerHolder()
            retHolder.value = self.value + other
            return retHolder
        else:
            return str(self) + str(other)

    def __radd__(self, other):
        if isinstance(other,str):
            return other + str(self)
        elif isinstance(other,IntegerHolder):
            retHolder=IntegerHolder()
            retHolder.value=self.value+other.value
            return retHolder
        elif isinstance(other,int):
            retHolder = IntegerHolder()
            retHolder.value = self.value + other
            return retHolder
        else:
            return str(other) + str(self)


@ValueHolder.register(str)
class StringHolder(ValueHolder):

    def __init__(self):
        self.value = None

    def de_serialize(self,string):
        self.value = string

    def serialize(self):
        return self.value


@ValueHolder.register(type(None))
class NoneHolder(ValueHolder):
    def __init__(self):
        self.value = None

    def de_serialize(self, string):
        self.value = None

    def serialize(self):
        return self.value


@ValueHolder.register(object)
class ObjectHolder(ValueHolder):
    def __init__(self):
        self.value = None

    def de_serialize(self, string):
        self.value = json.load(string)

    def serialize(self):
        return json.dumps(self.value)

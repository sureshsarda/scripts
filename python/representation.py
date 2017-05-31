import logging
import logging.handlers as handlers

class Foo(object):
    def __init__(self, val):
        self._value = val

    def __repr__(self):
        return '{0}-FooObject'.format(self._value)

    def __str__(self):
        return 'FooObject: [value: {0}]'.format(self._value)


foo = Foo(11)
print(foo)
print(repr(foo))
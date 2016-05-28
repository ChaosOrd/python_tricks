# Metaclass can also alter the behavior of a class when the object is created


class MyMeta(type):
    def __call__(cls, *args):
        print '__call__ of ', str(cls)
        print '__call__ *args=', str(args)
        return type.__call__(cls, *args)


class MyKlass(object):
    __metaclass__ = MyMeta

    def __init__(self, a, b):
        print 'MyKlass object with a=%s, b=%s' % (a, b)


print 'gonna create foo now...'
foo = MyKlass(1, 2)

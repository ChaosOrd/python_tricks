# The class of a class is called a metaclass
# Here is how you define a custom metaclass


class MyMeta(type):
    def __new__(mcs, name, bases, dct):
        print '-----------------------------------'
        print "Allocating memory for class", name
        print mcs
        print bases
        print dct
        return super(MyMeta, mcs).__new__(mcs, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print '-----------------------------------'
        print "Initializing class", name
        print cls
        print bases
        print dct
        super(MyMeta, cls).__init__(name, bases, dct)


class MyKlass(object):

    __metaclass__ = MyMeta

    def foo(self, param):
        pass

    some_attr = 2
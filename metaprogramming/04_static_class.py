
class NoInstances(type):

    def __call__(cls, *args, **kwargs):
        raise TypeError("No instances are allowed")


class MyStaticClass(object):

    __metaclass__ = NoInstances

    @staticmethod
    def do_some_stuff():
        print("Some stuff")


if __name__ == '__main__':
    MyStaticClass.do_some_stuff()
    obj = MyStaticClass()

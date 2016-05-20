
class Singleton(type):

    def __init__(cls, what, bases, attrs_dict):
        cls.__instance = None
        super(Singleton, cls).__init__(what, bases, attrs_dict)

    def __call__(cls, *args):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__call__(*args)
            return cls.__instance
        else:
            return cls.__instance


class MyKlass(object):
    __metaclass__ = Singleton

if __name__ == '__main__':
    obj = MyKlass()
    second_obj = MyKlass()
    obj.name = "foo"
    second_obj.name = "bar"
    print(obj.name)
    print(second_obj.name)
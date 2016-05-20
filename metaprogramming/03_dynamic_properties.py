
class AttributeMultiplier(type):
    def __init__(cls, what, bases, attrs_dict):

        for attr in attrs_dict:
            for idx in range(1, 4):
                setattr(cls, '{}_{}'.format(attr, idx), attrs_dict[attr])

        super(AttributeMultiplier, cls).__init__(what, bases, attrs_dict)


class MyKlass(object):

    __metaclass__ =  AttributeMultiplier

    def some_method(self):
        print("Inside some_method")


if __name__ == '__main__':
    obj = MyKlass()
    obj.some_method_1()
    obj.some_method_2()
    obj.some_method_3()
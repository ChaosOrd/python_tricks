
if __name__ == '__main__':

    my_dynamic_class = type('DynamicClass', (object,), {'x': 1, 'y': 'bla'})
    klass = my_dynamic_class()
    print(klass)
    print(klass.x)
    print(klass.y)


# class MyClass(object):
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

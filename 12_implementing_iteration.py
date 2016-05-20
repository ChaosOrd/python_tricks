
class MyList(object):

    def __init__(self):
        self.__my_list = range(10)

    def __iterate_my_list(self):
        for list_item in self.__my_list:
            yield list_item

    def __iter__(self):
        return self.__iterate_my_list()


if __name__ == '__main__':
    my_list = MyList()
    for item in my_list:
        print(item)

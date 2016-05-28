

def add_2(list_):
    for item in list_:
        yield item + 2


def mult_3(list_):
    for item in list_:
        yield item * 3


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    result = mult_3(add_2(my_list))
    print list(result)

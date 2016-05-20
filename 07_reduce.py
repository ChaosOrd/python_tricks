
if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = reduce(lambda x, y: x + y, my_list)/len(my_list)
    print(result)

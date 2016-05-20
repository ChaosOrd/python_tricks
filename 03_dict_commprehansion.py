
if __name__ == '__main__':
    tuples = [(1, 'a'), (2, 'b'), (3, 'c')]
    my_dict = {item[0]: item[1] for item in tuples}
    print(my_dict)
    # print(dict(tuples))


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(filter(lambda x: x % 2 == 0, my_list))
    bit_array = [x for x in my_list if x > 3]
    print(bit_array)
    print(any(bit_array))
    print(all(bit_array))

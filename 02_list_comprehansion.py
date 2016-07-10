
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]

    multiplied_arr = []
    for item in arr:
        if item != 2:
            multiplied_arr.append(item*item)
    print(multiplied_arr)






























    multiplied_arr = [item * item for item in arr if item != 2]
    print(multiplied_arr)

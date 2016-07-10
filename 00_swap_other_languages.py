# How do you swap the values of 2 variables without using the third?









































if __name__ == '__main__':
    x = 5
    y = 15
    x = x + y
    y = x - y
    x = x - y
    print('X is {}'.format(x))
    print('Y is {}'.format(y))
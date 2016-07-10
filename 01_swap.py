# How to do it pythonic way?

if __name__ == '__main__':
    x = 10
    y = 15

    x, y = y, x
    print('X is {}, Y is {}'.format(x, y))

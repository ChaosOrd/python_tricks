# Generators are lazy evaluated functions


def frange(start, stop, increment):
    x = start
    while x <= stop:
        yield x
        x += increment

if __name__ == '__main__':
    numbers = frange(3, 25, 3)
    for num in numbers:
        print(num)

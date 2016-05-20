from itertools import izip, chain

if __name__ == '__main__':
    first_list = [1, 2, 3, 4, 5]
    second_list = ['a', 'b', 'c', 'd', 'e']
    zipped = zip(first_list, second_list)
    print('Zipped:')
    for number, letter in zipped:
        print('The number is: {}, The letter is: {}'.format(number, letter))

    print('IZipped')
    izipped = izip(first_list, second_list)
    for number, letter in izipped:
        print('The number is: {}, The letter is: {}'.format(number, letter))

    print("Chained")
    chained = chain(first_list, second_list)
    for item in chained:
        print('The item is {}'.format(item))

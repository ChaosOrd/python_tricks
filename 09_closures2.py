
def do_complicated_stuff(callback):
    print("Doing some complicated stuff")
    callback()


if __name__ == '__main__':

    def callback_wrapper(call_number):
        def wrapped():
            print ("Number {} complicated stuff finished".format(call_number))
        return wrapped

    do_complicated_stuff(callback_wrapper(1))
    do_complicated_stuff(callback_wrapper(2))
    do_complicated_stuff(callback_wrapper(3))

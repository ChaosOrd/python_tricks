from threading import Thread

# Closures can also be used


def do_complicated_stuff(callback):
    print("Doing some complicated stuff")
    callback()


def start_doing_complicated_stuff(callback):
    thread = Thread(target=do_complicated_stuff, args=(callback,))
    thread.start()


if __name__ == '__main__':

    def callback_wrapper(call_number):
        def wrapped():
            print ("Number {} complicated stuff finished".format(call_number))
        return wrapped

    start_doing_complicated_stuff(callback_wrapper(1))
    start_doing_complicated_stuff(callback_wrapper(2))
    start_doing_complicated_stuff(callback_wrapper(3))

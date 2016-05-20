
def mult_closure(x):
    def wrapped(y):
        return x * y

    return wrapped

mult_by_three = mult_closure(3)
print(mult_by_three(5))

# When to use closure?

# - Great to dry up code. Add syntactic sugar

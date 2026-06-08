def do_stuff():
    print("Hello World")
    return

def add(a,b):
    c = a + b
    return c

def my_math(a,b):
    c = a + b
    d = a - b
    e = a * b
    if b != 0:
        f = a / b
    else:
        f = None
    return c, d, e, f

def my_math_list(a,b):
    c = a + b
    d = a - b
    e = a * b
    if b != 0:
        f = a / b
    else:
        f = None
    return_list = [c,d,e,f]
    return return_list

# main program starts here!
if __name__ == "__main__":
    # function that takes no arguments and returns nothing
    do_stuff()

    # function that takes arguments and returns a value
    x = 4
    y = 7
    z = add(x,y)
    print(z)

    # function that returns multiple values
    t, u, v, w = my_math(x,y)
    print(t, u, v, w)

    # function that returns a list
    r_list = my_math_list(x,y)
    print(r_list)



def decorator_func(func):
    def wrapper_func():
        print("Wrapper function worked")
        return func
    print("decorator function worked")
    return wrapper_func()


# def show():
#     print("Show worked")
#
#
# decorator_show = decorator_func(show)
#
# decorator_show()

@decorator_func
def display():
    print("display worked")


display()




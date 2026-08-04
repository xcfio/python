def dash(fn):
    def wrapper():
        print("-------------------------------")
        fn()
        print("-------------------------------")

    return wrapper


@dash
def hi():
    print("Hello world")


hi()

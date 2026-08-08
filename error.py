try:
    x = 1 / 0
    print(x)
except ZeroDivisionError as zd:
    print("Zero Division Error")
except BaseException as error:
    print(error)
else:
    print("this code has no error")
finally:
    print("this code always run")

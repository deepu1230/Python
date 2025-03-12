def throw_custom_exception():
    try:
        a = 10
        b = 0
        print(a / b)
    except ZeroDivisionError:
        raise Exception("Custom exception message")

try:
    throw_custom_exception()
except Exception as e:
    print(e)


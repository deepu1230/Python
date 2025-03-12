def handle_arithmetic_exception():
    try:
        a = 10
        b = 0
        print(a / b)
    except ZeroDivisionError:
        print("Arithmetic exception handled")

handle_arithmetic_exception()
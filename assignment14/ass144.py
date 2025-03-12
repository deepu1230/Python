def handle_exceptions():
    try:
        a = 10
        b = "hello"
        print(a / b)
    except ZeroDivisionError:
        print("Arithmetic exception handled")
    except TypeError:
        print("Type exception handled")

handle_exceptions()
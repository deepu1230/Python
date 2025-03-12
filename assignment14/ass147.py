def handle_exceptions():
    try:
        a = 10
        b = 0
        print(a / b)
    except ZeroDivisionError:
        print("Arithmetic exception handled")
    finally:
        print("Finally block executed")

handle_exceptions()


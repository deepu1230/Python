def generate_io_exception():
    try:
        with open("non_writable_file.txt", "w") as file:
            file.write("Hello, World!")
    except IOError:
        print("I/O exception handled")

generate_io_exception()


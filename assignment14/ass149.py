def generate_file_not_found_exception():
    try:
        with open("non_existent_file.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found exception handled")

generate_file_not_found_exception()

def read_file_just_to_index(filename, index):
    with open(filename, 'r') as file:
        file.seek(index)
        print(file.read())

read_file_just_to_index('example.txt', 10)
def read_file_stream(filename):
    with open(filename, 'r') as file:
        while True:
            chunk = file.read(1024)
            if not chunk:
                break
            print(chunk)

read_file_stream('example.txt')


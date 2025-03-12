def read_file_stream_random_access(filename):
    with open(filename, 'r') as file:
        file.seek(10)  # Seek to 10th byte
        print(file.read(10))  # Read 10 bytes from current position

read_file_stream_random_access('example.txt')

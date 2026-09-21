# file Not Found
try:
    with open('file_notfound.txt') as file:
        file.read()
except FileNotFoundError:
    print('File is not found here')
finally:
    print('Finished handling exception')
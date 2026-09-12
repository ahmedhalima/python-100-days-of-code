file = open('my_file.txt')
contents = file.read()
print(contents)
file.close()

with open('my_file.txt', 'r+') as my_file:
    content = my_file.read()
    print(content)
    new_content = '\n this is a new content'
    my_file.write(new_content)
    content = my_file.read()
    print(content)
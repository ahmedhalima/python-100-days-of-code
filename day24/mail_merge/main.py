def create_file(file_name, contents):
    file_name = file_name.lower().replace(' ', '_')
    with open(f'./Output/ReadyToSend/{file_name}', 'w') as file:
        file.write(contents)

# Create a letter using starting_letter.txt
with open('./Input/Letters/starting_letter.txt') as starting_letter:
    starting_template = starting_letter.read()
with open('./Input/Names/invited_names.txt') as starting_names:
    for name in starting_names.readlines():
        # replace the name in template
        name = name.strip()
        new_template = starting_template.replace('[name]', name)

        filename = f'letter_for_{name}.txt'
        create_file(filename, new_template)
        print(f'File created for {name}')
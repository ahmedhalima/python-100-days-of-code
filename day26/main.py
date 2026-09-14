# nato alphabet
import pandas

csv_list = pandas.read_csv('nato_phonetic_alphabet.csv')
phonetic_list = {row.letter:row.code for (key, row) in csv_list.iterrows()}

user_input = input('Enter your name\n')
user_input_list = {alpha.upper():phonetic_list[alpha.upper()] for alpha in user_input}

print(user_input_list)
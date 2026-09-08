from prettytable import PrettyTable

table = PrettyTable()
table.add_column("ID", [1,2,3])
table.add_column("Name", ['Ahmed','Shimaa','Mohammed'])
table.add_column("Age", [35,31,5])

print(table)
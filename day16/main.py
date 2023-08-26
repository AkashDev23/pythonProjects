from prettytable import PrettyTable
table=PrettyTable()
print (table)
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print (table)
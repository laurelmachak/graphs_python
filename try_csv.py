import csv


pokemon_file = open('Pokemon.csv')
# create a Reader object:
pokemon_reader = csv.reader(pokemon_file)
# create a list of lists:
pokemon_data = list(pokemon_reader)
print(pokemon_data[0][1])

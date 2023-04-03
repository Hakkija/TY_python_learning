def read_recipes(filename):
    with open(filename, 'r') as file:
        recipes = [line.strip().split(',') for line in file]
    return recipes


recipes = read_recipes('recipes.txt')

print("Recipes that require strawberries and sugar:")
for recipe in recipes:
    if 'strawberries' in recipe and 'sugar' in recipe:
        print(', '.join(recipe))

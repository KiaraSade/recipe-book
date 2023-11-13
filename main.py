# main.py

def view_recipes():
    with open('recipes.txt', 'r') as file:
        recipes = file.read()
        print(recipes)

def add_recipe():
    recipe_name = input("Enter recipe name: ")
    ingredients = input("Enter ingredients (comma-separated): ").split(', ')
    instructions = input("Enter instructions (one step per line, end with 'end'): ")
    
    with open('recipes.txt', 'a') as file:
        file.write(f"\n[{recipe_name}]\n")
        file.write("Ingredients:\n")
        for ingredient in ingredients:
            file.write(f"- {ingredient}\n")
        file.write("Instructions:\n")
        file.write(f"{instructions}\n")

# Test the program
view_recipes()
add_recipe()
view_recipes()

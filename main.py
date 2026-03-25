import re




def name_validation(use_case, limit_number):
    while True:
        name = input(f"Enter {use_case} name: ")
        if  not 3 < len(name) < int(limit_number):
            print("Name must be between 3 and 50 characters long")
        elif not name.strip():
            print("Name cannot be empty or contain only spaces")
        elif not re.match(r"^(?=.*[A-Za-z])[A-Za-z0-9\s\-']+$", name):
            print("Invalid name: only letters, numbers, space, hyphen (-), apostrophe (') allowed, and must contain at least one letter")
        else:
            return name

def validate_ingredient_name():
    while True:
        return name_validation("ingredient", 30)

def validate_ingredient_quantity():
    while True:
        try:
            quantity = float(input("Enter the ingredient quantity: "))
            if quantity < 0 :
                print("Ingredient quantity must be greater than zero")
        except ValueError:
            print("Ingredient quantity must be an integer")
        else:
            if quantity.is_integer():
                quantity = int(quantity)
            return quantity

def unit_validation():
    unit_list = ["g", "kg", "ml", "l", "cup", "tbsp", "tsp", "piece"]
    while True:
        unit = input("Enter the ingredient unit: ")
        if unit not in unit_list:
            print("Ingredient unit must be one of: g, kg, ml, l, cup, tbsp, tsp or piece")
        else:
            return unit

def input_ingredient():
    ingredient_list = []
    name_list = []
    while True:
        print("If you would like to continue, please enter the ingredient else enter finish")
        ingredient_name = validate_ingredient_name()

        if ingredient_name == "finish":
            if 3 < len(ingredient_list) < 20:
                return ingredient_list
            print("Recipe should include 3 to 20 ingredients")
            continue

        if ingredient_name in name_list:
            if input(f"Ingredient {ingredient_name} already exists, would you like to overwrite it? [y/n]").lower() != "y":
                continue
        ingredient_tuple = (ingredient_name, validate_ingredient_quantity(), unit_validation())
        ingredient_list.append(ingredient_tuple)
        name_list.append(ingredient_name)


def cooking_time_validation():
    while True:
        try:
            hours = int(input("Enter the cooking time in hours: "))
            minutes = int(input("Enter the cooking time in minutes: "))
            if (hours == 0 and minutes <= 5) or (hours >= 12 and minutes > 0 ):
                print("Cooking time must be between 00.05 and 12.00 hours")
            elif hours < 0 or hours > 24 or minutes < 0 or minutes > 59:
                print("Enter a valid cooking time")
            else:
                return f"{hours:02}:{minutes:02}"
        except ValueError:
            print("Time must be consist of integers")

def category_selection():
    while True:
        category_list = ["BREAKFAST", "LUNCH", "DINNER", "DESSERT", "SNACK", "BEVERAGES"]
        user_input = input("Select from this category ('BREAKFAST', 'LUNCH', 'DINNER', 'DESSERT', 'SNACK', 'BEVERAGES') ").upper()

        if user_input in category_list:
            return user_input
        else:
            print("Invalid category")

def recipe_validation():

    name = name_validation("recipe", "50")
    ingredients = input_ingredient()
    cooking_time = cooking_time_validation()
    category = category_selection()
    print(f"""Recipe Validated Successfully
          Name: {name}
          Ingredients: len{ingredients}
          Category: {category}
          Cooking Time: {cooking_time}""")
    return name, ingredients, cooking_time, category

def generate_recipe_id(recipes):
    counter = 1
    while True:
        recipe_id = f"RCP{counter:03d}"
        if recipe_id not in recipes:
            return recipe_id
        counter += 1

def multiple_recipe_entry(recipes):
    number_of_recipies_added = 0
    while True:
        recipe_id = generate_recipe_id(recipes)
        name, ingredients, cooking_time, category = recipe_validation()
        recipes[recipe_id] = {"name": name, "ingredients": ingredients, "time": cooking_time, "category": category}
        number_of_recipies_added += 1
        if input("Would you like to add another recipe? [y/n]: ") == "n":
            return recipes
        else:
            continue

recipe = {'RCP001': {'name': 'Pizza',
                     'ingredients': [('flour', 500, 'g'), ('chicken', 250, 'g'), ('carrots', 4, 'piece'), ('milk', 50, 'ml')],
                     'time': '00:30',
                     'category': 'BREAKFAST'},
          'RCP002': {'name': 'Rice',
                     'ingredients': [('rice', 500, 'g'), ('salt', 5, 'g'), ('water', 1, 'l'), ('rampe', 1, 'piece')],
                     'time': '01:00',
                     'category': 'BREAKFAST'},
          'RCP003': {'name': 'Cake',
                     'ingredients': [('flour', 1, 'kg'), ('eggs', 5, 'piece'), ('butter', 1, 'kg'), ('sugar', 2, 'kg')],
                     'time': '05:00',
                     'category': 'DESSERT'},
          'RCP004': {'name': 'Pudding',
                     'ingredients': [('flour', 500, 'g'), ('honey', 500, 'ml'), ('eggs', 4, 'piece'), ('nuts', 5, 'g')],
                     'time': '02:45',
                     'category': 'DESSERT'},}

def single_recipe_display(recipes):
    try:
        check_in = int(input("What recipe would you like to check? RCP"))
        check_in = f"RCP{check_in:03d}"


        print(f"""
===================================================================
Recipe ID: {check_in}
Name: {recipes[check_in]["name"]}
Category: {recipes[check_in]["category"]}
Cooking Time: {recipes[check_in]["time"]}
------------------------------------------------------------------- 
Ingredients:""")
        for number, item in enumerate(recipes[check_in]["ingredients"], 1):
            ingredient, quantity, unit = item
            print(f"  {number}. {ingredient} - {quantity}{unit}")
        print(f"""
-------------------------------------------------------------------
Tags: 
===================================================================
        """.strip())
    except ValueError:
        print("Invalid input. Enter recipe number")

    except KeyError:
        print("Invalid input. Recipe number not found.")

def display_recipes(recipes):

    print(f"Total Recipies: {len(recipes)}")
    print("---------------------------------------")
    for recipe_id, data in recipes.items():
        print(f"{recipe_id}|{data['name']}|{data['category']}|{data['time']}")
    print("---------------------------------------")


def display_by_category(recipes):
    count = 0
    while True:
        user_prompt = input("Which category would you like to display? ").upper()
        for recipe_id, data in recipes.items():
            if data['category'] == user_prompt:
                print(f"{recipe_id}|{data['name']}|{data['time']}")
                count += 1
            else:
                print("Invalid input. Recipe category not found.")
                continue
        print(f"Found {count} {user_prompt} recipes")
        return False

multiple_recipe_entry(recipe)




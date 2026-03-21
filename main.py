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
            if not 3 < len(ingredient_list) < 20:
                print("Recipe should include 3 to 20 ingredients")
                continue
            else:
                return ingredient_list
        elif ingredient_name in name_list:
            confirmation = input(f"Ingredient {ingredient_name} already exists, would you like to overwrite it? [y/n]")
            if confirmation == "y":
                pass
            elif confirmation == "n":
                continue
        ingredient_quantity = validate_ingredient_quantity()
        ingredient_unit = unit_validation()
        ingredient_tuple = (ingredient_name, ingredient_quantity, ingredient_unit)
        ingredient_list.append(ingredient_tuple)
        name_list.append(ingredient_name)


def cooking_time_validation():
    while True:
        try:
            hours = int(input("Enter the cooking time in hours: "))
            minutes = int(input("Enter the cooking time in minutes: "))
            if (hours >= 0 and minutes <= 5) or (hours >= 12 and minutes > 0 ):
                print("Cooking time must be between 00.05 and 12.00 hours")
            elif hours < 0 or hours > 24 or minutes < 0 or minutes > 59:
                print("Enter a valid cooking time")
            else:
                if hours < 10 and minutes < 10:
                    return f"0{hours}:0{minutes}"
                elif hours < 10:
                    return f"0{hours}:{minutes}"
                elif minutes < 10:
                    return f"{hours}:0{minutes}"
                else:
                    return f"{hours}:{minutes}"
        except ValueError:
            print("Time must be consist of integers")

def category_selection():
    while True:
        category_list = ["BREAKFAST", "LUNCH", "DINNER", "DESSERT", "SNACK", "BEVERAGES"]
        user_input = input("Select from this category ('BREAKFAST', 'LUNCH', 'DINNER', 'DESSERT', 'SNACK', 'BEVERAGES') ")
        for category in category_list:
            if user_input == category.lower() or user_input == category.title():
                print("Category is case sensitive")
            elif user_input in category_list:
                return category
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

recipe_validation()
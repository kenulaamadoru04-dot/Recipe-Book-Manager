import re

def name_validation(use_case, limit_number):
    while True:
        name = input(f"Enter {use_case} name: ")
        if  not 3 < len(name) < limit_number:
            print("Name must be between 3 and 50 characters long")
        elif not name.strip():
            print("Name cannot be empty or contain only spaces")
        elif not re.match(r"^(?=.*[A-Za-z])[A-Za-z0-9\s\-']+$", name):
            print("Invalid name: only letters, numbers, space, hyphen (-), apostrophe (') allowed, and must contain at least one letter")
        else:
            return name

def validate_ingredient_name():
    while True:
        name_validation("ingredient", 30)


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
        print("If you would like to continue, please enter the ingredient else enter finished")
        ingredient_name = validate_ingredient_name()
        if ingredient_name == "finished":
            if not 3 <ingredient_list < 20:
                print("Recipe should include 3 to 20 ingredients")
                return False
        elif ingredient_name in name_list:
            confirmation = input(f"Ingredient {ingredient_name} already exists, would you like to overwrite it? [y/n]")
            if confirmation == "y":
                ingredient_quantity = validate_ingredient_quantity()
                ingredient_unit = unit_validation()
                ingredient_tuple = (ingredient_name, ingredient_quantity, ingredient_unit)
                ingredient_list.append(ingredient_tuple)
            elif confirmation == "n":
                input_ingredient()











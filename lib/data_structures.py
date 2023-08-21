spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = []
    for foods in spicy_foods:
        names.append(foods['name'])
    return names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spiciest_foods.append(food)
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        spice = "🌶" * food["heat_level"] 

        print(f"{name} ({cuisine}) | Heat Level: {spice}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    pass

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        spice = "🌶" * food["heat_level"] 

        if food["heat_level"] > 5:
            print(f"{name} ({cuisine}) | Heat Level: {spice}")
    pass

def get_average_heat_level(spicy_foods):
    running_total = 0
    running_list = len(spicy_foods)

    for food in spicy_foods:
        running_total += food["heat_level"]

    average_heat_level = running_total / running_list
    return average_heat_level

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

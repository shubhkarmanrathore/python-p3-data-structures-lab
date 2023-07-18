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
    names = [food['name'] for food in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    names = [food for food in spicy_foods if food['heat_level'] > 5]
    return names

def print_spicy_foods(spicy_foods):
    spice_emoji = "🌶"
    for food in spicy_foods:
        emoji_count = food['heat_level'] * spice_emoji
        print (f"{food['name']} ({food['cuisine']}) | Heat Level: {emoji_count}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    spicy_food_list = [foods for foods in spicy_foods if foods['heat_level'] > 5]

    for food in spicy_food_list:
        name = food['name']
        heat = food['heat_level']
        cuisine = food['cuisine']
        print(f"{name} ({cuisine}) | Heat Level: {'🌶' * int(heat)}")

def get_average_heat_level(spicy_foods):
    heat = []
    for food in spicy_foods:
        heat_level = food["heat_level"]
        heat.append(heat_level)

    total_sum = sum(heat)
    average = total_sum / len(heat)
    print(int(average))
    return int(average)

def create_spicy_food(spicy_foods, spicy_food):
    name = spicy_food["name"]
    cuisine = spicy_food["cuisine"]
    heat = spicy_food["heat_level"]

    new_food = {"name": name, "cuisine": cuisine, "heat_level": heat}

    spicy_foods.append(new_food)

    print(spicy_foods)
    return spicy_foods

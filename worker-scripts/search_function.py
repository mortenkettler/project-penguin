def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find {expected}")

beers = [
    {"name": "Spannmålstout", "brewery": "Remmarlöv", "abv": 6.0},
    {"name": "Migla", "brewery": "Remmarlöv", "abv": 6.5},
    {"name": "Double Migla", "brewery": "Remmarlöv", "abv": 8.0},
]

def get_beer_name(beer):
    return beer["name"]

# pass in functions into other functions
print(search(beers, "Migla", get_beer_name))

# alternative lambda
print(search(beers, "Double Migla", lambda beer: beer["name"]))
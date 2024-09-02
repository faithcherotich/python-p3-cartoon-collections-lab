def roll_call_dwarves(dwarves):
    for index, dwarf in enumerate(dwarves, start=1):
        print(f"{index}. {dwarf}") 
roll_call_dwarves(["Doc", "Dopey", "Bashful", "Grumpy"])

def summon_captain_planet(planeteer_calls):
    return [call.capitalize() + "!" for call in planeteer_calls]
planeteer_calls = ["earth", "wind", "fire", "water", "heart"]
results= summon_captain_planet(["carrot", "cucumber", "pepper"])
print(results)

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False


def find_the_cheese(items):
    cheeses = ["cheddar","gouda","camembert"]
    for item in items:
         if item in cheeses:
            return item
    return None


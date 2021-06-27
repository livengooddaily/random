import random

bewohner = {
    150: "Torben",
    151: "Steffen",
    152: "Kai",
    153: "Theo",
    154: "Nick",
    155: "Max",
    156: "Eddie",
    157: "Jared",
    158: "Robin",
    159: "Jayant",
    160: "Can"
}

room_numbers = list(bewohner.keys())
successfully_added = []
pairs = []
count = 0
number_of_weeks = len(bewohner)

def has_occurred_twice(room_number, successfully_added):
    return True if successfully_added.count(room_number) == 2 else False

while len(pairs) != number_of_weeks:
    count += 1
    room1 = random.choice(room_numbers)
    room2 = random.choice(room_numbers)
    last_quarter = int(number_of_weeks * 0.75)

    if room1 == room2:
        pass
    elif has_occurred_twice(room1, successfully_added):
        room_numbers.remove(room1)
    elif has_occurred_twice(room2, successfully_added):
        room_numbers.remove(room2)
    elif len(successfully_added) < last_quarter and (room1 in successfully_added or room2 in successfully_added):
        pass
    elif len(successfully_added) >= last_quarter and (room1 in successfully_added[-last_quarter:] or room2 in successfully_added[-last_quarter:]):
        if len(pairs) == number_of_weeks - 1:
            pairs.insert(0,[room1,room2])
            successfully_added.append(room1)
            successfully_added.append(room2)
        else:
            pass
    else:
        successfully_added.append(room1)
        successfully_added.append(room2)
        pairs.append([room1,room2])

print(f'Solution found in {count} tries')
room_numbers = list(bewohner.keys())
for occurrence in [successfully_added.count(room) for room in room_numbers]:
    print(occurrence)
for week, pair in enumerate(pairs):
    print(f"Woche {week + 1}: {bewohner[pair[0]]} ({pair[0]}) und {bewohner[pair[1]]} ({pair[1]})")
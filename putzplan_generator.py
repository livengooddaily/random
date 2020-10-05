import random

bewohner = {
    150: "Torben",
    151: "Steffen",
    152: "Mouad",
    153: "Theo",
    154: "Unknown",
    155: "Max",
    156: "Eddie",
    157: "Jared",
    158: "Robin",
    159: "Jayant",
    160: "Can"
}

room_numbers = list(bewohner.keys())
results = []
pairs = []
count = 0

def has_occurred_twice(room_number, results):
    return True if results.count(room_number) == 2 else False

while len(pairs) != 11:
    count += 1
    room1 = random.choice(room_numbers)
    room2 = random.choice(room_numbers)

    if room1 == room2:
        pass
    elif has_occurred_twice(room1, results):
        room_numbers.remove(room1)
        pass
    elif has_occurred_twice(room2, results):
        room_numbers.remove(room2)
    elif len(results) < 8 and (room1 in results or room2 in results):
        pass
    elif len(results) >= 8 and (room1 in results[-8:] or room2 in results[-8:]):
        if len(pairs) == 10:
            pairs.insert(0,[room1,room2])
        else:
            pass
    else:
        results.append(room1)
        results.append(room2)
        pairs.append([room1,room2])

print(f'Solution found in {count} tries')
for week, pair in enumerate(pairs):
    print(f"Woche {week + 1}: {bewohner[pair[0]]} ({pair[0]}) und {bewohner[pair[1]]} ({pair[1]})")
import random
import time

start = time.time()

room_numbers = [x + 1 for x in range(149,160)]
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

    if time.time()-start > 3:
        print(f'Solution not found after {count} tries')
        for room in room_numbers:
            print(room, results.count(room))
        print(results)
        print(pairs)
        break

print(f'Solution found in {count} tries')
for pair in pairs:
    print(pair)
import random
import xlsxwriter
import datetime

# Name der Excel-Datei
excel_datei = "putzplan.xlsx"

# Start Datum
datum = "16.08.2021"

# Zimmernummer, Name des Bewohners
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

# Alle Küchendienst aufgaben
aufgaben = [
    "Mikrowelle", 
    "Backofen (Bleck, Rost, Schutzbleck, Seiten)",
    "Küche und Wohnzimmer saugen und wischen",
    "ALLE Oberflächen",
    "Abtropfgitter, Bestecktrockner",
    "Beide Herdplatte",
    "Küchenfenster (beidseitig)",
    "Mülleimer (Innen- und Außenseite)",
    "Toaster und Wasserkocher",
    "Unterseite der Küchenschränke",
    "Staubsauger saubern",
    "Alle allgemeine Schränke putzen"
]

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

print(f'Lösung in {count} Versuche gefunden\n------------ERGEBNISSE------------')
for week, pair in enumerate(pairs):
    print(f"Woche {week + 1}: {bewohner[pair[0]]} ({pair[0]}) und {bewohner[pair[1]]} ({pair[1]})")


workbook = xlsxwriter.Workbook(excel_datei)
worksheet = workbook.add_worksheet()

row = 0
col = 1
date = datetime.datetime.strptime(datum, "%d.%m.%Y")

for pair in pairs:
    room1 = pair[0]
    room2 = pair[1]
    end_date = date + datetime.timedelta(days=13)

    worksheet.write(row, col, f"{room1} & {room2}")
    worksheet.write(row+1, col, f"{date.strftime('%d.%m')}-{end_date.strftime('%d.%m')}")

    date = end_date + datetime.timedelta(days=1)
    col += 1

col = 0
row += 2

for task in aufgaben:
    worksheet.write(row, col, task)
    row += 1

workbook.close()
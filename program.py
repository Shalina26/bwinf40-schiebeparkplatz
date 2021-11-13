from pathlib import Path


def read_input(filename='parkplatz0.txt'):
    """ Beispieldatei einlesen
    Die Zeilen in Integer und List umwandeln und Zeilenumbrüche mit .strip() entfernen.
    Default ist das Aufgabenbeispiel parkplatz0.txt.
    """
    file = Path('sampledata', filename)
    with open(file, 'r') as file_in:
        parked_cars = file_in.readline().split()
        moving_cars_total = file_in.readline().strip()
        moving_cars = [line.strip() for line in file_in.readlines()]

    print(parked_cars)
    print(moving_cars_total)
    print(moving_cars)

    return parked_cars, moving_cars

def make_parkinglot(parked_cars, moving_cars):
    """
    Erstellt aus parked_cars und alphabet die Liste parkinglot mit allen Autos, die ausgeparkt werden sollen.
    Erstellt aus moving_cars ein dict(), dessen key der Buchstabe des Autos und value die Nummer des Parkplatzes ist.
    Gibt den Autos auf dem Parkplatz einen Index und prüft nacheinander alle Autos, ob sie ausparken können oder nicht.
    """

    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                "U", "V", "W", "X", "Y", "Z"]
    parkinglot = []
    end = parked_cars[1]

    occupiedlot = {}

    for element in moving_cars:
        letter, number = element.split()
        number = int(number)
        occupiedlot[letter] = number
        occupiedlot[letter.lower()] = number + 1

    print(occupiedlot)

    count = 0
    for letter in alphabet:
        arr = [letter]
        arr.append(0)
        for key, value in occupiedlot.items():
            if value == count:
                arr.append(key.upper())
                arr.remove(0)
        parkinglot.append(arr)
        if letter == end:
            break
        count += 1

    print(parkinglot)
    return parkinglot


def move_cars(parkinglot):

    for x in range(0, len(parkinglot)):
        parking_lot_copy = [["A", 0], ["B", 0], ["C", "H"], ["D", "H"], ["E", 0], ["F", "I"], ["G", "I"]]
        if parking_lot_copy[x][1] != 0:
            y = x
            while parking_lot_copy[x][1] != 0:
                if parking_lot_copy[y - 1][1] == 0:
                    parking_lot_copy[y - 1][1] = parking_lot_copy[y][1]
                    parking_lot_copy[y][1] = parking_lot_copy[y + 1][1]
                    parking_lot_copy[y + 1][1] = 0
                    print(parking_lot_copy[x][0], "move left", parking_lot_copy[x - 1][1])
                    y -= 1
                elif parking_lot_copy[y - 1][1] == parking_lot_copy[y][1]:
                    parking_lot_copy[y - 2][1] = parking_lot_copy[y - 1][1]
                    parking_lot_copy[y - 1][1] = parking_lot_copy[y][1]
                    parking_lot_copy[y][1] = 0
                    print(parking_lot_copy[x][0], "move left", parking_lot_copy[x - 1][1])
        else:
            print(parking_lot_copy[x][0], "free to go")

    print_parkinglot(parkinglot)


def print_parkinglot(parkinglot):
    for x in range(0, len(parkinglot)):
        if parkinglot[x][1] == 0:
            print(parkinglot[x][0], "empty")
        else:
            print(parkinglot[x][0], "taken")


if __name__ == '__main__':
    parked_cars, moving_cars = read_input()
    parkinglot = make_parkinglot(parked_cars, moving_cars)
    move_cars(parkinglot)

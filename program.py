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

    for letter in alphabet:
        parkinglot.append(letter)
        if letter == end:
            break

    occupiedlot = {}

    for element in moving_cars:
        letter, number = element.split()
        number = int(number)
        occupiedlot[letter] = number
        occupiedlot[letter.lower()] = number + 1

    print(occupiedlot)

    for space in parkinglot:
        index = parkinglot.index(space)
        if index in occupiedlot.values():
            print_result(index, occupiedlot, parkinglot)
        else:
            print(f"{parkinglot[index]}: ")


def move_cars(index, occupiedlot, parkinglot):
    """
    Prüft, welches Auto aus occupiedlot das Auto blockiert, was ausparken will und prüft, ob es sich um das Vorder- oder
    Hinterteil handelt, das blockiert.
    """

    indexItems = 0
    for key, value in occupiedlot.items():
        if index == value:
            div = indexItems % 2
            if div == 0:
                check = value + 2
                result = assign_side_and_number_blocking_back(parkinglot, check)
            else:
                check = value - 2
                result = assign_side_and_number_blocking_front(check)
        indexItems += 1

    return key, result[0], result[1]


def assign_side_and_number_blocking_back(parkinglot, check):
    if check >= len(parkinglot):
        number = 2
        side = "links"
    else:
        number = 1
        side = "rechts"

    return number, side


def assign_side_and_number_blocking_front(check):
    if check <= 0:
        number = 2
        side = "rechts"
    else:
        number = 1
        side = "links"

    return number, side


def print_result(index, occupiedlot, parkinglot):
    result = move_cars(index, occupiedlot, parkinglot)
    crashingCar = "H"
    number = 1

    print(f"{parkinglot[index]}: {crashingCar} {number} {result[2]}, {result[0].upper()} {result[1]} {result[2]}")


if __name__ == '__main__':
    parked_cars, moving_cars = read_input()
    make_parkinglot(parked_cars, moving_cars)

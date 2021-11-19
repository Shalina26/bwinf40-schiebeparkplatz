from pathlib import Path
from copy import deepcopy


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

    count = 0
    for letter in alphabet:
        array = [letter]
        array.append(0)
        for key, value in occupiedlot.items():
            if value == count:
                array.append(key.upper())
                array.remove(0)
        parkinglot.append(array)
        if letter == end:
            break
        count += 1

    print(parkinglot)
    return parkinglot


def move_cars(parkinglot):
    moving_car = None
    direction = None

    for current_car in range(0, len(parkinglot)):
        parking_lot_copy = deepcopy(parkinglot)
        cars = {}
        count = 0  # for defining moving_car only once and then changing its value for every step
        if parking_lot_copy[current_car][1] != 0:
            while parking_lot_copy[current_car][1] != 0:
                count += 1

                if count == 1:
                    if current_car == len(parkinglot) - 1:
                        moving_car = current_car - 1
                        moving_car, direction = move_left(parking_lot_copy, moving_car, current_car, count, cars, direction)
                        continue

                    if current_car == 0:
                        moving_car = current_car
                        moving_car, direction = move_right(parking_lot_copy, moving_car, current_car, count, cars, direction)
                        continue

                    if 0 < current_car < len(parkinglot) - 1:
                        if parking_lot_copy[current_car + 1][1] == parking_lot_copy[current_car][1]:
                            if count == 1:
                                moving_car = current_car
                            moving_car, direction = move_right(parking_lot_copy, moving_car, current_car, count, cars, direction)
                            continue

                        elif parking_lot_copy[current_car - 1][1] == parking_lot_copy[current_car][1]:
                            if count == 1:
                                moving_car = current_car - 1
                            moving_car, direction = move_left(parking_lot_copy, moving_car, current_car, count, cars, direction)
                else:
                    if direction == "links":
                        moving_car, direction = move_left(parking_lot_copy, moving_car, current_car, count, cars, direction)
                    else:
                        moving_car, direction = move_right(parking_lot_copy, moving_car, current_car, count, cars, direction)

            print(f"{parking_lot_copy[current_car][0]}: {cars} {direction}")

        else:
            print(f"{parking_lot_copy[current_car][0]}: ")


def move_left(parking_lot_copy, moving_car, current_car, count, cars, direction):
    crash, blocking_car = is_crash_left(parking_lot_copy, moving_car)
    if not crash:  # no crash
        cars[parking_lot_copy[current_car][1]] = count
        direction = "links"
        moving_car = move_car_one_left(parking_lot_copy, moving_car)
    elif crash and not blocking_car:  # crash against the border
        cars[parking_lot_copy[current_car][1]] = count
        direction = "rechts"
        moving_car = move_car_one_right(parking_lot_copy, moving_car)
    else:  # another car needs to be moved first
        print("hello")
        print(parking_lot_copy)
        moving_car -= 2
        move_left(parking_lot_copy, moving_car, current_car, count, cars, direction)
        print("bye")
        if not cars.get(parking_lot_copy[moving_car][1]):
            cars[parking_lot_copy[moving_car][1]] = 0
        cars[parking_lot_copy[moving_car][1]] += 1
        moving_car = move_car_one_left(parking_lot_copy, moving_car)
        print(parking_lot_copy)

    return moving_car, direction


def move_left_recursion():
    pass


def move_right(parking_lot_copy, moving_car, current_car, count, cars, direction):
    crash, blocking_car = is_crash_right(parking_lot_copy, moving_car)
    if not crash:  # no crash
        cars[parking_lot_copy[current_car][1]] = count
        direction = "rechts"
        moving_car = move_car_one_right(parking_lot_copy, moving_car)
    elif crash and not blocking_car:  # crash against the border
        print("Hello")
        cars[parking_lot_copy[current_car][1]] = count
        direction = "links"
        moving_car = move_car_one_left(parking_lot_copy, moving_car)
    else:  # another car needs to be moved first
        pass

    return moving_car, direction


def move_car_one_left(parking_lot_copy, moving_car):
    parking_lot_copy[moving_car - 1][1] = parking_lot_copy[moving_car][1]
    parking_lot_copy[moving_car + 1][1] = 0
    moving_car -= 1
    return moving_car


def move_car_one_right(parking_lot_copy, moving_car):
    parking_lot_copy[moving_car + 2][1] = parking_lot_copy[moving_car][1]
    parking_lot_copy[moving_car][1] = 0
    moving_car += 1
    return moving_car


def is_crash_left(parking_lot_copy, moving_car):
    try:
        if parking_lot_copy[moving_car - 1][1] != 0:
            crash = True
            blocking_car = True

        else:
            crash = False
            blocking_car = False
        return crash, blocking_car
    except IndexError:
        crash = True
        blocking_car = False
        return crash, blocking_car


def is_crash_right(parking_lot_copy, moving_car):
    try:
        if parking_lot_copy[moving_car + 2][1] != 0:
            crash = True
            blocking_car = True
        else:
            crash = False
            blocking_car = False
        return crash, blocking_car
    except IndexError:
        crash = True
        blocking_car = False
        return crash, blocking_car


if __name__ == '__main__':
    parked_cars, moving_cars = read_input()
    parkinglot = make_parkinglot(parked_cars, moving_cars)
    move_cars(parkinglot)

from pathlib import Path
from copy import deepcopy


def read_input(filename='parkplatz2.txt'):
    """ Beispieldatei einlesen
    Die Zeilen in Integer und List umwandeln und Zeilenumbrüche mit .strip() entfernen.
    Default ist das Aufgabenbeispiel parkplatz0.txt.
    """
    file = Path('sampledata', filename)
    with open(file, 'r') as file_in:
        parked_cars = file_in.readline().split()
        moving_cars_total = file_in.readline().strip()
        moving_cars = [line.strip() for line in file_in.readlines()]

    print(f"Parkende Autos: {parked_cars}")
    print(f"Anzahl an Schiebeautos: {moving_cars_total}")
    print(f"Position der Schiebeautos: {moving_cars}")

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

    print(f"Layout Parkplatz: {parkinglot}\n")
    return parkinglot


def move_cars(parkinglot):
    moving_car = None

    for current_car in range(0, len(parkinglot)):
        parking_lot_copy = deepcopy(parkinglot)
        cars = {}
        count = 0  # for defining moving_car only once and then changing its value for every step
        direction = None
        if parking_lot_copy[current_car][1] != 0:
            while parking_lot_copy[current_car][1] != 0:
                count += 1

                if count == 1:
                    if current_car == len(parkinglot) - 1:
                        moving_car = current_car - 1
                        moving_car, direction = move_left_recursion(parking_lot_copy, moving_car, current_car, cars, direction)
                        continue

                    if current_car == 0:
                        moving_car = current_car
                        moving_car, direction = move_right_recursion(parking_lot_copy, moving_car, current_car, cars, direction)
                        continue

                    if 0 < current_car < len(parkinglot) - 1:
                        if parking_lot_copy[current_car + 1][1] == parking_lot_copy[current_car][1]:
                            moving_car = current_car
                            moving_car, direction = move_right_recursion(parking_lot_copy, moving_car, current_car, cars, direction)
                            continue

                        elif parking_lot_copy[current_car - 1][1] == parking_lot_copy[current_car][1]:
                            moving_car = current_car - 1
                            moving_car, direction = move_left_recursion(parking_lot_copy, moving_car, current_car, cars, direction)
                            continue
                else:
                    if direction == "links":
                        moving_car, direction = move_left_recursion(parking_lot_copy, moving_car, current_car, cars, direction)
                        continue
                    elif direction == "rechts":
                        moving_car, direction = move_right_recursion(parking_lot_copy, moving_car, current_car, cars, direction)
                        continue

            print_result(parking_lot_copy, current_car, cars, direction)

        else:
            print(f"{parking_lot_copy[current_car][0]}: ")


def move_left_recursion(parking_lot_copy, moving_car, current_car, cars, direction):
    crash, blocking_car = is_crash_left(parking_lot_copy, moving_car)
    if not crash:
        direction = "links"
        if not cars.get(parking_lot_copy[moving_car][1]):
            cars[parking_lot_copy[moving_car][1]] = 0
        cars[parking_lot_copy[moving_car][1]] += 1
        moving_car = move_car_one_left(parking_lot_copy, moving_car)
    elif crash and not blocking_car:
        direction = "rechts"
    else:
        direction = "links"
        moving_car -= 2
        move_left_recursion(parking_lot_copy, moving_car, current_car, cars, direction)
        moving_car += 2
        if not cars.get(parking_lot_copy[moving_car][1]):
            cars[parking_lot_copy[moving_car][1]] = 0
        cars[parking_lot_copy[moving_car][1]] += 1
        moving_car = move_car_one_left(parking_lot_copy, moving_car)

    return moving_car, direction


def move_right_recursion(parking_lot_copy, moving_car, current_car, cars, direction):
    crash, blocking_car = is_crash_right(parking_lot_copy, moving_car)
    if not crash:  # no crash
        direction = "rechts"
        if not cars.get(parking_lot_copy[moving_car][1]):
            cars[parking_lot_copy[moving_car][1]] = 0
        cars[parking_lot_copy[moving_car][1]] += 1
        moving_car = move_car_one_right(parking_lot_copy, moving_car)
    elif crash and not blocking_car:  # crash against the border
        direction = "links"
    else:  # another car needs to be moved first
        direction = "rechts"
        moving_car += 2
        move_right_recursion(parking_lot_copy, moving_car, current_car, cars, direction)
        moving_car -= 2
        if not cars.get(parking_lot_copy[moving_car][1]):
            cars[parking_lot_copy[moving_car][1]] = 0
        cars[parking_lot_copy[moving_car][1]] += 1
        moving_car = move_car_one_right(parking_lot_copy, moving_car)

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
    if moving_car - 1 >= 0:
        if parking_lot_copy[moving_car - 1][1] != 0:
            crash = True
            blocking_car = True
        else:
            crash = False
            blocking_car = False
        return crash, blocking_car
    else:
        crash = True
        blocking_car = False
        return crash, blocking_car


def is_crash_right(parking_lot_copy, moving_car):
    if moving_car + 2 <= len(parkinglot) - 1:
        if parking_lot_copy[moving_car + 2][1] != 0:
            crash = True
            blocking_car = True
        else:
            crash = False
            blocking_car = False
        return crash, blocking_car
    else:
        crash = True
        blocking_car = False
        return crash, blocking_car


def print_result(parking_lot_copy, current_car, cars, direction):
    solution = []
    for key, value in cars.items():
        move = f"{key} {value} {direction}"
        solution.append(move)
    solution.sort()
    if direction == "rechts":
        solution.reverse()
    result = ", ".join(solution)
    print(f"{parking_lot_copy[current_car][0]}: {result}")


if __name__ == '__main__':
    parked_cars, moving_cars = read_input()
    parkinglot = make_parkinglot(parked_cars, moving_cars)
    move_cars(parkinglot)

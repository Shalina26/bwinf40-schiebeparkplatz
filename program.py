from pathlib import Path
from copy import deepcopy
import random


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

    for current_car in range(0, len(parkinglot)):
        parking_lot_copy = deepcopy(parkinglot)
        if parking_lot_copy[current_car][1] != 0:
            while parking_lot_copy[current_car][1] != 0:

                try:
                    move_right(parking_lot_copy, current_car)
                except IndexError:
                    move_left(parking_lot_copy, current_car)

                if parking_lot_copy[current_car - 1][1] == 0:
                    try:
                        move_right(parking_lot_copy, current_car + 1)
                        print(f"{parking_lot_copy[current_car][0]}: {parking_lot_copy[current_car + 1][1]} 1 rechts")
                    except IndexError:
                        move_left(parking_lot_copy, current_car)
                        print(f"{parking_lot_copy[current_car][0]}: {parking_lot_copy[current_car - 1][1]} 2 links")
                elif parking_lot_copy[current_car - 1][1] == parking_lot_copy[current_car][1]:
                    try:
                        move_left(parking_lot_copy, current_car - 1)
                        print(f"{parking_lot_copy[current_car][0]}: {parking_lot_copy[current_car - 1][1]} 1 links")
                    except IndexError:
                        move_right(parking_lot_copy, current_car)
                        print(f"{parking_lot_copy[current_car][0]}: {parking_lot_copy[current_car + 1][1]} 2 rechts")
                else:
                    pass
        else:
            print(f"{parking_lot_copy[current_car][0]}: ")

    print_parkinglot(parkinglot)


def move_left(parking_lot_copy, current_car):
    if is_crash_left(parking_lot_copy, current_car):
        crash_car_index = current_car - 2
    else:
        move_car_one_left(parking_lot_copy, current_car)


def move_right(parking_lot_copy, current_car):
    if is_crash_right(parking_lot_copy, current_car):
        crash_car_index = current_car + 2
    else:
        move_car_one_left(parking_lot_copy, current_car)


def move_car_one_left(parking_lot_copy, current_car):
    parking_lot_copy[current_car - 1][1] = parking_lot_copy[current_car][1]
    parking_lot_copy[current_car + 1][1] = 0
    current_car_copy -= 1


def move_car_one_right(parking_lot_copy, current_car):
    parking_lot_copy[current_car + 1][1] = parking_lot_copy[current_car][1]
    parking_lot_copy[current_car - 1][1] = 0


def is_crash_left(parking_lot_copy, current_car):
    if parking_lot_copy[current_car - 1][1] != 0:
        return True
    return False


def is_crash_right(parking_lot_copy, current_car):
    try:
        if parking_lot_copy[current_car + 2][1] != 0:
            return True
        return False
    except IndexError:
        return True


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

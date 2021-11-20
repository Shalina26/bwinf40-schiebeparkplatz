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
        occupiedlot[letter] = [number, number + 1]

    print(occupiedlot)

    dict = {}
    count = 0
    for space in parkinglot:
        index = parkinglot.index(space)
        for key, value in occupiedlot.items():
            if index in value:
                occupied = 1
            else:
                occupied = 0
            if occupied == 0:
                dict[parkinglot[index]] = "frei "
            else:
                dict[parkinglot[index]] = "besetzt "
                occupied = 1
            count += 1
    print(f"{dict}")


def move_cars(index, occupiedlot, parkinglot):
    for k, v in occupiedlot.items():
        if v == index:
            value = v
            key = k
            print(key, value)
            solution = move_right(index, key, value, parkinglot, occupiedlot)
            solution1 = move_left(index, key, value)
            if solution[1] and solution1[1]:
                if solution[0] <= solution1[0]:
                    print("rechts")
                elif solution[0] > solution1[0]:
                    print("links")
            elif solution[1] and not solution1[1]:
                print("rechts")
            elif solution1[1] and not solution[1]:
                print("links")
            break


def move_right(index, key, value, parkinglot, occupiedlot):
    effort = 0
    possible = True
    cars = {}  # key = Auto H... value = Anzahl der Züge
    count = 0

    # crash = False
    # while index == value or crash:
    while count != 10:
        for k, v in occupiedlot.items():
            if index == v:
                cars[k] += 1
                occupiedlot[k] += 1
                effort += 1
                if value > len(parkinglot) or value + 1 > len(parkinglot):
                    possible = False
                    break
                else:
                    possible = True

            if value in occupiedlot.items() or value + 1 in occupiedlot.items():

                crash = True
                for k, v in occupiedlot.items():
                    if v in [value, value + 1]:
                        cars[k] += 1
                        v += 1
                        if value > len(parkinglot) or value + 1 > len(parkinglot):
                            possible = False
                            break
                        else:
                            possible = True

            else:
                crash = False
        count += 1

        return effort, possible


def move_left(index, key, value):
    possible = True
    effortLeft = 0

    crash = False
    while index == value or crash:
        pass

    return effortLeft, possible


"""
def crash_cars(index, occupiedlot, parkinglot):

    Prüft, welches Auto aus occupiedlot im Weg steht und ob es sich um das Vorder- oder Hinterteil dieses Autos handelt.
    Darauf basierend wird entschieden, in welche Richtung das Auto als erstes verschoben werden soll. Der Weg mit
    weniger Aufwand wird gewählt. (Variable "effort" anlegen, die pro Zug mitzählt)

    cars = {}

    idx = 0
    for key, value in occupiedlot.items():
        if index == value:
            div = idx % 2
            if div == 0:
                info = assign_side_and_number_blocking_back(parkinglot, key, value)
                if info[1] == "links":
                    check2 = value - 2
                else:
                    check2 = value + 1
            else:
                info = assign_side_and_number_blocking_front(value)
                if info[1] == "rechts":
                    check2 = value + 2
                else:
                    check2 = value - 1
            cars[key] = info[0]
            move_cars(index, value, check2)
            break
        idx += 1


def move_cars_old(index, value, check2):
    crash = 0

    while index == value or crash == 1:
        for key, value in occupiedlot.items():
            if check2 == v:
                if dif == 2 or dif == -2:
                    cars[k] = 2
                else:
                    cars[k] = 1
                crash += 1



def assign_side_and_number_blocking_back(parkinglot, key, value):
    check = value + 2
    if check >= len(parkinglot):
        number = 2
        side = "links"
    else:
        number = 1
        side = "rechts"

    return number, side


def assign_side_and_number_blocking_front(value):
    check = value - 2
    if check < 0:
        number = 2
        side = "rechts"
    else:
        number = 1
        side = "links"

    return number, side


def car_crash(parkinglot, occupiedlot, value, index, check2):
    #result = move_cars(index, occupiedlot, parkinglot)
    #key = result[0]
    crash = True
    #cars = {}


    for k, v in occupiedlot.items():
        if check2 == v:
            dif = value - v
            if dif == 2 or dif == -2:
                number = 2
            else:
                number = 1
            cars[k] = 1

            while check2 == v:
            #crashingCar = f"{k.upper()}"
            side = result[2]

            break
        else:
            crashingCar = ""
            number = ""
            side = ""
            break

    return crashingCar, number, side


def print_result(index, occupiedlot, parkinglot, cars):
    result = move_cars(index, occupiedlot, parkinglot)
    #crash = car_crash(parkinglot, occupiedlot, value, index, check2)
    crash = "x"

    print(f"{parkinglot[index]}: {crash}, {result[0].upper()} {result[1]} {result[2]}")
"""

if __name__ == '__main__':
    parked_cars, moving_cars = read_input()
    make_parkinglot(parked_cars, moving_cars)

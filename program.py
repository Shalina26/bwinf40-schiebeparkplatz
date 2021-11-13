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
    parkingLot = []
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
        parkingLot.append(arr)
        if letter == end:
            break
        count += 1

    print(parkingLot)
    return parkingLot


def parkingLotProblem(parkingLot):

    for x in range(0, len(parkingLot)):
        parkingLotCopy = [["A", 0], ["B", 0], ["C", "H"], ["D", "H"], ["E", 0], ["F", "I"], ["G", "I"]]
        if parkingLotCopy[x][1] != 0:
            y = x
            while parkingLotCopy[x][1] != 0:
                if parkingLotCopy[y - 1][1] == 0:
                    parkingLotCopy[y - 1][1] = parkingLotCopy[y][1]
                    parkingLotCopy[y][1] = parkingLotCopy[y + 1][1]
                    parkingLotCopy[y + 1][1] = 0
                    print(parkingLotCopy[x][0], "move left", parkingLotCopy[x - 1][1])
                    y -= 1
                elif parkingLotCopy[y - 1][1] == parkingLotCopy[y][1]:
                    parkingLotCopy[y - 2][1] = parkingLotCopy[y - 1][1]
                    parkingLotCopy[y - 1][1] = parkingLotCopy[y][1]
                    parkingLotCopy[y][1] = 0
                    print(parkingLotCopy[x][0], "move left", parkingLotCopy[x - 1][1])
        else:
            print(parkingLotCopy[x][0], "free to go")

    printParkingLot(parkingLot)


def printParkingLot(parkingLot):
    for x in range(0, len(parkingLot)):
        if parkingLot[x][1] == 0:
            print(parkingLot[x][0], "empty")
        else:
            print(parkingLot[x][0], "taken")


if __name__ == '__main__':
    parked_cars, moving_cars = read_input()
    parkingLot = make_parkinglot(parked_cars, moving_cars)
    parkingLotProblem(parkingLot)

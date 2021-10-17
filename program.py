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
    Gibt den Autos auf dem Parkplatz einen Index und prüft, welche Autos ausparken können und welche nicht.
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
            print(f"{parkinglot[index]}: besetzt")
        else:
            print(f"{parkinglot[index]}: ")


if __name__ == '__main__':
    parked_cars, moving_cars = read_input()
    make_parkinglot(parked_cars, moving_cars)
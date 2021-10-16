# bwinf40 | A1: Schiebeparkplatz

Auf dem "Schiebeparkplatz" in Tübingen darf man Wagen auch quer vor den normalen Parkplätzen abstellen. Quer stehende Wagen können vorsichtig vorwärts oder rückwärts verschoben werden, um einem blockierten Wagen die Ausfahrt zu ermöglichen.

Das Bild zeigt eine Situation auf einem so funktionierenden Parkplatz. Dieser Parkplatz hat eine einzelne "Parkreihe", also eine Reihe mit normalen Plätzen:

![a1](https://user-images.githubusercontent.com/1307113/134763671-11f91080-cfa5-42f0-bbd3-5001396484af.png)

In dieser Situation gilt:
- Damit die Wagen A, B oder E ausfahren können, muss kein anderer Wagen verschoben werden.
- Damit die Wagen C, D oder G ausfahren können, muss jeweils mindestens ein anderer Wagen verschoben werden.
- Damit der Wagen F ausfahren kann, müssen hingegen zuerst Wagen H und dann Wagen I verschoben werden.

Die Stadtplaner von Bewinfingen wollen nun auch einen Schiebeparkplatz haben - aber einen vollautomatischen! Insbesondere soll das Verschieben von einem Computerprogramm gesteuert werden.

## Aufgabe 1

Schreibe ein Programm, das eine Situation auf einem Schiebeparkplatz mit einer Parkreihe einliest und für jeden Wagen auf einem normalen Platz bestimmt, welche andere Wagen wie verschoben werden müssen, damit er ausfahren kann. Dabei sollen möglichst wenige verschoben werden.

Die Ausgabe des Programms für das obige Beispiel:

```
A:
B:
C: H 1 rechts
D: H 1 links
E:
F: H 1 links, I 2 links
G: I 1 links
```

Wende dein Programm mindestens auf alle Beispiele an, die du im Ordner [/beispieldaten](/beispieldaten) findest, und dokumentiere die Ergebnisse.
  

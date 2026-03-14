# Zahlenrate Spiel

from random import randint
zahl = randint(1, 100)

print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht!")
while True:
    eingabe = int(input("Rate an welche Zahl ich denke! "))

    if eingabe == zahl:
        print("Yey! Du hast die richtige Zahl erraten! Die Zahl an die ich dachte ist" , zahl , "! ")
        break

    if eingabe < zahl:
        print("Die Zahl ist zu klein!" )
    else:
        print("Die Zahl ist zu groß!")
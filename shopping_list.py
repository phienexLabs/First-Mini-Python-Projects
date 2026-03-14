#Einkaufszettel

einkaufszettel = []

while True:
    aktion = input("Möchtest du einen Artikel hinzufügen, entfernen oder die Liste anzeigen? (hinzufügen / entfernen / anzeigen / beenden) ").strip().lower()


    if aktion == "hinzufügen":
        artikel = input("Welchen Artikel möchtest du hinzufügen? ")
        einkaufszettel.append(artikel)
        print("Artikel wurde hinzugefügt. ")

    elif aktion == "entfernen":
        artikel = input("Welchen Artikel möchtest du entfernen? ")

        if artikel in einkaufszettel:
            einkaufszettel.remove(artikel)
            print("Artikel wurde entfernt. ")
        else:
            print("Artikel wurde nicht gefunden. ")

    elif aktion == "anzeigen":
        print("Dein Einkaufszettel: ")
        for artikel in einkaufszettel:
            print(f" - {artikel}")

    elif aktion == "beenden":
        print("Einkaufszettel beendet. ")
        break
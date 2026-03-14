# Ausweisabfrage Club

name = input("Wie heißt du? ")
alter = int(input("Wie alt bist du? "))

if alter < 18:
    print("Du bist leider zu jung. ")
else:
    ausweis = input("Hast du einen Ausweis dabei? (ja/nein ")
    hat_ausweis = ausweis == "ja"

    if hat_ausweis:
        print(f"Hi", name, " viel Spaß im Club!")
    else:
        print("Ohne Ausweis kein Zutritt, komm bald wieder. ")
# Kino Ticket Preis Generator
alter = int(input("Wie alt bist du? "))
anzahl = int(input("Wie viele Tickets möchten Sie kaufen? "))

if alter > 65:
    preis = 7.5 * anzahl
elif alter >= 18:
    preis = 10 * anzahl
else:
    preis = 5 * anzahl

if anzahl == 1:
    print(f"Ihr Ticket kostet {preis} Euro")
else:
    print(f"Ihr Tickets kosten {preis} Euro")
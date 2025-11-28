import statistics

# Deine Liste mit Werten
werte = [3, 7, 87]

# Berechne hier den Durchschnitt
durchschnitt = sum(werte) / len(werte)

# oder

durchschnitt = statistics.mean(werte)

# Gib das Ergebnis aus
print(durchschnitt)
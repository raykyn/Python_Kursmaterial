satz = "Programmieren mit Python ist wirklich spannend."

# Ermittle das fünfte Wort im Satz
fuenftes_wort = satz.split()[4]
print(fuenftes_wort)

# Zähle die Buchstaben im Satz - ohne Leerzeichen
anzahl_buchstaben = len(satz.replace(" ", ""))
print(anzahl_buchstaben)

# Prüfe, ob das Wort "Python" im Satz enthalten ist. Falls kein Python enthalten ist, gib "-1" aus, sonst den Index, wo "Python" steht.
# Tipp: Schau dir mal die String-Funktionen an
python_im_satz = satz.find("Python")
print(python_im_satz)

# Erzeuge einen neuen String, der aus den ersten 3 Zeichen des ersten Wortes und den letzten 3 Zeichen des letzten Wortes besteht.
neues_wort = satz[:3] + satz[-3:]
print(neues_wort)
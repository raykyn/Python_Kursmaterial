text = "Es ist so toll an der Zentralbibliothek Zürich programmieren zu lernen!"

# Wie lang ist der Text?
textlaenge = len(text)
print(textlaenge)

# Welches ist das 16. Zeichen im Text?
zeichen_16 = text[15]
print(zeichen_16)

# An welchem Index kommt zum ersten Mal ein ü vor?
erstes_ue = text.index("ü")
print(erstes_ue)

# Wer muss den Text schon versteht? Sortiert mal lieber die Buchstaben!
sortierte_zeichen = sorted(text)
print(sortierte_zeichen)
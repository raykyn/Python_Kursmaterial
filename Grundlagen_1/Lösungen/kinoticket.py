# Preise und Rabatt
kinderpreis = 5
jugendlichenpreis = 7
erwachsenenpreis = 12
seniorenpreis = 6

rabbattag = "montag"
rabbathoehe = 2

# Käufer-Informationen
alter = 46

tag_des_kaufs = "montag"

# Berechnung
if alter <= 12:  # kinder
    preis = kinderpreis
elif alter <= 17:
    preis = jugendlichenpreis
elif alter <= 64:
    preis = erwachsenenpreis
else:
    preis = seniorenpreis

if tag_des_kaufs == rabbattag:
    preis -= rabbathoehe

print(preis)
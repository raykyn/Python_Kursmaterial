# Preise und Rabatt
kinderpreis = 5
jugendlichenpreis = 7
erwachsenenpreis = 12
seniorenpreis = 6

rabbatttag = "montag"
rabatttag2 = "donnerstag"
rabbathoehe = 2

# Käufer-Informationen
alter = 46

tag_des_kaufs = "donnerstag"

# Berechnung
if alter <= 12:  # kinder
    preis = kinderpreis
elif alter <= 17:
    preis = jugendlichenpreis
elif alter <= 64:
    preis = erwachsenenpreis
else:
    preis = seniorenpreis

if tag_des_kaufs == rabbatttag or tag_des_kaufs == rabatttag2:
    preis -= rabbathoehe

# noch schöner gelöst wäre übrigens:
# if tag_des_kaufs in [rabbatttag, rabatttag2]:
#    preis -= rabbathoehe

print(preis)
import math

punkt_a = [2, 5]
punkt_b = [7, 1]

# Berechne hier die Entfernung
abstand = math.sqrt((punkt_a[0] - punkt_b[0])**2 + (punkt_a[1] - punkt_b[1])**2)

# oder 

abstand = math.dist(punkt_a, punkt_b)

print(abstand)
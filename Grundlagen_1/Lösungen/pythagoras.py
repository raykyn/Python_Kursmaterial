import math

kathete_a = 23
kathete_b = 15

hypothenuse = math.sqrt(kathete_a*kathete_a + kathete_b*kathete_b)

# oder

hypothenuse = math.sqrt(kathete_a**2 + kathete_b**2)

# oder

hypothenuse = math.hypot(kathete_a, kathete_b)

print(hypothenuse)
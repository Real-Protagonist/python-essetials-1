def liters_100km_to_miles_gallon(liters):
    gallons = liters / 3.785411784
    miles = 100 * 1000 / 1609.344
    return miles / gallons

def miles_gallon_to_liters_100km(miles):
    mt = miles * 1609.344 / 1000 / 100
    lit = 3.785411784
    return lit / mt

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(miles_gallon_to_liters_100km(31.4))

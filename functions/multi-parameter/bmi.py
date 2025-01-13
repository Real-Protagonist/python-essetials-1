def bmi(weight, height):
    # CHECKING THE MEANING OF THE EACH VALUES
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None

    return weight / height ** 2

def lb_to_kg(lb):
    return lb * 0.45359237

def ft_and_inch_to_m(ft, inch=0.0):
    return ft * 0.3048 + inch * 0.0254

print(ft_and_inch_to_m(6))
print(lb_to_kg(1))

print(bmi(lb_to_kg(176), ft_and_inch_to_m(5, 7)))

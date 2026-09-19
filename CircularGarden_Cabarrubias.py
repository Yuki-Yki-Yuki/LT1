import math

# Asks for the users' radius in meters.
Radius = float(input("Please enter the radius of the circle in meters: "))

Area = math.pi * math.pow(Radius, 2) # Calculates the area using math.pi as the shorter placement of the actual pi value.
Circumference = 2 * math.pi * Radius # Calculates the circumference using math.pi as the pi itself.
Square_Root = math.sqrt(Area) # Calculates the square root by using the square root function.
Rounded_Down_Area = math.floor(Area) # Calculates the rounded down area using math.floor which rounds the value to the equal or less of it.
Rounded_Up_Area = math.ceil(Area) # Calculates the rounded up area using math.ceil which rounds the value to the equal or greater of it.

# Outputs the calculated values in their correct units.
print(f"The area of the circular garden is: {Area:.2f} square meters.")
print(f"The circumference of the circular garden is: {Circumference:.2f} meters.")
print(f"The square root of the area is: {Square_Root:.2f}")
print(f"The rounded circumference is: {Rounded_Down_Area} square meters.")
print(f"The rounded circumference is: {Rounded_Up_Area} square meters.")
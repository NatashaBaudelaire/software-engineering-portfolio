import math

def calculate_area(shape, measurements):
    shape = shape.lower()
    if shape == "square":
        side = float(measurements[0])
        return side ** 2
    elif shape == "rectangle":
        width = float(measurements[0])
        height = float(measurements[1])
        return width * height
    elif shape == "triangle":
        base = float(measurements[0])
        height = float(measurements[1])
        return (base * height) / 2
    elif shape == "circle":
        radius = float(measurements[0])
        return math.pi * radius ** 2
    else:
        print(f"Warning: '{shape}' is not a recognised shape. Skipping.")
        return 0 

print("--- Total Area Calculation for the Machine ---")

unit = input("Enter the unit (metre or centimetre): ").strip().lower()

n = int(input("Enter the number of shapes: "))

total_area = 0

for _ in range(n):
    line = input("Enter shape and measurements (e.g., 'square: 5'): ").strip()
    shape, values = line.split(":")
    measurements = values.strip().split()
    
    area = calculate_area(shape, measurements)
    
    if unit.startswith("centimetre"):
        area /= 10000
    
    total_area += area

print(f"\nThe total area required for the machine is {total_area:.2f} square metres.")
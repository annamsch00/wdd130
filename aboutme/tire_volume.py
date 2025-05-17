import math
pi = math.pi

w = float(input("Enter the width of the tire in mm (ex 205):"))
print(f"Confirmed Width: {w}")
a = float(input("Enter the aspect ratio of the tire (ex 60):"))
print(f"Confirmed Aspect Ratio: {a}")
d = float(input("Enter the diameter of the wheel in inches (ex 15):"))
print(f"Confirmed Diameter: {d}")
v = (pi * (pow(w,2)*a*(w*a+2540*d)))/10000000000
print(f"The approximate volume is {v} liters.")
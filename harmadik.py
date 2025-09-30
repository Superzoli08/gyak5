import math

# Kör területének kiszámítása

sugar = float(input("A kör sugara: "))

terulet = sugar**2 * math.pi

print(f"A kör területe: {round(terulet, 2)}")
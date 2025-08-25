from library import NumeroComplejo
import unittest
import math
z1 = NumeroComplejo(3, 4)   # 3 + 4i
z2 = NumeroComplejo(1, -2)  # 1 - 2i

print("z1 =", z1)

print("z2 =", z2)

print("Suma:", z1.suma(z2))
print("Resta:", z1.resta(z2))
print("Producto:", z1.producto(z2))
print("División:", z1.division(z2))
print("Módulo de z1:", z1.modulo())
print("Conjugado de z1:", z1.conjugado())
print("Polar de z1:", z1.a_polar())
print("Cartesiano desde polar (r=5, θ=π/4):", NumeroComplejo.desde_polar(5, math.pi/4))
print("Fase de z1:", z1.fase())
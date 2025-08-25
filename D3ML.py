import math


class NumeroComplejo:
    def __init__(self, real: float, imag: float):
        self.real = real
        self.imag = imag

    def __repr__(self):
        signo = "+" if self.imag >= 0 else "-"
        return f"{self.real} {signo} {abs(self.imag)}i"

def suma(self, otro):
        return NumeroComplejo(self.real + otro.real, self.imag + otro.imag)

def resta(self, otro):
        return NumeroComplejo(self.real - otro.real, self.imag - otro.imag)

def producto(self, otro):
        r = self.real * otro.real - self.imag * otro.imag
        i = self.real * otro.imag + self.imag * otro.real
        return NumeroComplejo(r, i)

def division(self, otro):
        denom = otro.real**2 + otro.imag**2
        if denom == 0:
            raise ZeroDivisionError("No se puede dividir por cero")
        r = (self.real * otro.real + self.imag * otro.imag) / denom
        i = (self.imag * otro.real - self.real * otro.imag) / denom
        return NumeroComplejo(r, i)


def modulo(self):
        return math.sqrt(self.real**2 + self.imag**2)

def conjugado(self):
        return NumeroComplejo(self.real, -self.imag)

def a_polar(self):
        r = self.modulo()
        theta = math.atan2(self.imag, self.real)  # ángulo en radianes
        return r, theta

@staticmethod
def desde_polar(r, theta):
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        return NumeroComplejo(x, y)
def fase(self):
        return math.atan2(self.imag, self.real)
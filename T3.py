# =========================
# CASO DISCRETO
# =========================
import math

def comb(n, k):
    return math.comb(n, k)

total = comb(8, 2)

def f(x, y):
    if x + y > 2:
        return 0
    return (comb(3, x) * comb(2, y) * comb(3, 2 - x - y)) / total

print("----- CASO DISCRETO -----")
print("f(1,1) =", f(1,1))

suma = 0
for x in range(3):
    for y in range(3):
        if x + y <= 2:
            suma += f(x, y)

print("Suma total =", suma)


# =========================
# CASO CONTINUO
# =========================
import sympy as sp

x, y = sp.symbols('x y')

f_expr = x*y

print("\n----- CASO CONTINUO -----")

integral_total = sp.integrate(f_expr, (y, 0, 1), (x, 0, 2))
print("Integral total =", integral_total)

prob = sp.integrate(f_expr, (y, 0, 0.5), (x, 0, 1))
print("P(X<=1, Y<=0.5) =", prob)

from scipy.stats import binom, poisson, norm, expon
import numpy as np

print("===== BINOMIAL =====")
n = 5
p = 0.4

# Ejercicio 1
print("P(X=2):", binom.pmf(2, n, p))

# Ejercicio 2
print("P(X<=2):", binom.cdf(2, n, p))

# Aplicación
print("Aplicación P(X=1):", binom.pmf(1, 8, 0.1))


print("\n===== POISSON =====")
lam = 3

# Ejercicio 1
print("P(X=2):", poisson.pmf(2, lam))

# Ejercicio 2
print("P(X<=2):", poisson.cdf(2, lam))

# Aplicación
print("P(X>5):", 1 - poisson.cdf(5, 4))


print("\n===== NORMAL =====")

# Ejercicio 1
print("P(X<1):", norm.cdf(1, 0, 1))

# Ejercicio 2
print("P(-1<X<1):", norm.cdf(1) - norm.cdf(-1))

# Aplicación
print("P(X>180):", 1 - norm.cdf(180, 170, 10))


print("\n===== EXPONENCIAL =====")

# Ejercicio 1
print("P(X<1):", expon.cdf(1, scale=1/2))

# Ejercicio 2
print("P(X>2):", 1 - expon.cdf(2, scale=1/2))

# Aplicación
print("P(X>3):", np.exp(-0.5 * 3))

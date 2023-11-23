import numpy as np
from scipy.optimize import minimize

def easom_extended(x):
    n = len(x)
    cos_term = np.prod(np.cos(x)**2)
    exp_term = np.exp(-np.sum((x - np.pi)**2))
    return -(cos_term * exp_term)

# Resolver para n = 10
n = 10
bounds = [(-100, 100)] * n  # Límites de búsqueda aleatoria para cada variable

result = minimize(easom_extended, np.random.uniform(-100, 100, n), method='Nelder-Mead', bounds=bounds,options={'disp': True})

print("Punto óptimo encontrado para n = 10:", result.x)


# Resolver para n = 100
n = 100
bounds = [(-100, 100)] * n  # Límites de búsqueda aleatoria para cada variable

result = minimize(easom_extended, np.random.uniform(-100, 100, n), method='Nelder-Mead', bounds=bounds,options={'disp': True})

print("Punto óptimo encontrado para n = 100:", result.x)


# Resolver para n = 500
n = 500
bounds = [(-100, 100)] * n  # Límites de búsqueda aleatoria para cada variable

result = minimize(easom_extended, np.random.uniform(-100, 100, n), method='Nelder-Mead', bounds=bounds,options={'disp': True})

print("Punto óptimo encontrado para n = 500:", result.x)


# Resolver para n = 1000
n = 1000
bounds = [(-100, 100)] * n  # Límites de búsqueda aleatoria para cada variable

result = minimize(easom_extended, np.random.uniform(-100, 100, n), method='Nelder-Mead', bounds=bounds,options={'disp': True})

print("Punto óptimo encontrado para n = 1000:", result.x)


import numpy as np
from scipy.optimize import minimize

def objective_function(x):
    n = len(x)
    cos_term = np.prod(np.cos(x)**2)
    exp_term = np.exp(-np.sum((x - np.pi)**2))
    return -((-1)**n * cos_term * exp_term)

def gradient(x, h=1e-6):
    n = len(x)
    grad = np.zeros(n)
    for i in range(n):
        x_plus_h = x.copy()
        x_plus_h[i] += h
        x_minus_h = x.copy()
        x_minus_h[i] -= h
        grad[i] = (objective_function(x_plus_h) - objective_function(x_minus_h)) / (2 * h)
    return grad
print('n=10')
x0 = np.full(10,4)  # Initial guess for x
result = minimize(objective_function, x0, method='Newton-CG', jac=gradient)
print(result)
print('n=100')
x0 = np.full(100,4)  # Initial guess for x
result = minimize(objective_function, x0, method='Newton-CG', jac=gradient)
print(result)
print('n=500')
x0 = np.full(500,4)  # Initial guess for x
result = minimize(objective_function, x0, method='Newton-CG', jac=gradient)
print(result)
print('n=1000')
x0 = np.full(500,4)  # Initial guess for x
result = minimize(objective_function, x0, method='Newton-CG', jac=gradient)
print(result)
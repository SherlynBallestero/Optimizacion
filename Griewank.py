
import numpy as np
from scipy.optimize import minimize

# Definir la función Griewank
def griewank(x):
    sum_part = np.sum(x**2 / 4000)
    prod_part = np.prod(np.cos(x / np.sqrt(np.arange(1, len(x) + 1))))
    return 1 + sum_part - prod_part

# Definir el gradiente de la función Griewank
def griewank_gradient(x):
    n = len(x)
    gradient = np.zeros(n)
    for i in range(n):
        sum_part = np.sum(x**2 / 4000)
        prod_part = np.prod(np.cos(x / np.sqrt(np.arange(1, len(x) + 1))))
        gradient[i] = x[i] / 2000 + (np.sin(x[i] / np.sqrt(i+1)) * prod_part) / np.sqrt(i+1)
    return gradient

# Definir el método de Newton para minimizar la función Griewank
#para dimension 10
print("n=10")
n1 = 10
initial_point1 = np.ones(n1)
result1 = minimize(griewank, initial_point1, method='Newton-CG', jac=griewank_gradient, options={'disp': True})
print(result1.x)  # Imprimir el resultado
#para dimension 100
print("n=100")
n2 = 100
initial_point2 = np.ones(n2)
result2 = minimize(griewank, initial_point2, method='Newton-CG', jac=griewank_gradient, options={'disp': True})
print(result2.x)
#para dimension 500
print("n=500")
n3 = 500
initial_point3 = np.ones(n3)
result3 = minimize(griewank, initial_point3, method='Newton-CG', jac=griewank_gradient, options={'disp': True})
print(result3.x)
#para dimension 1000
print("n=1000")
n4 = 1000
initial_point4 = np.ones(n4)
result4 = minimize(griewank, initial_point4, method='Newton-CG', jac=griewank_gradient, options={'disp': True})
print(result4.x)
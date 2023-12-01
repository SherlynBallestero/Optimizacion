import numpy as np
from scipy.optimize import fmin

def easom_extended(x):
    n = len(x)
    cos_term = np.prod(np.cos(x)**2)
    exp_term = np.exp(-np.sum((x - np.pi)**2))
    return -(cos_term * exp_term)

def main():
    x_inicial = np.array([4.5, 4])
    x_opt = fmin(easom_extended, x_inicial, disp=False)
    print("Solución óptima:", x_opt)

if __name__ == "__main__":
    main()

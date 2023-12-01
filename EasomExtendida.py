import numpy as np
from scipy.optimize import fmin

def easom_extended(x):
    n = len(x)
    cos_term = np.prod(np.cos(x)**2)
    exp_term = np.exp(-np.sum((x - np.pi)**2))
    return -(cos_term * exp_term)

def main():
    print("n=2")
    x_inicial1 = np.full(2,4)
    x_opt1 = fmin(easom_extended, x_inicial1, disp=False)
    a=easom_extended(x_opt1)
    print(' optimo en n=10',a)
    print("Solución óptima:", x_opt1)
    
    print("n=10")
    x_inicial1 = np.full(10,4)
    x_opt1 = fmin(easom_extended, x_inicial1, disp=False)
    a=easom_extended(x_opt1)
    print(' optimo en n=10',a)
    print("Solución óptima:", x_opt1)
    
    print("n=100")
    x_inicial2=np.full(100,4)
    x_opt2 = fmin(easom_extended, x_inicial2, disp=False)
    a=easom_extended(x_opt2)
    print(' optimo en n=100',a)
    print("Solución óptima:", x_opt2)
    
    print("n=500")
    x_inicial3=np.full(500,4)
    x_opt3 = fmin(easom_extended, x_inicial3, disp=False)
    a=easom_extended(x_opt3)
    print(' optimo en n=500',a)
    print("Solución óptima:", x_opt3)
    
    print("n=1000")
    x_inicial4=np.full(1000,4)
    x_opt4 = fmin(easom_extended, x_inicial4, disp=False)
    a=easom_extended(x_opt4)
    print(' optimo en n=1000',a)
    print("Solución óptima:", x_opt4)
    
    

if __name__ == "__main__":
    main()






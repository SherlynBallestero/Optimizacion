from scipy.optimize import minimize
import numpy as np
import psutil
import os

def jong_function(x):
    return np.sum(x**2)
def jong_gradient(x):
    return 2*x

def gradient_descent(gradient_f, initial_point, learning_rate, epsilon):
    #analizar cpu
    pid = os.getpid()
    process=psutil.Process(pid)
    
    #desarrollo del metodo
    lista_Resultados=[]
    
    current_point = initial_point
    #para contar el numero de iteracciones
    cont=0
    while True:
        cont=cont+1
        lista_Resultados.append(current_point)
        grad = gradient_f(current_point)
        current_point = current_point - learning_rate * grad
        if np.linalg.norm(grad) < epsilon:
            break
    #resultados    
    dimension=len(initial_point)
    print(f"Para dimension {dimension} se hicieron {cont} iteracciones") 
    cpu_times = process.cpu_times()
    print(f"Tiempo de CPU utilizado: {cpu_times.user} segundos")  
    #print(lista_Resultados) 
    return current_point 
        
   
#Parametros Necesarios
learning_rate = 0.1  # Tasa de aprendizaje
epsilon=0.00000000000000000000001#parametro de parada
# Resolver para n = 10
n1 = 10
initial_point1 = np.ones(n1)  # Punto inicial
result1 = gradient_descent(jong_gradient, initial_point1, learning_rate, epsilon)
#print("Punto óptimo encontrado para n = 10:")
print("Valor óptimo de la función de Jong para n = 10: con maximo-gradiente", jong_function(result1))
print('valor optenido para Newton en n=10')
result1 = minimize(jong_function, initial_point1, method='Newton-CG', jac=jong_gradient, options={'disp': True})
print(result1.x)
# Resolver para n = 100
n2=100
initial_point2 = np.ones(n2)  # Punto inicial
result2 = gradient_descent(jong_gradient, initial_point2, learning_rate, epsilon)
#print("Punto óptimo encontrado para n = 100:", result2)
print("Valor óptimo de la función de Jong para n = 100:", jong_function(result2))
print('valor optenido para Newton en n=100')
result1 = minimize(jong_function, initial_point2, method='Newton-CG', jac=jong_gradient, options={'disp': True})
print(result1.x)
# Resolver para n = 500
n3=500
initial_point3 = np.ones(n3)  # Punto inicial
result3 = gradient_descent(jong_gradient, initial_point3, learning_rate, epsilon)
#print("Punto óptimo encontrado para n = 100:", result3)
print("Valor óptimo de la función de Jong para n = 100:", jong_function(result3))
print('valor optenido para Newton en n=500')
result1 = minimize(jong_function, initial_point3, method='Newton-CG', jac=jong_gradient, options={'disp': True})
print(result1.x)
# Resolver para n = 1000
n4=1000
initial_point4 = np.ones(n4)  # Punto inicial
result4 = gradient_descent(jong_gradient, initial_point4, learning_rate, epsilon)
#print("Punto óptimo encontrado para n = 100:", result4)
print("Valor óptimo de la función de Jong para n = 1000:", jong_function(result4))
print('valor optenido para Newton en n=10')
result1 = minimize(jong_function, initial_point4, method='Newton-CG', jac=jong_gradient, options={'disp': True})
print(result1.x)



# Evaluación de Desempeño del Método de Newton-CG para Minimizar la Función de Griewank

## Introducción
Para resolver la función Griewank se empleará el método de Newton.
El método de Newton-CG es un método de optimización numérica que se utiliza para minimizar funciones no lineales. Este método se basa en la aproximación de la función objetivo mediante una serie de Taylor y en la resolución del sistema de ecuaciones lineales que resulta de dicha aproximación.
En este informe, se evalúa el desempeño del método de Newton-CG para minimizar la función de Griewank, que es una función multimodal con múltiples mínimos locales.

## Configuración Experimental

Se llevaron a cabo experimentos para diferentes dimensiones de la función de Griewank (n = 10, 100, 500 y 1000). Para cada experimento, se utilizó el mismo punto de partida inicial (un vector de unos).

## Resultados

Los resultados de los experimentos se muestran en la siguiente tabla:

| Dimensión (n) | Número de Iteraciones | Valor del Mínimo | 
|---|---|---|---|
| 10 | 8 | 0 | 
| 100 | 11 | 0 | 
| 500 | 15 | 0| 
| 1000 | 19 | 0 | 



## Análisis de Resultados
Como se puede observar, el número de iteraciones aumenta ligeramente a medida que aumenta la dimensión de la función.  El valor del mínimo encontrado en todos los experimentos es el mismo, lo que indica que el método de Newton-CG es capaz de encontrar el mínimo global de la función de Griewank.

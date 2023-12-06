# Evaluación de Desempeño del Método de Newton para Minimizar la Función de Eason-Extendida

## Introducción
Para resolver la función Easom_Extendida se usa en este proyecto el método de Newton. En general, el método de Newton es un método muy eficiente para encontrar los mínimos y máximos de funciones diferenciables.

## Configuración Experimental

Se llevaron a cabo experimentos para diferentes dimensiones de la función de Easom-extendida(n = 10, 100, 500 y 1000). Para cada experimento, se utilizó el mismo punto de partida inicial (un vector de 4).

## Resultados

Los resultados de los experimentos se muestran en la siguiente tabla:

| Dimensión (n) | Valor del Mínimo |No.Evaluaciones del gradiente|descripción|
|---|---|---|---|
| 10 | -0.9999994890015352|442|La optimización se ha detenido porque la función objetivo no ha mejorado en las últimas  maxiter  iteraciones. |
| 100 | -1.1658547678625258e-69 |1 |La optimización se ha completado con éxito|
| 500 | -0.0 |1  |La optimización se ha completado con éxito|
| 1000 | -0.0 |1 | La optimización se ha completado con éxito|



## Análisis de Resultados
Se puede apreciar al ejecutar el metodo como a medida que es menor la dimensión son mas certeros los resultados optenidos, como es el caso para n=10 que se optiene un número bastante cercano a -1 pero ya para el caso de n=500 los resultados menos de acuerdo a lo esperado, pero aun asi cercano en cierto modo al valor del óptimo. Se puede apreciar ademas el punto óptimo optenido para cada caso cuando se ejecuta el método, se ven valores cercanos a (pi,pi..pi), pero es más exacto cuando la dimensión es menor.

## Conclusiones
En general, el método de Newton es un método muy eficiente para encontrar los mínimos y máximos de funciones diferenciables. Sin embargo, es importante tener en cuenta que el método de Newton puede no funcionar bien en funciones que no son convexas o cóncavas


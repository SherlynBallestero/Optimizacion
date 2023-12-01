# Evaluación de Desempeño del Método de la hormiga para Minimizar la Función de Eason-Extendida

## Introducción
Para resolver la función Easom_Extendida se usa en este proyecto el método de búsqueda local llamado método de la hormiga. Este método es adecuado para resolver problemas de optimización no convexos, como es el caso de esta función.

## Configuración Experimental

Se llevaron a cabo experimentos para diferentes dimensiones de la función de Griewank (n = 10, 100, 500 y 1000). Para cada experimento, se utilizó el mismo punto de partida inicial (un vector de 4).

## Resultados

Los resultados de los experimentos se muestran en la siguiente tabla:

| Dimensión (n) | Valor del Mínimo |
|---|---|
| 10 | -0.9999998929539294| 
| 100 | -6.35752231421126e-57 | 
| 500 | -0.0 |  
| 1000 | -0.0 |  



## Análisis de Resultados
Se puede apreciar al ejecutar el metodo como a medida que es menor la dimensión son mas certeros los resultados optenidos, como es el caso para n=10 que se optiene un número bastante cercano a -1 pero ya para el caso de n=500 los resultados menos de acuerdo a lo esperado. Se puede apreciar ademas el punto optimo optenido para cada caso cuando ejecutamos el método, se aprecian valores cercanos a (pi,pi..pi), pero es más exacto cuando la dimensión es menor.

## Conclusiones
El método de la hormiga tiene varias ventajas. Es relativamente simple de implementar y puede ser muy eficiente en problemas de optimización no convexos. También es un método robusto que puede funcionar bien en una variedad de condiciones.Sin embargo, el método de la hormiga también tiene algunas desventajas. Es posible que no encuentre la solución óptima en todos los casos. Además, el método puede ser lento en problemas con grandes espacios de búsqueda.


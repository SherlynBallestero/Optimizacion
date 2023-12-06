
# Resolviendo Jong....

## Introducción
A continuación se evalúa el desempeño del método del gradiente descendiente para minimizar la función de Jong, que es una función multimodal con múltiples mínimos locales.
El método del gradiente descendiente es un método de optimización iterativo que se utiliza para encontrar el mínimo de una función. La idea básica del método es comenzar con una aproximación inicial a la solución y luego iterar, en cada iteración, calculando la dirección en la que la función disminuye más rápidamente y moviéndose en esa dirección. El método del gradiente descendiente convergerá al mínimo de la función si la función es convexa y si la tasa de aprendizaje se selecciona adecuadamente.
 En el caso de la función de Jong, dado que es una  función convexa decisimos aplicar el método del gradiente descendiente y anallizar cómo este converge al mínimo de la función.Posteriormente se aplica el método de Newton, el cual es bastante eficiente y se aplica a funcions diferenciables. Por último se hace una comparación en los resultados. 

## Evaluación de Desempeño del Método del Gradiente Descendente para Minimizar la Función de Jong

## Configuración Experimental

Se llevaron a cabo experimentos para diferentes dimensiones de la función de Jong (n = 10, 100, 500 y 1000). Para cada experimento, se utilizó el mismo punto de partida inicial (un vector de unos) y como factor de aprendizaje 0.1.

## Resultados

Los resultados de los experimentos se muestran en la siguiente tabla:

| Dimensión (n) | Número de Iteraciones | Valor del Mínimo | Tiempo de Ejecución |
|---|---|---|---|
| 10 | 247 |1.3379921764539405e-47~0 | 0.1875 s |
| 100 | 252 | 1.4366581600433837e-47~0| 0.1875 s |
| 500 | 256 | 1.205156213460521e-47~0 | 0.203125 s |
| 1000 | 257 | 1.5425999532294675e-47~0 | 0.203125 s |



## Análisis de Resultados
Para el analisis se utilizó un factor de aprendizaje constante de 0.1. se puede observar que tanto, el número de iteraciones como el tiempo de ejecución aumentan a medida que aumenta la dimensión de la función.  El valor del mínimo encontrado en todos los experimentos es el mismo 0 o mas bien un valor bastante aproximado, por lo que podemos intuir que el método del gradiente descendente es capáz de encontrar el mínimo global de la función de Jong.

También se puede observar que el método del gradiente descendente es más eficiente para dimensiones pequeñas que para dimensiones grandes.El cálculo del gradiente se vuelve más costoso a medida que aumenta la dimensión. El gradiente de una función de n variables es un vector de n componentes, por lo que el cálculo del gradiente requiere n operaciones. A medida que aumenta la dimensión, el cálculo del gradiente se vuelve más costoso

## Conclusiones
En general, el método del gradiente descendiente es un método de optimización eficáz para minimizar la función de Jong. Sin embargo, es importante tener en cuenta las limitaciones del método, como el número de iteraciones y el tiempo de ejecución, y el tamaño de la dimensión.
## Evaluación de Desempeño del Método de Newton para Minimizar la Función de Jong

Ahora veamos que  ocurre en la resolución de la función a travéz del método de Newtón.
## Configuración Experimental
Se llevaron a cabo experimentos para diferentes dimensiones de la función de Jong(n = 10, 100, 500 y 1000). Para cada experimento, se utilizó el mismo punto de partida inicial (un vector de 1).
## Resultados

Los resultados de los experimentos se muestran en la siguiente tabla:

| Dimensión (n) | Número de Iteraciones | Valor del Mínimo | NoEvaluciones|
|---|---|---|---|
| 10 | 2 |0.000000 | 2|
| 100 | 2 | 0.000000| 2 |
| 500 | 2 |  0.000000| 2 |
| 1000 | 2 |  0.000000 | 2 |
## Análisis de Resultados
Se obtuvieron resultados muy buenos en este método, dado que se adquiere el óptimo de la función (0..0) en 2 iteraciones independiente de la longitud del vector de entrada.
# Comparación
Al aplicar el primer método se obtienen resultados buenos pero solo acercados del valor esperado, en cambio con Newton con un  menor número de iteraciones se obtienen resultados significatiamente  exactos.
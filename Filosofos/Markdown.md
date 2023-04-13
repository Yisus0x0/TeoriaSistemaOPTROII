# Concurrencia:

En informática la concurrencia se refiere a la capacidad de un sistema para realizar múltiples tareas en paralelo o superpuestas en lugar de en una secuencia lineal esto significa que se pueden ejecutar varias tareas simultáneamente en el mismo sistema, lo que puede mejorar el rendimiento y la eficiencia del sistema.


# Paralelismo vs. Concurrencia en informática: 

Paralelismo y concurrencia son dos conceptos relacionados pero diferentes en informática el paralelismo se refiere a la capacidad de un sistema para realizar múltiples tareas al mismo tiempo utilizando diferentes núcleos de CPU o diferentes procesadores la concurrencia, por otro lado, se refiere a la capacidad de un sistema para ejecutar múltiples tareas en un mismo procesador.

# Hilos implementación en Python: 

En Python, los hilos se implementan mediante la biblioteca de subprocesos (threads). Python utiliza la técnica de subprocesos para lograr la concurrencia los hilos en Python son livianos y se crean utilizando la clase Thread de la biblioteca threading, los hilos permiten que un programa realice varias tareas simultáneamente, lo que mejora el rendimiento y la eficiencia del sistema.

# deadlock

Un deadlock (o interbloqueo en español) es una situación en un sistema concurrente en la que dos o más procesos quedan bloqueados y no pueden continuar su ejecución, ya que cada uno de ellos está esperando a que el otro libere un recurso que necesita para seguir ejecutándose, esto puede generar una situación de estancamiento en el sistema, donde ninguno de los procesos puede avanzar.

El deadlock es un problema muy común en los sistemas informáticos, especialmente en los sistemas operativos y en las redes de computadoras, donde múltiples procesos compiten por recursos limitados, como memoria, CPU, dispositivos de entrada y salida, entre otros.

Existen diferentes técnicas para prevenir o resolver un deadlock, como el algoritmo del banquero, que utiliza un enfoque de asignación segura de recursos para evitar el deadlock. También existen algoritmos de detección y recuperación del deadlock, que detectan la existencia del problema y toman medidas para recuperar el sistema. En cualquier caso, es importante implementar soluciones adecuadas para evitar el impacto negativo del deadlock en el sistema.

# Exclusión mutua:

La exclusión mutua es un concepto utilizado en informática para garantizar que dos o más procesos no intenten acceder al mismo recurso simultáneamente, la exclusión mutua se logra mediante el uso de bloqueos, que permiten que solo un proceso acceda a un recurso en un momento dado.

# Mantenga y espere: 

Mantener y esperar es un problema que se produce cuando dos o más procesos intentan adquirir varios recursos al mismo tiempo, y cada uno mantiene un recurso mientras espera para adquirir otros recursos necesarios, esto puede provocar estancamiento si un proceso mantiene un recurso mientras espera por otro que ya ha sido adquirido por otro proceso.

# No preventivo 

No preventivo se refiere a un enfoque de manejo de interbloqueos (deadlocks) que se enfoca en la detección y resolución del problema una vez que ha ocurrido, en lugar de tomar medidas preventivas para evitar que el deadlock ocurra en primer lugar, en un enfoque no preventivo, el sistema espera hasta que se produce un deadlock y luego toma medidas para resolverlo, esto puede implicar la identificación de los procesos involucrados en el deadlock, la liberación de los recursos que están siendo retenidos por cada proceso, o la interrupción de uno o más procesos para romper el deadlock.

# Espera circular: 

La espera circular es un problema que se produce cuando varios procesos están esperando que otro proceso libere un recurso, creando un círculo de espera. Esto puede provocar estancamiento si ningún proceso puede continuar hasta que se liberen los recursos. 




# Cómo manejar el interbloque en sistemas operativos - Compara con el problema de los filósofos: 

Un interbloqueo en un sistema operativo es un estado en el que varios procesos se bloquean entre sí mientras esperan que otros procesos del mismo grupo utilicen los recursos. 
El Problema Filosófico es un ejemplo clásico de este tipo de situación, en el que cinco filósofos se sientan alrededor de una mesa con un plato de fideos y dos tenedores, y deben alternar entre comer y pensar para comer, cada filósofo debe tomar dos tenedores a la izquierda y a la derecha, pero si todos los filósofos intentan tomar los mismos tenedores al mismo tiempo, se pone en marcha una especie de condición de carrera  o una espera circular y nadie puede comer. El problema es encontrar un algoritmo que permita a los filósofos no tener nunca se mueran de hambre y que evite el interbloqueo.


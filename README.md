# Programación concurrente y paralela

## Filósofos
Se agregan dos archivos referentes al algoritmo de los filósofos comensales.
El archivo _Filosofos - Lock.py_ es una implementación del algoritmo usando la función **Lock()** de Python, con las condiciones de bloqueo típicas, es decir, si un hilo (en este caso representado por un filósofo) intenta acceder a un recurso compartido en uso, tendrá que entrar en espera activa hasta poder acceder a él.
Por su parte, en el archivo _Filosofos - Rlock.py_ se hace uso de la función **RLock()**, por lo que las condiciones se modifican a un bloque reentrante, admitiendo con ello el bloqueo en más de una ocasión del mismo Lock, además de solo permitir su desbloqueo por el mismo hilo que lo ha bloqueado.

# Práctica UNIR EIEC
 Repositorio de Práctica en GitHub: Actividad Grupal de Pull Requests

> Los comandos del Makefile funcionarán en Linux y MacOS. En caso de usar Windows, deben adaptarse o ejecutarlos en una máquina virtual Linux, como WSL.

## Ejecución
La aplicación puede ejecutarse con el siguiente comando:

```bash
python3 main.py nombre_fichero eliminar_duplicados
```
Donde `nombre_fichero` es la **"ruta"** al fichero que contiene la lista de palabras, una por línea y `dup` es **"yes"** para eliminar palabras duplicadas o **"no"** para mantener la lista

## Ejemplos
Los siguientes son unos ejemplos de cómo se puede ejecutar el programa:

### Ejecución sin parámetros
Si ejecutamos el programa sin introducirle los parámetros esperados, es decir; de la siguiente manera:

```bash
python3 main.py
```

Obtendremos la siguiente salida:
```
Se debe indicar el fichero como primer argumento
El segundo argumento indica si se quieren eliminar duplicados
```

### Ejecución con un fichero creado por el usuario y eliminando duplicados
Teniendo el siguiente fichero de texto:

```txt
Ford
Audi
Ferrari
Mercedes
Renault
Mercedes
Ford
Audi
Ford
Honda
Audi
Honda
```

Podemos ejecutar el programa con el siguiente comando:

```bash
python3 main.py fichero.txt yes
```

Lo que producirá la siguiente salida por consola:

```
Se leerán las palabras del fichero .\ejemplo.txt
['Audi', 'Ferrari', 'Ford', 'Honda', 'Mercedes', 'Renault']
```
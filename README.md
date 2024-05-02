# Practica UNIR EIEC :rocket:

Repositorio de Práctica en GitHub: Actividad Grupal de Pull Requests

El programa recive una serie de palabras y las imprime en pantalla. Loas argumentos opcionales son los siguientes:

- Nombre del fichero: string, lugar donde se encuentran las palabras a recorrer.
- Eliminar duplicados: string, indica si se deben eliminar las palabras duplicadas (`yes`: se deben eliminar | EOC: no eliminar).
- Orden: string, indica si se deben ordenar las palabras (`yes`: orden ascendente | EOC: no ordenar).

Ejemplo de ejecución (sin opciones):

```bash
$ python3 main.py

No se proporcionaron argumentos.
¿Desea continuar con la configuración predeterminada? (yes/no): yes
Se leerán las palabras del fichero words.txt
['alex', 'alex', 'alvaro', 'anderson', 'continua', 'diego', 'entornos', 'entrega', 'integracion', 'master', 'universitario']
```

Ejemplo de ejecución (con opciones):

```bash
python3 main.py words2.txt yes yes

Se leerán las palabras del fichero words2.txt
['A', 'Brand', 'File', 'New', 'Test']
```

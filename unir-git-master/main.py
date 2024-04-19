"""
License: Apache
Organization: UNIR
"""

import os
import sys
import platform

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False


def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
    else:
        print("No se proporcionaron argumentos.")
        user_choice = input("¿Desea continuar con la configuración predeterminada? (yes/no): ").lower()
        if user_choice == "yes":
            filename = DEFAULT_FILENAME
            remove_duplicates = DEFAULT_DUPLICATES
        else:
            print("Saliendo del programa.")
            sys.exit(0)

    print(f"Se leerán las palabras del fichero {filename}")
    if platform.system() == "Windows":
        script_dir = os.path.dirname(__file__)  # Get the directory of the current script
        file_path = os.path.join(script_dir, filename)
    else:
        file_path = os.path.join(filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"El fichero {filename} no existe")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    print(sort_list(word_list))
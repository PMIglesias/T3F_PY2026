def pausa():
    input("\nPresiona Enter para continuar al siguiente ejercicio...")


def ejercicio_1_division():
    print("\n--- Ej1: División ---")
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = a / b
    except ZeroDivisionError:
        print("Error: No podés dividir por 0.")
    except ValueError:
        print("Error: Debe ingresar números válidos.")
    else:
        print(f"El resultado es: {resultado}")
    finally:
        print("Fin del ejercicio 1.")


def ejercicio_2_suma_mixta():
    print("\n--- Ej2: Suma de número y cadena ---")
    try:
        numero = float(input("Ingrese un número: "))
        cadena = input("Ingrese una cadena de texto: ")
        resultado = numero + cadena
    except TypeError:
        print("Error de tipo: no se puede sumar un número con una cadena.")
    except ValueError:
        print("Error: Debe ingresar un número válido.")
    else:
        print(f"Resultado: {resultado}")
    finally:
        print("Fin del ejercicio 2.")


def ejercicio_3_diccionario():
    print("\n--- Ej3: Acceso a un diccionario ---")
    diccionario = {"nombre": "Juan", "pais": "Argentina"}
    print(f"Claves disponibles: {list(diccionario.keys())}")
    clave = input("Ingrese la clave a buscar: ")
    try:
        valor = diccionario[clave]
    except KeyError:
        print(f"Error: La clave '{clave}' no existe en el diccionario.")
    else:
        print(f"Valor encontrado: {valor}")
    finally:
        print("Fin del ejercicio 3.")


def ejercicio_4_archivo():
    print("\n--- Ej4: Abrir un archivo ---")
    print("Ejemplo: prueba.txt")
    nombre = input("Ingrese el nombre del archivo a abrir: ")
    try:
        with open(nombre, "r", encoding="utf-8") as archivo:
            print("Contenido del archivo:")
            print(archivo.read())
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre}' no existe.")
        print("Creando el archivo...")
        with open(nombre, "w", encoding="utf-8") as archivo:
            archivo.write("Este archivo se creó automáticamente.\n")
        print("Archivo creado con éxito.")
    finally:
        print("Fin del ejercicio 4.")


def ejercicio_5_division_validada():
    print("\n--- Ej5: División con validación ---")
    while True:
        try:
            n1 = float(input("Ingrese el primer número: "))
            n2 = float(input("Ingrese el segundo número: "))
            resultado = n1 / n2
        except ValueError:
            print("Error: Ambos valores deben ser numéricos. Intente de nuevo.")
        except ZeroDivisionError:
            print("Error: No podés dividir por 0. Intente de nuevo.")
        else:
            print(f"El resultado de la división es: {resultado}")
            break
        finally:
            print("Intento procesado.")


if __name__ == "__main__":
    ejercicio_1_division()
    pausa()

    ejercicio_2_suma_mixta()
    pausa()

    ejercicio_3_diccionario()
    pausa()

    ejercicio_4_archivo()
    pausa()

    ejercicio_5_division_validada()

    input("\nFin del programa. Presiona Enter para salir...")
def pausa():
    input("\nPresiona Enter para continuar al siguiente ejercicio...")

def ejercicio_1_mayor():
    print("\nEj1: Mayor de dos números")
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Error: Debe ingresar números válidos.")
        return
    
    mayor = a if a > b else b
    print(f"El mayor es: {mayor}" if a != b else "Los dos números son iguales.")

def buscar_palabra_en_args(palabra, *args):
    resultado = "se encuentra" if palabra in args else "no se encuentra"
    print(f"La palabra '{palabra}' {resultado} en la lista.")

def ejercicio_2_buscar_palabra():
    print("\nEj2: Buscar una palabra (*args)")
    
    lista_palabras = ["sol", "luna", "estrella", "cielo", "nube"]
    
    print(f"Lista disponible para buscar: {lista_palabras}")
    
    palabra_buscar = input("Ingrese la palabra que desea buscar: ").strip().lower()
    
    buscar_palabra_en_args(palabra_buscar, *lista_palabras)

def ejercicio_3_par_impar():
    print("\nEj3: Par o impar")
    try:
        n = int(input("Ingrese un número entero: "))
    except ValueError:
        print("Error: Debe ingresar un número entero.")
        return
    
    tipo = "par" if n % 2 == 0 else "impar"
    print(f"El número {n} es {tipo}.")

def calcular_promedio_args(*args):
    # Consigna 5: Validar cantidad de argumentos
    if len(args) < 2:
        print("Error: No se pasaron suficientes argumentos. Se necesitan al menos 2 números.")
        return
    
    promedio = sum(args) / len(args) if len(args) > 0 else 0
    print(f"El promedio es: {promedio:.2f}")

def ejercicio_4_promedio():
    print("\nEj4: Promedio desde lista (*args)")
    entrada = input("Ingrese números separados por espacio: ")
    
    try:
        numeros = [float(x) for x in entrada.split()]
    except ValueError:
        print("Error: todos los valores deben ser numéricos.")
        return
        
    calcular_promedio_args(*numeros)


if __name__ == "__main__":
    ejercicio_1_mayor()
    pausa()
    
    ejercicio_2_buscar_palabra()
    pausa()
    
    ejercicio_3_par_impar()
    pausa()
    
    ejercicio_4_promedio()
    
    input("\nFin del programa. Presiona Enter para salir...")
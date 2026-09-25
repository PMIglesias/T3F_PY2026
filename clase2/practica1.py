A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("Ej1 Unión")
union = A | B
print(f"A = {A}")
print(f"B = {B}")
print(f"Elementos en A o en B, o en ambos: {union}\n")

input("Presiona Enter para continuar...\n")

print("Ej2 Intersección")
interseccion = A & B
print(f"Elementos comunes en A y en B: {interseccion}\n")

input("Presiona Enter para continuar...\n")

print("Ej3 Diferencia")
diferencia = A - B
print(f"Elementos en A o en B pero no en ambos: {diferencia}\n")

input("Presiona Enter para continuar...\n")

print("Ej4: Subconjuntos")
subconjunto = {1, 2, 3, 4, 5, 6, 7}
es_subconjunto = A.issubset(subconjunto)
print(f"¿Es A ({A}) un subconjunto de B_sub ({subconjunto})?: {es_subconjunto}\n")

input("Presiona Enter para continuar...\n")

print("Ej5: Número de elementos del conjunto A")
cant_elementos = len(A)
print(f"El conjunto A ({A}) tiene {cant_elementos} elementos.")

# 📝 ejercicio2.py
# 🎓 Promedio de notas
# Puntaje: 12 puntos

# Instrucciones:
# 1. Solicita cuántas notas ingresará el usuario.
# 2. Usa un ciclo para pedir las notas una por una y guárdalas en una lista.
# 3. Calcula el promedio con dos decimales.
# 4. Muestra si el promedio es suficiente para aprobar (4.0 o más) o no.
# 5. Todas las notas deben estar entre 1.0 y 7.0.

# 👇 Aquí comienza tu código
cantidad = int(input("¿cuantas notas quiere agregar? "))
notas = []
for i in range(cantidad):
    nota = float(input(f"Ingrese la nota {i+1}: "))
promedio = sum(notas) / cantidad
print(f"El promedio es: {round(promedio, 2)}")
if promedio >= 4.0:
    print("el promedio es suficiente para aprovar")
else:
    print("el promedio no es suficuente para aprobar.")

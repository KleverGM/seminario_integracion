"""
pide cuantos dias registras para cada dia ingrese T(tarde), O(ok) y P(permiso)
cuerta y muestra tardanza totales
"""
dias = int(input("¿cuantos dias vas a cargar?"))
tardes = 0

for i in range(dias):
    marca = input(f"dia {i+1} (T=tarde, O=ok, P=permiso)").strip().upper()
    if marca == "T":
        tardes+=1
print(f"tardanzas totales: ${tardes}")

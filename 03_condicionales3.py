"""
vacaciones por antiguedad pide años de antiguedad y muestra dias de vacaciones segun
<1=0
<3=3
<5=10
>=5=15
"""
antiguedad = float(input("Ingrese sus años de antiguedad: "))

if antiguedad <1:
    dias_vacaciones = 0
    print("No tiene derechoo a vacaciones")
elif antiguedad <3:
    dias_vacaciones = 3
    print(f"tiene derecho a ${dias_vacaciones} dias de vacaciones ")
elif antiguedad <5:
    dias_vacaciones = 10
    print(f"tiene derecho a ${dias_vacaciones} dias de vacaciones ")
elif antiguedad >=5:
    dias_vacaciones = 15
    print(f"tiene derecho a ${dias_vacaciones} dias de vacaciones ")
else:
    print("ingreso un valor incorrecto")
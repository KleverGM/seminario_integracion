salario = float(input("Ingrese su salario: "))
desempeño = int(input("Ingrese su desempeño del 1 al 5: "))
if desempeño == 1:
    total = salario * 0.02
    print(f"su esfuerzo es de ${total + salario}")
elif desempeño == 2:
    total = salario * 0.05
    print(f"su esfuerzo es de ${total + salario}")
elif desempeño ==3:
    total = salario * 0.10
    print(f"su esfuerzo es de ${total + salario}")
elif desempeño == 4:
    total = salario * 0.15
    print(f"su esfuerzo es de ${total + salario}")
else:
    print("Ingrese alguno de los numero solicitados ")
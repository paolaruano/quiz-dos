#Entrada


nombre = input("Ingrese el nombre ")
dias= int(input("Ingrese el numero de dias laborados : "))
salario= int(input("Ingrese el salario : "))

Prima=round(((salario*dias)/360),2)
Cesantias=round(((salario*dias)/360),2)
Intereses=round(((Cesantias*0.12)/dias),2)
Vacaciones=round(((salario*dias)/720),2)
Liquidacion=round((Prima+Cesantias+Intereses+Vacaciones),2)


print(f"Señor {nombre} para los {dias} dias laborados y salario ${salario}"
      f", su liquidacion se compone asi: "
      f"Prima ${Prima}  "
      f"Cesantia ${Cesantias} "
      f"Intereses cesantias ${Intereses} "
      f"Vacaciones: ${Vacaciones} "
      f"Liquidacion: ${Liquidacion} ")


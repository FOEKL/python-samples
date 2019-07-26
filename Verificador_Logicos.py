imposto = float(input("Digite o imposto: "))
if imposto < 10.:
    print("Baixo")
elif imposto >= 10. and imposto <=27.:
    print ( "Medio")
elif imposto > 27. and imposto < 100:
    print ("Alto")
else:
    print("Imposto invalido")

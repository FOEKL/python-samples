salario =  int(input ('Salario: '))
imposto = 27.
while imposto > 0.:
    imposto = input('Imposto ou (0) para sair:')
    #Comando abaixo indica se a variavel imposto for vazia
    if not imposto:
        imposto: 27.
    elif imposto == 's':
        break
    else:
        imposto = float(imposto)
    print( "Valor real: {0}".format(salario - (salario * (imposto * 0.01))))
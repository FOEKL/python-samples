A = [1,1, 3,5,8,13,21,34,55,89]
def lista_menor(lista):
    numero_do_usuario = int(input('Digite o numero desejado:'))
    lista_menor = []
    for elemento in lista:
        if elemento < numero_do_usuario:
            lista_menor.append(elemento)
    print(lista_menor)

if __name__ == "__main__":
    lista_menor(A)
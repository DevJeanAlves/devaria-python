#operador logico "and":
def SecondOperand():
    print("Avaliando o segundo operador-")
    return True
if __name__ == '__main__':
    a = False and SecondOperand()
    print(a)
    b = True and SecondOperand()
    print(b)

#op. selec. "switch e if":
    nome = 'Jean'

    if nome == 'Carlos':
        print('O nome é Carlos')
    elif nome == 'Jean':
        print('O nome é Jean')
    else:
        print('Não é nenhum nome')

#input:
if __name__ == '__main__':
    numero = input("Digite um numero")
    print(f'O numero digitado foi {numero}')


    temperatura = 20
    print(type(temperatura))
    temperatura = "Jean"
    print(temperatura)

    listaNomes = ['Jean', 'Jade', 'Bellinha']
    print(listaNomes)

    idade = 27

    dicionarioPessoa = {
        'nome': 'Jean',
        'idade': idade
    }

    print(dicionarioPessoa)
# Comentário
    numeroComplexo = 5 + 5j
    print(numeroComplexo)

    verificacao = False
    print(type(verificacao))

    varNulla = None
    print(type(varNulla))

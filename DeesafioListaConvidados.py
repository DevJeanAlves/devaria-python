if __name__ == '__main__':
    listaConvidados = ['Jade', 'Jean', "Elena"]

    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade'))

    estaNaLista = nome in listaConvidados
    maiorIdade = idade >= 18

    if estaNaLista:
        if maiorIdade:
            print('Pode entrar, você foi convidado e é maior de idade!')
        else:
            print('Desculpe, seu nome esta na lista, porém não é maior  de idade')
    else:
        print("Desculpe, mas seu nome não esta na lista")
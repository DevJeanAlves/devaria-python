if __name__ == '__main__':
    nota = int(input('Digite sua nota: '))  #convertendo pra int6

    if nota <= 30:
        print('Você foi reprovado!')
    elif nota <= 60:
        print('Você ficou de prova final!')
    else:
        print("Você está aprovado!")
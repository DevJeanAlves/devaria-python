def Validar(valido):
    if valido == True:
        return 'O valor da váriavel é True'
    else:
        return 'O valor da váriavel é False'

if __name__ == '__main__':
    test = True

    respostaDaFuncao = Validar(test)

    print(respostaDaFuncao)
def soma(n1, n2):
    print(f'somando {n1} + {n2}')
    resultado = n1 + n2
    return resultado

def sub(n1, n2):
    print(f'Subitraindo {n1} - {n2}')
    resultado = n1 - n2
    return resultado

def multi(n1, n2):
    print(f'Multiplicando {n1} * {n2}')
    resultado = n1 * n2
    return resultado


def divisao(n1, n2):
    print(f'dividindo {n1} / {n2}')
    resultado = n1 + n2
    return resultado

if __name__ == '__main__':
    n1 = int(input("digite o primeiro numero: "))
    n2 = int(input("Digite o segundo numero: "))

    operador = input("Digite o operdador do calculo(+,-,/,*)")

    if operador == '+':
        resultado = soma(n1, n2)
    elif operador == '-':
        resultado = sub(n1, n2)
    elif operador == '*':
        resultado = multi(n1, n2)
    elif operador == '/':
        resultado = divisao(n1, n2)
    else:
        print("Operador incorreto")


print(f'O resultado é: {resultado}')





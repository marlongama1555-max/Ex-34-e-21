import os

# Variáveis globais
valor: int = 0
dir: str = ''
arq: str = ''


def mult(vlr, tab):
    res = vlr * tab
    return res


def grava(c, rslt):
    global dir, arq

    file: str = ''
    tipo: str = ''
    enc: str = ''
    linha: str = ''

    linha = str(rslt) + '\n'

    if os.path.exists(dir) and os.path.isdir(dir):

        file = os.path.join(dir, arq)

        if os.path.exists(file) and c > 1:
            tipo = 'a'
        else:
            tipo = 'w'

        enc = 'utf-8'

        with open(file, tipo, encoding=enc) as arquivo:
            arquivo.write(linha)


def main():
    global valor

    contador = 1
    result = 0

    valor = int(input('Digite um valor entre 1 e 10: '))

    while valor < 1 or valor > 10:
        valor = int(input('Valor inválido! Digite um valor entre 1 e 10: '))

    global dir, arq
    dir = '/tmp/exercicios'
    arq = 'ex34.txt'

    while contador <= 10:
        result = mult(valor, contador)
        print(valor, 'x', contador, '=', result)
        grava(contador, result)
        contador += 1

        import os

# Variáveis globais
nome: str = ''

nota1: float = 0.0
nota2: float = 0.0
nota3: float = 0.0
nota4: float = 0.0
valor_media: float = 0.0

dir: str = ''
arq: str = ''


def med(n1, n2, n3, n4):
    media: float = 0.0

    media = (n1 + n2 + n3 + n4) / 4

    return media


def escreveArq(caminho, arquivo, linha_cad):
    file: str = ''
    tipo: str = ''
    enc: str = ''

    if os.path.exists(caminho) and os.path.isdir(caminho):

        file = os.path.join(caminho, arquivo)

        if os.path.exists(file):
            tipo = 'a'
        else:
            tipo = 'w'

        enc = 'utf-8'

        with open(file, tipo, encoding=enc) as f:
            f.write(linha_cad)


def cadastro(nm, nt1, nt2, nt3, nt4, vlr_med):
    global dir, arq

    linha: str = ''

    dir = '/tmp/exercicios'
    arq = 'ex21.txt'

    linha = (
        nm + ';' +
        str(nt1) + ';' +
        str(nt2) + ';' +
        str(nt3) + ';' +
        str(nt4) + ';' +
        str(vlr_med) + '\n'
    )

    escreveArq(dir, arq, linha)


def entrada():
    global nome, nota1, nota2, nota3, nota4, valor_media

    nome = input('Digite o nome do aluno: ')

    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))
    nota4 = float(input('Digite a quarta nota: '))

    valor_media = med(nota1, nota2, nota3, nota4)

    print('Média:', valor_media)

    if valor_media >= 6.0:
        print('APROVADO')
    elif valor_media >= 3.0:
        print('EXAME')
    else:
        print('RETIDO')

    cadastro(nome, nota1, nota2, nota3, nota4, valor_media)


def main():
    contador = 0

    while contador < 5:
        entrada()
        contador += 1


main()

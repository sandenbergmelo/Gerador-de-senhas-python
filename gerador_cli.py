from random import shuffle, choice
from string import ascii_letters, digits

symbols  = '@#.,*%+=-!?&'

# Funções
def gerar_senha(letras=8, numeros=4, caracteres_especiais=2):
    generated = ''
    generated += gerar_caracteres(letras, ascii_letters)
    generated += gerar_caracteres(numeros, digits)
    generated += gerar_caracteres(caracteres_especiais, symbols)

    senha = embaralhar_caracteres(generated)
    return senha

def gerar_caracteres(length, chars):
    generated = ''
    for _ in range(length):
        generated += choice(chars)
    return generated

def embaralhar_caracteres(chars):
    chars = list(chars)
    shuffle(chars)
    return ''.join(chars)

def salvar_senha(senha):
    with open('senhas.txt', 'a') as senhas:
        senhas.write(f'{senha}\n')
    return 'Senha salva em senhas.txt'

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('--letras', '-l',type=int, default=8, help='Quantidade de letras')
    parser.add_argument('--numeros', '-n',type=int, default=4, help='Quantidade de números')
    parser.add_argument('--chars', '-c',type=int, default=2, help='Quantidade de caracteres especiais')
    parser.add_argument('--salvar', '-s', type=bool, nargs='?', default=False, help='Salvar senha em arquivo txt')

    args = parser.parse_args()

    senha = gerar_senha(args.letras, args.numeros, args.chars)

    print(senha)

    if args.salvar != False:
        print(salvar_senha(senha))

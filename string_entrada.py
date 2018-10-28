import textwrap
paragrafos = []# lista e amarxernar os paragrafos

numero_paragrafos = int(input('Quantos parágrafos tem o texto?\n'))

#lendo os paragrafos
for c in range(1, numero_paragrafos +1):
    paragrafo = str(input(f'\n parágrafo {c}: \n'))
    paragrafos.append(paragrafo)

#função para justificar o texto
def justifica(texto, tamanho):
    for linha in textwrap.wrap(texto.replace('\n', ''), tamanho):#usanto o textwrap
        por_palavra, sobra = divmod(tamanho - len(linha), linha.count(' '))
        por_palavra *= ' '; sobra *= [' ']
        yield ' '.join(palavra + por_palavra + (sobra.pop() if sobra else '')
            for palavra in linha.split(' ')).rstrip()


#imprimindo os resultados
for paragrafo in paragrafos:
    print('\n'.join(justifica(paragrafo, 40)))
    print(' ')



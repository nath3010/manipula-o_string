import textwrap

paragrafo1 = '''In the beginning God created the heavens and the earth. Now the 
earth was formless and empty, darkness was over the surface of the deep, and 
the Spirit of God was hovering over the waters.'''
paragrafo2 ='''And God said, "Let there be light," and there was light. God saw that the light 
was good, and he separated the light from the darkness. God called the light 
"day," and the darkness he called "night." And there was evening, and there was 
morning - the first day.'''

def justifica(texto, tamanho):
    for linha in textwrap.wrap(texto.replace('\n', ''), tamanho):#usanto o textwrap
        por_palavra, sobra = divmod(tamanho - len(linha), linha.count(' '))
        por_palavra *= ' '; sobra *= [' ']
        yield ' '.join(palavra + por_palavra + (sobra.pop() if sobra else '')
            for palavra in linha.split(' ')).rstrip()


print('\n'.join(justifica(paragrafo1, 40)))
print(' ')
print('\n'.join(justifica(paragrafo2, 40)))



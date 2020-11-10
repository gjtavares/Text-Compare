import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("\nDigite o texto " + str(i) +" (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("\nDigite o texto " + str(i) +" (aperte enter para sair): ")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e devolve o grau de similaridade nas assinaturas.'''
    somatorio = 0
    
    for posicao in range(0,6,1):
        somatorio = abs(as_a[posicao] - as_b[posicao]) +  somatorio
    
    return somatorio/6

def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e devolve a assinatura do texto.'''
    todas_as_sentencas = separa_sentencas(texto)
    todas_as_frases = []
    todas_as_palavras = []

    for sentenca in todas_as_sentencas:
        todas_as_frases = todas_as_frases + separa_frases(sentenca)
    
    for frase in todas_as_frases:
        todas_as_palavras = todas_as_palavras + separa_palavras(frase)
     
    wal = tam_medio_palavra(todas_as_palavras)
    ttr = rel_typetoken(todas_as_palavras)
    hlr = raz_hapaxlegomana(todas_as_palavras)
    sal = tam_medio_sentecas(todas_as_sentencas)
    sac = len(todas_as_frases)/len(todas_as_sentencas)
    pal = tam_medio_frase(todas_as_frases)

    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e devolve o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    numtotal_textos = len(textos)
    num_texto = 0
    grau_similaridade = []
    while num_texto < numtotal_textos:
        assinatura_texto = calcula_assinatura(textos[num_texto])
        grau_similaridade.append(compara_assinatura(ass_cp, assinatura_texto))
        num_texto+=1
    
    infectado_COHPIAH = 0

    for texto in range(1,numtotal_textos,1):
        if grau_similaridade[texto] < grau_similaridade[infectado_COHPIAH]:
            infectado_COHPIAH = texto
    
    return infectado_COHPIAH + 1
        
def tam_medio_palavra(todas_as_palavras):
    '''Função resposável por calcular o tamanho médios das palavras'''
    num_palavras = len(todas_as_palavras)
    soma_tam_palavras = 0
    for palavra in todas_as_palavras:
        soma_tam_palavras = len(palavra) + soma_tam_palavras
    
    return soma_tam_palavras/num_palavras

def rel_typetoken(todas_as_palavras):
    '''Função resposável por calcular a relação Type-Token - Número de palavras diferentes dividido pelo total de palavras'''
    num_palavras_dif = n_palavras_diferentes(todas_as_palavras)
    return num_palavras_dif/len(todas_as_palavras)

def raz_hapaxlegomana(todas_as_palavras):
    '''Fyunção responsável por calcular razão Hapax Legoma - Número de palavras que aparecem uma unica vez dividido pelo total de palavras'''
    num_palavras_unicas = n_palavras_unicas(todas_as_palavras)
    return num_palavras_unicas/len(todas_as_palavras)

def tam_medio_sentecas(todas_as_sentencas):
    '''Função responsável por calcular o tamanho médio das sentenças'''
    num_setencas = len(todas_as_sentencas)
    num_total_caracteres = 0
    for sentenca in todas_as_sentencas:
        num_total_caracteres = num_total_caracteres + len(sentenca)
    
    return num_total_caracteres/num_setencas

def tam_medio_frase(todas_as_frases):
    '''Função responsável por calcular o tamanho médio das frases''' 
    tot_caracteres = 0
    for frase in todas_as_frases:
        tot_caracteres = tot_caracteres + len(frase)
    
    return tot_caracteres/len(todas_as_frases)

def main():
    '''Função principal'''
    assinatura_referencia = le_assinatura()
    textos = le_textos()
    infectado = avalia_textos(textos,assinatura_referencia)

    print('\nO autor do texto', infectado, 'está infectado com COH-PIAH')

main()
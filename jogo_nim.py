def main():
    print('Bem-vindo ao jogo do NIM! Escolha:')
    print('1 - para jogar partida isolada')
    print('2 - para jogar um campeonato')

    Escolha = int(input())

    if(Escolha==1):
        print('Você escolheu uma partida isolada!')
        partida()
    else:
        print('Você escolheu um campeonato!')
        campeonato()

def campeonato():
    rodada = 1
    while rodada <= 3:
        print('\n**** Rodada', rodada, ' ****')
        partida()
        rodada+=1
    print('\n\n**** Final do Campeonato! ****')
    print('\n\nPlacar: Você 0 X 3 Computador')

def partida():
    n_menor_que_m = True
    while n_menor_que_m:
        n = int(input('Informe o numero de peças: '))
        m = int(input('Informe o limite de peça por jogada: '))
        if(n>=m):
            n_menor_que_m = False
        else:
            print('\nn precisa ser menor ou igual a m\n')
    if(n%(m+1)==0):
        print('\nVocê começa!')
        UsuarioJoga = True
        while n>0:
            if(UsuarioJoga):
                n = n - usuario_escolhe_jogada(n,m)
                UsuarioJoga = False
                if(n==0): print()
                elif(n>1):
                    print('Restam', n, 'peças.\n')
                else:
                    print('Resta apenas', n, 'peça!\n')
            else:
                n = n - computador_escolhe_jogada(n,m)
                UsuarioJoga = True
                if(n==0): print()
                elif(n>1):
                    print('Restam', n, 'peças.\n')
                else:
                    print('Resta apenas', n, 'peça!\n')     
    else:
        print('\nComputador começa!')
        ComputadorJoga = True
        while n>0:
            if(ComputadorJoga):
                n = n - computador_escolhe_jogada(n,m)
                ComputadorJoga = False
                if(n==0): print()
                elif(n>1):
                    print('Restam', n, 'peças.\n')
                else:
                    print('Resta apenas', n, 'peça!\n')
            else:
                n = n - usuario_escolhe_jogada(n,m)
                ComputadorJoga = True
                if(n==0): print()
                elif(n>1):
                    print('Restam', n, 'peças.\n')
                else:
                    print('Resta apenas', n, 'peça!\n')
    
    print('Fim do Jogo. O computador Venceu!!!')


def computador_escolhe_jogada(n,m):
    i = m - 1
    num_max = True
    if(n<=m):
        if(n>1):
            print('\nComputador retirou', n, 'peças!')
        else:
            print('\nComputador retirou', n, 'peça!')
        return n
    else:
        while i > 0:
            if((n-(m-i))%(m+1)==0):
                num_max = False
                break
            else:
                i-=1

        if(num_max):
            if(m>1):
                print('\nComputador retirou', m, 'peças!')
            else:
                print('\nComputador retirou', m, 'peça!')
            return m
        else:
            if((m-i)>1):
                print('\nComputador retirou', (m-i), 'peças!')
            else:
                print('\nComputador retirou', (m-i), 'peça!')
            return (m-i)

def usuario_escolhe_jogada(n,m):
    EscolhaUsuario = int(input('Quantas peças irá retirar? '))
    while (EscolhaUsuario > m) or (EscolhaUsuario <= 0):
        print('Jogada Invalida! Tente novamente!')
        EscolhaUsuario = int(input('Quantas peças irá retirar? '))
    
    if(EscolhaUsuario>1):
        print('\nVocê retirou', EscolhaUsuario, 'peças!')
        return EscolhaUsuario
    else:
        print('\nVocê retirou', EscolhaUsuario, 'peça!')
        return EscolhaUsuario

main()
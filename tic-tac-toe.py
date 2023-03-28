#Goncalo Carmo 99228

def eh_tabuleiro(tab):
    '''Esta funcao recebe um argumento e devolve True se o argumento corresponde a um tabuleiro, caso contrario, devolve False.'''
    count=0
    if isinstance(tab, tuple):
        for i in range(len(tab)):
            if isinstance(tab[i], tuple):
                for c in tab[i]:
                    if c in range (-1,2) and type(c)==int:
                        count+=1
    return count==9

def eh_posicao(p):
    '''Esta funcao recebe um argumento e devolve True se o argumento corresponde a uma posicao no tabuleiro, caso contrario, devolve false.'''
    return p in range(1,10) and type(p)==int

def obter_coluna(tab, c):
    '''Esta funcao recebe um tabuleiro e um inteiro de 1 a 3 que corresponde ao numero da coluna e devolve a respetiva coluna.'''
    if eh_tabuleiro(tab) and c in range(1,4) and type(c)==int:
        c-=1
        col=tuple()
        for i in range(len(tab)):
            col=col+(tab[i][c],)
        return col        
    raise ValueError ('obter_coluna: algum dos argumentos e invalido')

def obter_linha(tab, l):
    '''Esta funcao recebe um tabuleiro e um inteiro de 1 a 3 que corresponde ao numero da linha e devolve a respetiva linha.'''
    if eh_tabuleiro(tab) and l in range(1,4) and type(l)==int:
        l-=1
        linh= tab[l]
        return linh
    raise ValueError ('obter_linha: algum dos argumentos e invalido')

def obter_diagonal(tab, d):
    '''Esta funcao recebe um tabuleiro e um inteiro que corresponde a orientacao da diagonal, sendo 1 a diagonal descendente da esquerda para a direita, e 2 a diagonal ascendente da esuerda para a direita, e devolve um tuplo com os valores dessa diagonal.'''
    if eh_tabuleiro(tab) and d in range(1,3) and type(d)==int:
        diag=tuple()
        if d==1:
            for i in range(len(tab)):
                diag=diag+(tab[i][i],)
            return diag
        else:
            x=2
            for i in range(len(tab)):
                diag=diag+(tab[x][i],)
                x-=1
            return diag
    raise ValueError ('obter_diagonal: algum dos argumentos e invalido')

def tabuleiro_str(tab):
    '''Esta funcao recebe um tabuleiro e devolve a sua representacao na forma de uma string.'''
    if eh_tabuleiro(tab):
        string=''
        for i in range(len(tab)):
            for c in range(len(tab[i])):
                if tab[i][c]==1:
                    symb='X'
                elif tab[i][c]==0:
                    symb=' '
                else:
                    symb='O'
                string+=' '+symb+' '
                if c != 2:
                    string+='|'
            if i != 2:
                string+='\n-----------\n'
        return (string)
    raise ValueError ('tabuleiro_str: o argumento e invalido') 

def eh_posicao_livre(tab, p):
    '''Esta funcao recebe um tabuleiro e uma posicao e devolve True se essa posicao estiver livre, caso contrario, devolve False.'''
    if eh_tabuleiro(tab) and eh_posicao(p):
        p-=1
        return tab[p//3][p%3]==0
    raise ValueError ('eh_posicao_livre: algum dos argumentos e invalido')

def obter_posicoes_livres(tab):
    '''Esta funcao recebe um tabuleiro e devolve um tuplo ordenado com todas as suas posicoes livres.'''
    if eh_tabuleiro(tab):
        tot_livres=tuple()
        for p in range (1,10):
            if eh_posicao_livre(tab, p):
                tot_livres=tot_livres+(p,)
        return(tot_livres)
    raise ValueError ('obter_posicoes_livres: o argumento e invalido')
        
def jogador_ganhador(tab):
    '''Esta funcao recebe um tabuleiro e devole um inteiro que corresponde ao jogador que venceu a partida no tabuleiro fornecido, sendo o valor 1 se o vencedor for o jogador 'X' e -1 se vencedor for o jogador'O'.'''
    if eh_tabuleiro(tab):
        for c in range(1,4):
            col=obter_coluna(tab,c)
            if col==(1,1,1):
                return 1
            if col==(-1,-1,-1):
                return -1
            lnh=obter_linha(tab,c)
            if lnh==(1,1,1):
                return 1
            if lnh==(-1,-1,-1):
                return -1
        for d in range(1,3):
            diag=obter_diagonal(tab,d)
            if diag==(1,1,1):
                return 1
            if diag==(-1,-1,-1):
                return -1
        return 0
    raise ValueError ('jogador_ganhador: o argumento e invalido')

def marcar_posicao(tab,j,p):
    '''Esta funcao recebe um tabueiro, um inteiro identificando o jogador, 1 para 'X' ou -1 para 'O', e uma posicao livre, e devolve um tabuleiro com a posicao indicada marcada com o simbolo do jogador'''
    if eh_tabuleiro(tab) and eh_posicao(p) and eh_posicao_livre(tab,p) and j in (-1,1) and type(j)==int:
        p-=1
        list_tab=list(tab)
        list_lnh=list(tab[p//3])
        list_lnh[p%3]=j
        list_tab[p//3]=tuple(list_lnh)
        tab=tuple(list_tab)
        return tab
    raise ValueError ('marcar_posicao: algum dos argumentos e invalido')
    
def escolher_posicao_manual(tab):
    '''Esta funcao pede ao utilizador uma posicao e verifica se e possivel fazer uma jogada nessa mesma posicao.'''
    if eh_tabuleiro(tab):
        p=eval(input('Turno do jogador. Escolha uma posicao livre: '))
        if eh_posicao(p) and eh_posicao_livre(tab,p):
            return p
        else: raise ValueError('escolher_posicao_manual: a posicao introduzida e invalida')
    raise ValueError ('escolher_posicao_manual: o argumento e invalido')

def jog_vitoria(tab,j):
    '''Esta funcao recebe um tabuleiro e um inteiro identificando o jogador, 1 para 'X' ou -1 para 'O', e analisa o tabuleiro para verificar se o jogador tem duas pecas em linha e uma posicao livre, se tiver, devolve essa posicao livre.'''
    for l in range(1,4):
        lnh=obter_linha(tab,l)
        if lnh in ((j,j,0),(0,j,j),(j,0,j)):
            for p in range(len(lnh)):
                if lnh[p]==0:
                    return p+1+(l-1)*3
    for c in range(1,4):
        col=obter_coluna(tab,c)
        if col in ((j,j,0),(0,j,j),(j,0,j)):
            for p in range(len(col)):
                if col[p]==0:
                    return p*3+c
    for d in range(1,3):
        diag=obter_diagonal(tab,d)
        if diag in ((j,j,0),(0,j,j),(j,0,j)):
            for p in range(len(diag)):
                if diag[p]==0:
                    return 1+6*(d-1)+p*(4-(d-1)*6)
    return 0
                    
def jog_bloqueio(tab,j):
    '''Esta funcao recebe um tabuleiro e um inteiro identificando o jogador, 1 para 'X' ou -1 para 'O', e analisa o tabuleiro para verificar se o jogador adversario tem duas pecas em linha e uma posicao livre, se tiver, devolve essa posicao livre.'''
    return jog_vitoria(tab,-j)

def jog_bifurcacao(tab,j):
    '''Esta funcao recebe um tabuleiro e um inteiro identificando o jogador, 1 para 'X' ou -1 para 'O', e analisa o tabuleiro para verificar se o jogador tem duas linhas/colunas/diagonais que se intersetam, em que cada uma tem uma das suas pecas, se a posicao de intersecao estiver livre, devolve essa posicao.'''
    livres=obter_posicoes_livres(tab)
    for p in livres:
        tabTeste=marcar_posicao(tab,j,p)
        testeVitoria=jog_vitoria(tabTeste,j)
        if testeVitoria!=0:
            tabTeste=marcar_posicao(tabTeste,-j,testeVitoria)
            if jog_vitoria(tabTeste,j)!=0:
                return p
    return 0

def jog_bloq_bifurcacao(tab,j):
    '''Esta funcao recebe um tabuleiro e um inteiro identificando o jogador, 1 para 'X' ou -1 para 'O', e analisa o tabuleiro para verificar se o jogador adversario tem uma bifurcacao, se tiver apenas uma, devolve a posicao que bloqueia essa bifurcacao, senao, devolve a posicao que permite criar um dois em linha para forcar o adversario a defender, desde que a defesa nao resulte noutra bifurcacao para o adversario.'''
    bifurc=jog_bifurcacao(tab,-j)
    livres=obter_posicoes_livres(tab)
    if bifurc!=0:
        totBifurc=tuple()
        totBifurc+=(bifurc,)
        for p in livres:
            if p>bifurc:
                tabTeste=marcar_posicao(tab,-j,p)
                testeVitoria=jog_vitoria(tabTeste,-j)
                if testeVitoria!=0:
                    tabTeste=marcar_posicao(tabTeste,j,testeVitoria)
                    if jog_vitoria(tabTeste,-j)!=0:
                        totBifurc+=(p,)
        if len(totBifurc)==1:
            return jog_bifurcacao(tab,-j)
        posPossiveis=tuple()
        for posBifurc in totBifurc:
            novTab=marcar_posicao(tab,-j,posBifurc)
            for livre in obter_posicoes_livres(novTab):
                tabVitoria=marcar_posicao(novTab,j,livre)
                if jog_vitoria(tabVitoria,j)!=0:
                    if jog_vitoria(tabVitoria,j) not in totBifurc:
                        posPossiveis+=(livre,)
        posPossiveis=sorted(posPossiveis)
        return posPossiveis[0]
    return 0

def jog_centro(tab,j):
    '''Esta funcao recebe um tabuleiro e um inteiro identificando o jogador, 1 para 'X' ou -1 para 'O', e analisa o tabuleiro para verificar se a posicao central do tabuleiro introduzido esta livre, se sim devolve essa mesma posicao.'''
    livre=obter_posicoes_livres(tab)
    if 5 in livre:
        return 5  
    return 0

def jog_canto_oposto(tab,j):
    '''Esta funcao recebe um tabuleiro e um inteiro identificando o jogador, 1 para 'X' ou -1 para 'O', e analisa o tabuleiro para verificar se o adversario tem um simbolo num dos cantos, se sim, devolve a posicao do canto oposto.'''
    for d in range(1,3):
        diag=obter_diagonal(tab,d)
        if diag[0]==-j and eh_posicao_livre(tab,1+6*(d-1)+2*(4-(d-1)*6)):
            return 1+6*(d-1)+2*(4-(d-1)*6)
        if diag[2]==-j and eh_posicao_livre(tab,1+6*(d-1)):
            return 1+6*(d-1)
    return 0

def jog_canto_vazio(tab,j):
    '''Esta funcao recebe um tabuleiro e um inteiro identificando o jogador, 1 para 'X' ou -1 para 'O', e analisa o tabuleiro para verificar se um canto esta livre, se sim, joga nesse canto.'''
    livre=obter_posicoes_livres(tab)
    if 1 or 3 or 7 or 9 in livre:
        for p in (1,3,7,9):
            if eh_posicao_livre(tab,p):
                return p
    return 0
        
def jog_lateral_vazio(tab,j):
    '''Esta funcao recebe um tabuleiro e um inteiro identificando o jogador, 1 para 'X' ou -1 para 'O', e analisa o tabuleiro para verificar se uma posicao lateral (nao e canto nem o centro) esta livre, se sim, devolve essa posicao.'''
    livre=obter_posicoes_livres(tab)
    if 2 or 4 or 6 or 8 in livre:
        for p in (2,4,6,8):
            if eh_posicao_livre(tab,p):
                return p
    return 0       
            
def strat_basico(tab,j):
    '''Esta funcao recebe um tabuleiro e um inteiro identificando o jogador, 1 para 'X' ou -1 para 'O', e realiza a estrategia 'basico' que segue os criterios das funcoes jog_centro, jog_canto_vazio e jog_lateral_vazio, respetivamente, devolvendo a posicao obtida na primeira funcao que nao obtem um resultado nulo.'''
    if jog_centro(tab,j)!=0:
        return jog_centro(tab,j)
    if jog_canto_vazio(tab,j)!=0:
        return jog_canto_vazio(tab,j)
    if jog_lateral_vazio(tab,j)!=0:
        return jog_lateral_vazio(tab,j)
            
def strat_normal(tab,j):
    '''Esta funcao recebe um tabuleiro e um inteiro identificando o jogador, 1 para 'X' ou -1 para 'O', e realiza a estrategia 'normal' que segue os criterios das funcoes jog_vitoria, jog_bloqueio, jog_centro, jog_canto_oposto, jog_canto_vazio e jog_lateral_vazio, respetivamente, devolvendo a posicao obtida na primeira funcao que nao obtem um resultado nulo.'''
    if jog_vitoria(tab,j)!=0:
        return jog_vitoria(tab,j)
    if jog_bloqueio(tab,j)!=0:
        return jog_bloqueio(tab,j)
    if jog_centro(tab,j)!=0:
        return jog_centro(tab,j)
    if jog_canto_oposto(tab,j)!=0:
        return jog_canto_oposto(tab,j)
    if jog_canto_vazio(tab,j)!=0:
        return jog_canto_vazio(tab,j)
    if jog_lateral_vazio(tab,j)!=0:
        return jog_lateral_vazio(tab,j)
    
def strat_perfeito(tab,j):
    '''Esta funcao recebe um tabuleiro e um inteiro identificando o jogador, 1 para 'X' ou -1 para 'O', e realiza a estrategia 'perfeito' que segue os criterios das funcoes jog_vitoria, jog_bloqueio, jog_bifurcacao, jog_bloq_bifurcacao, jog_centro, jog_canto_oposto, jog_canto_vazio e jog_lateral_vazio, respetivamente, devolvendo a posicao obtida na primeira funcao que nao obtem um resultado nulo.'''
    if jog_vitoria(tab,j)!=0:
        return jog_vitoria(tab,j)
    if jog_bloqueio(tab,j)!=0:
        return jog_bloqueio(tab,j)
    if jog_bifurcacao(tab,j)!=0:
        return jog_bifurcacao(tab,j)
    if jog_bloq_bifurcacao(tab,j)!=0:
        return jog_bloq_bifurcacao(tab,j)
    if jog_centro(tab,j)!=0:
        return jog_centro(tab,j)
    if jog_canto_oposto(tab,j)!=0:
        return jog_canto_oposto(tab,j)
    if jog_canto_vazio(tab,j)!=0:
        return jog_canto_vazio(tab,j)
    if jog_lateral_vazio(tab,j)!=0:
        return jog_lateral_vazio(tab,j)    
    
def escolher_posicao_auto(tab,j,strat):
    '''Esta funcao recebe um tabuleiro, um inteiro identificando o jogador, 1 para 'X' ou -1 para 'O', e uma cadeia de caracteres identificando uma estrategia, que pode ser 'basico', 'normal' ou 'perfeito', e devolve a posicao escolhida automaticamente em funcao da estrategia especificada.'''
    if eh_tabuleiro(tab) and (j in (-1,1)) and type(j)==int:
        if strat=='basico':
            return strat_basico(tab,j)
        if strat=='normal':
            return strat_normal(tab,j)
        if strat=='perfeito':
            return strat_perfeito(tab,j)
    raise ValueError('escolher_posicao_auto: algum dos argumentos e invalido')

def jogador_primeiro(jog,strat,tab):
    '''Esta funcao recebe um inteiro identificando o jogador humano, 1 para 'X' ou -1 para 'O', uma cadeia de caracteres identificando uma estrategia, que pode ser 'basico', 'normal' ou 'perfeito' e um tabuleiro, e permite jogar um jogo completo do Jogo do Galo onde o jogador humano joga primeiro, devolve a cadeia de caracteres correspondente ao jogador vencedor ('X' ou 'O') ou , caso se esgotem as posicoes livres, devolve 'EMPATE' '''
    j=1
    while jogador_ganhador(tab)==0:
        p=escolher_posicao_manual(tab)
        tab=marcar_posicao(tab,j,p)
        print(tabuleiro_str(tab))
        if obter_posicoes_livres(tab)==():
            break
        if jogador_ganhador(tab)==0:
            print('Turno do computador ('+strat+'):')
            p=escolher_posicao_auto(tab,-j,strat)
            tab=marcar_posicao(tab,-j,p)
            print(tabuleiro_str(tab))
        if obter_posicoes_livres(tab)==():
            break
    if jogador_ganhador(tab)==1:
        return jog
    elif jogador_ganhador(tab)==-1:
        return 'O'
    return 'EMPATE'    

def pc_primeiro(jog,strat,tab):
    '''Esta funcao recebe um inteiro identificando o jogador humano, 1 para 'X' ou -1 para 'O', uma cadeia de caracteres identificando uma estrategia, que pode ser 'basico', 'normal' ou 'perfeito' e um tabuleiro, e permite jogar um jogo completo do Jogo do Galo onde o computador joga primeiro, devolve a cadeia de caracteres correspondente ao jogador vencedor ('X' ou 'O') ou , caso se esgotem as posicoes livres, devolve 'EMPATE' '''
    j=-1
    while jogador_ganhador(tab)==0:
        print('Turno do computador ('+strat+'):')
        p=escolher_posicao_auto(tab,-j,strat)
        tab=marcar_posicao(tab,-j,p)
        print(tabuleiro_str(tab))
        if obter_posicoes_livres(tab)==():
            break        
        if jogador_ganhador(tab)==0:
            p=escolher_posicao_manual(tab)
            tab=marcar_posicao(tab,j,p)
            print(tabuleiro_str(tab))
        if obter_posicoes_livres(tab)==():
            break
    if jogador_ganhador(tab)==-1:
        return jog
    elif jogador_ganhador(tab)==1:
        return 'X'
    return 'EMPATE'

def jogo_do_galo(jog,strat):
    '''Esta funcao recebe um inteiro identificando o jogador humano, 1 para 'X' ou -1 para 'O', uma cadeia de caracteres identificando uma estrategia, que pode ser 'basico', 'normal' ou 'perfeito', e permite jogar um jogo completo do Jogo do Galo de um jogador contra o computador e devolve a cadeia de caracteres correspondente ao jogador vencedor ('X' ou 'O') ou , caso se esgotem as posicoes livres, devolve 'EMPATE' '''
    if jog in ('X','O') and strat in ('basico','normal','perfeito'):
        print("Bem-vindo ao JOGO DO GALO.\nO jogador joga com '"+jog+"'.")
        tab=((0,0,0),(0,0,0),(0,0,0))
        if jog=='X':
            return jogador_primeiro(jog,strat,tab)
        if jog=='O':
            return pc_primeiro(jog,strat,tab)
        raise ValueError('jogo_do_galo: algum dos argumentos e invalido')
    
jogo_do_galo(1, 'normal')
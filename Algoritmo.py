from funcoes import opc_1_a_3
# A FAZER:
# cor da agua, odor etc tudo será função
# antes de confirmar, mostrar lista organizada com as respostas
# pedir pra confirmar tudo ao final é mais fácil do que confirmar a cada etapa

def titulo():
    print('QUANTIFICAÇÃO DA ANÁLISE DOS PARÂMETROS MACROSCÓPIOS')
    print('-='*30)

def cabecalho(msg):
    print('')
    print('='*30)
    print(f'{msg:^30}')
    print('='*30)


titulo()
dict = {}
confirmar = ''
while confirmar != 's':
    cabecalho('COR DA ÁGUA')
    opc_1_a_3('Escura', 'Clara', 'Transparente')
    dict['cor_da_agua'] = int(input('Insira o n° relativo a Cor da Água:'))

    cabecalho('ODOR')
    opc_1_a_3('Cheiro Forte', 'Cheiro Fraco', 'Sem cheiro')
    dict['odor_da_agua'] = int(input('Insira o n° relativo ao Odor da Água:'))


    cabecalho('LIXO')
    opc_1_a_3('Muito', 'Pouco', 'Sem lixo')
    dict['lixo'] = int(input('Insira o n° relativo ao Lixo ao Redor:'))


    cabecalho('MATERIAIS FLUTUANTES')
    opc_1_a_3('Muito', 'Pouco', 'Sem materiais')
    dict['materiais_flutuantes'] = int(input('Insira o n° relativo a presença de Materiais Flutuantes:'))


    cabecalho('ESPUMAS')
    opc_1_a_3('Muito', 'Pouco', 'Sem espuma')
    dict['espumas'] = int(input('Insira o n° relativo a presença de Espuma:'))


    cabecalho('ÓLEOS')
    opc_1_a_3('Muito', 'Pouco', 'Sem óleos')
    dict['oleos'] = int(input('Insira o n° relativo a presença de Óleos:'))


    cabecalho('ESGOTO')
    opc_1_a_3('Esgoto doméstico', 'Fluxo Superficial', 'Sem esgoto')
    dict['esgoto'] = int(input('Insira o n° relativo a presença de Esgoto:'))


    cabecalho('VEGETAÇÃO(PRESERVAÇÃO)')
    opc_1_a_3('Alta degradação', 'Baixa degradação', 'Preservada')
    dict['vegetacao'] = int(input('Insira o n° relativo a presença de Vegetação:'))


    cabecalho('USO POR ANIMAIS')
    opc_1_a_3('Presença', 'Apenas marcas', 'Não detectado')
    dict['animais'] = int(input('Insira o n° relativo a presença de Animais:'))


    cabecalho('USO POR HUMANOS')
    opc_1_a_3('Presença', 'Apenas marcas', 'Não detectado')
    dict['humanos'] = int(input('Insira o n° relativo a presença de humanos:'))


    cabecalho('PROTEÇÃO DO LOCAL')
    opc_1_a_3('Sem proteção', 'Com proteção e acesso', 'Com proteção sem acesso')
    dict['protecao'] = int(input('Insira o n° relativo a presença a Proteção do Local:'))


    cabecalho('PROXIMIDADE COM RESIDÊNCIA OU ESTABELECIMENTO')
    opc_1_a_3('Menos de 50 metros', 'Entre 50 e 100 metros', 'Mais de 100 metros')
    dict['residencias'] = int(input('Insira o n° relativo à proximidade de residências ou estabelecimentos:'))


    cabecalho('TIPO DE ÁREA DE INSERÇÃO')
    opc_1_a_3('Ausente', 'Propriedade privada', 'Parques ou áreas protegidas')
    dict['insercao'] = int(input('Insira o n° relativo tipo de área de inserção da nascente:'))


    print(dict)
    confirmar = str(input('Confirma as informações? [S/N]')).strip().lower()


resultado = (sum(dict.values()))

print(resultado)



#CLASSIFICAÇÃO
#CLASSE ABCDE
#GRAU ÓTIMO,BOA,RAZOÁVEL,RUIM,PÉSSIMO
#PONTUAÇÃO
#37 A 39, 34 A 36, 31 A 33, 28 A 30, ABAIXO DE 28

if resultado >= 37 and resultado <= 39:
    print('Classe: A')
    print('Grau: Ótimo')

elif resultado >= 34 and resultado <= 36:
    print('Classe: B')
    print('Grau: Bom')

elif resultado >= 31 and resultado <= 33:
    print('Classe: C')
    print('Grau: Razoável')

elif resultado >= 28 and resultado <= 30:
    print('Classe: D')
    print('Grau: Ruim')

elif resultado < 28:
    print('Classe: E')
    print('Grau: Péssimo')




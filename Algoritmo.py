def titulo():
    print('-=' * 50)
    print(f"{'QUANTIFICAÇÃO DA ANÁLISE DOS PARÂMETROS MACROSCÓPIOS':^100}")
    print('-='*50)
    print('Algoritmo elaborado a partir da metodologia disponível em:\nGOMES, P. M.; MELO, C. de; VALE, V. S. do. Avaliação dos impactos ambientais em nascentes na cidade\n de Uberlândia-MG: análise macroscópica. Sociedade & Natureza, [S. l.], v. 17, n. 32, 2006.\n Disponível em: https://seer.ufu.br/index.php/sociedadenatureza/article/view/9169. ')
    print('')
    print('Instruções: Responder as perguntas com valor de 1 a 3.')
    print('='*100)
    print(f"{'QUESTIONÁRIO':^100}")
    print('='*100)
    

def cabecalho(msg):
    print('')
    print('-'*100)
    print(f'{msg:^40}')
    print('-'*100)

def opc_1_a_3(opc1,opc2,opc3):
    print('OPÇÕES: [1]', opc1,'[2]',opc2,'[3]',opc3)

titulo()
dict = {}
confirmar = ''

while confirmar != 's':
    cabecalho('COR DA ÁGUA')
    opc_1_a_3('Escura', 'Clara', 'Transparente')
    dict['cor_da_agua'] = int(input('>Insira o n° relativo a Cor da Água:'))

    cabecalho('ODOR')
    opc_1_a_3('Cheiro Forte', 'Cheiro Fraco', 'Sem cheiro')
    dict['odor_da_agua'] = int(input('>Insira o n° relativo ao Odor da Água:'))


    cabecalho('LIXO')
    opc_1_a_3('Muito', 'Pouco', 'Sem lixo')
    dict['lixo'] = int(input('>Insira o n° relativo ao Lixo ao Redor:'))


    cabecalho('MATERIAIS FLUTUANTES')
    opc_1_a_3('Muito', 'Pouco', 'Sem materiais')
    dict['materiais_flutuantes'] = int(input('>Insira o n° relativo a presença de Materiais Flutuantes:'))


    cabecalho('ESPUMAS')
    opc_1_a_3('Muito', 'Pouco', 'Sem espuma')
    dict['espumas'] = int(input('>Insira o n° relativo a presença de Espuma:'))


    cabecalho('ÓLEOS')
    opc_1_a_3('Muito', 'Pouco', 'Sem óleos')
    dict['oleos'] = int(input('>Insira o n° relativo a presença de Óleos:'))


    cabecalho('ESGOTO')
    opc_1_a_3('Esgoto doméstico', 'Fluxo Superficial', 'Sem esgoto')
    dict['esgoto'] = int(input('>Insira o n° relativo a presença de Esgoto:'))


    cabecalho('VEGETAÇÃO(PRESERVAÇÃO)')
    opc_1_a_3('Alta degradação', 'Baixa degradação', 'Preservada')
    dict['vegetacao'] = int(input('>Insira o n° relativo a presença de Vegetação:'))


    cabecalho('USO POR ANIMAIS')
    opc_1_a_3('Presença', 'Apenas marcas', 'Não detectado')
    dict['animais'] = int(input('>Insira o n° relativo a presença de Animais:'))


    cabecalho('USO POR HUMANOS')
    opc_1_a_3('Presença', 'Apenas marcas', 'Não detectado')
    dict['humanos'] = int(input('>Insira o n° relativo a presença de humanos:'))


    cabecalho('PROTEÇÃO DO LOCAL')
    opc_1_a_3('Sem proteção', 'Com proteção e acesso', 'Com proteção sem acesso')
    dict['protecao'] = int(input('>Insira o n° relativo a presença a Proteção do Local:'))


    cabecalho('PROXIMIDADE COM RESIDÊNCIA OU ESTABELECIMENTO')
    opc_1_a_3('Menos de 50 metros', 'Entre 50 e 100 metros', 'Mais de 100 metros')
    dict['residencias'] = int(input('>Insira o n° relativo à proximidade de residências ou estabelecimentos:'))


    cabecalho('TIPO DE ÁREA DE INSERÇÃO')
    opc_1_a_3('Ausente', 'Propriedade privada', 'Parques ou áreas protegidas')
    dict['insercao'] = int(input('>Insira o n° relativo tipo de área de inserção da nascente:'))

    print('-=' * 50)
    print('Confira as informações:')
    for k, v in dict.items():
        print(f'> A pergunta: {k} tem o valor: {v}')
    print('-='*50)
    confirmar = str(input('Confirma as informações? Digite [S] ou qualquer tecla para sair')).strip().lower()

resultado = (sum(dict.values()))


if resultado >= 37 and resultado <= 39:
    print('='*100)
    print(f'RESULTADO:{resultado}')
    print('='*100)
    print('CLASSE: A')
    print('GRAU: Ótimo')

elif resultado >= 34 and resultado <= 36:
    print('=' * 100)
    print(f'RESULTADO:{resultado}')
    print('=' * 100)
    print('CLASSE: B')
    print('GRAU: Bom')

elif resultado >= 31 and resultado <= 33:
    print('=' * 100)
    print(f'RESULTADO:{resultado}')
    print('=' * 100)
    print('Classe: C')
    print('GRAU: Razoável')

elif resultado >= 28 and resultado <= 30:
    print('=' * 100)
    print(f'RESULTADO:{resultado}')
    print('=' * 100)
    print('CLASSE: D')
    print('GRAU: Ruim')

elif resultado <= 27:
    print('=' * 100)
    print(f'RESULTADO:{resultado}')
    print('=' * 100)
    print('CLASSE: E')
    print('GRAU: Péssimo')

else:
    print('Resultado não encontrado, por favor refaça o questionário.')



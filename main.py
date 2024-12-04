lv_1 = [{'alimento':'Café','preco':'4'},
        {'alimento':'Leite','preco':'5'},
        {'alimento':'Óleo Vegetal','preco':'3'},
        {'alimento':'Pão Francês','preco':'3'}
        ]

lv_2 = [{'alimento':'Azeite de Oliva','preco':'17'},
        {'alimento':'Chocolate','preco':'9'},
        {'alimento':'Bisnaguinha','preco':'5'},
        {'alimento':'Kinder Ovo','preco':'10'}
        ]

lista_alimento = lv_1
player = 1
xp = 0

for alimento in lista_alimento:
        nome_alim = alimento['alimento']
        preco_alim = alimento['preco']

print (player)
print(f'* {nome_alim} | R${preco_alim}')

player = 2
if player == 2:
    lista_alimento = lv_1 + lv_2

    for alimento in lista_alimento:
        nome_alim = alimento['alimento']
        preco_alim = alimento['preco'] 
    
    print (player)
    print (lista_alimento)

   



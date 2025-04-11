print("Bem-vindo a Loja do Marcos Paulo")

x = float(input('Entre com o valor do produto: '))
y = int(input('Entre com a quantidade do produto: '))

v = x * y #Calculo para a saber qual será o Valor da compra.

#Valores máximos dos descontos. Preferi colocar os valores aqui
# para não precisar mudar diretamente no código, caso a empresa X precise de mudar algo.
d1 = 2500 #d1 = M. Desconto 1
d2 = 6000 #d2 = M. Desconto 2
d3 = 10000 #d3 = M. Desconto 3

#Porcentagem dos Descontos
pd1 = 0 #Porcentagem Desconto 1
pd2 = 4 #Porcentagem Desconto 2
pd3 = 7 #Porcentagem Desconto 3
pd4 = 11 #Porcentagem Desconto 4

#Frase, coloquei aqui para caso a "empresa X" queria mudar a forma que se comunica com o cliente.
sem = 'O valor SEM desconto: R$'
com = 'O valor COM desconto: R$'



#Valor com Desconto
v1 = v * (1 - pd2 / 100) #Cálculo com o Desconto 2
v2 = v * (1 - pd3 / 100) #Cálculo com o Desconto 3
v3 = v * (1 - pd4 / 100) #Cálculo com o Desconto 4

#Calculos
if v < d1:
    print(f'{sem}{v:.2f}')
elif d1 <= v < d2:
    print(f'{sem}{v:.2f}')
    print(f'{com}{v1:.2f}')
elif d2 <= v < d3:
    print(f'{sem}{v:.2f}')
    print(f'{com}{v2:.2f}')
else:
    print(f'{sem}{v:.2f}')
    print(f'{com}{v3:.2f}')

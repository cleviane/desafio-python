import pandas as pd

#pip install pandas
dados = pd.read_csv('transportadoras.csv') #irá ler o arquivo csv

print('Opção mais barata 1: para Custo de Frete até 100Kg [R$/Kg]')
# irá exibir os dados da opção mais barata da transportadora, com seus respectivos campos
print(dados.loc[[4],
                ['Nome','Cidade','Custo de Frete até 100Kg [R$/Kg]','Tempo para Entrega','Custo de Frete até 100Kg [R$/Kg]']])
# valor total do valor mais barato até 100kg
valorTotal = 1.30 * 50
print(f"Valor total na compra de por Ex. 50kg: {valorTotal}\n")

# irá exibir os dados da segunda opção mais barata da transportadora, com seus respectivos campos
print(f'Opção mais barata 2: para Custo de Frete mais de 100Kg [R$/Kg]\n')
print(dados.loc[[4],
                ['Nome', 'Cidade', 'Custo de Frete mais de 100Kg [R$/Kg]','Tempo para Entrega', 'Custo de Frete mais de 100Kg [R$/Kg]']])
# valor total do valor mais barato mais de 100kg
valorTotal = 0.95 * 130
print(f"Valor total na compra de por Ex. 130kg: {valorTotal}\n")

print("__________________________________________________________")

print('Opção mais rápida 1: para Tempo para Entrega\n')
# irá exibir os dados da opção mais rápida da transportadora, com seus respectivos campos
print(dados.loc[[12], 
                ['Nome', 'Cidade', 'Custo de Frete até 100Kg [R$/Kg]','Tempo para Entrega', 'Custo de Frete mais de 100Kg [R$/Kg]']])
# valor total do valor mais rápido
valorTotal = 14.50 * 50
print(f"Valor total na compra de por Ex. 50kg: {valorTotal}\n")

print('Opção mais rápida 2: para Tempo para Entrega')
# irá exibir os dados da segunda opção mais rápida da transportadora, com seus respectivos campos
print(dados.loc[[13], 
                ['Nome', 'Cidade', 'Custo de Frete mais de 100Kg [R$/Kg]','Tempo para Entrega', 'Custo de Frete mais de 100Kg [R$/Kg]']])
# valor total do valor mais rápido
valorTotal = 15.72 * 130
print(f"Valor total na compra de por Ex. 130kg: {valorTotal}\n")

print("__________________________________________________________")

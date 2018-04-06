import pickle

meus_dados = ['Matheus', 3.14, [1, 2, 3]]

with open('arquivo.txt', 'wb') as file:
    pickle.dump(meus_dados, file)

with open('arquivo.txt', 'rb') as file:
    dados_carregados = pickle.load(file)

print(dados_carregados)

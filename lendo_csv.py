import pandas as pd

numeros = []
df = pd.read_csv("dados.csv", engine='python', sep=';', encoding='utf8')

# print(df.to_string())

print("-----------------------------------------------------------------")

for i in range(len(df)):  # Percorrendo o CSV df
    numeros.append(df.loc[i, 'Numero'])

print(numeros)

print("-----------------------------------------------------------------")

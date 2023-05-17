# Análise de Dados com Python

### Desafio:

#Você trabalha em uma empresa do varejo e tem milhares de clientes diferentes.

#Com o objetivo de aumentar o faturamento e o lucro da sua empresa, a diretoria quer conseguir identificar quem é o cliente ideal para seus produtos, baseado no histórico de compras dos clientes.

#Para isso, ela fez um trabalho de classificar os clientes com uma nota de 1 a 100. Só que agora, sobrou para você conseguir, a partir dessa nota, descobrir qual o perfil de cliente ideal da empresa.

#Qual a profissão? Qual a idade? Qual a faixa de renda? E todas as informações que você puder analisar para dizer qual o cliente ideal da empresa.

# Base de Dados: https://drive.google.com/drive/folders/1XvNLDKVH7TUS8HdH4r0TkXL__MFpoc3e?usp=share_link



#####

import pandas as pd 

baseDeDados = pd.read_csv("clientes.csv", encoding="latin", sep=";")

# Retirando Colunas sem importancia

baseDeDados = baseDeDados.drop("Unnamed: 8", axis = 1)

# Tratamento de Dados

# print(baseDeDados.info()) - Conferindo 

baseDeDados["Salário Anual (R$)"] = pd.to_numeric(baseDeDados["Salário Anual (R$)"], errors="coerce")

# print(baseDeDados.info()) - Conferindo 


# Retirando linhas vazias 

baseDeDados = baseDeDados.dropna()

# print(baseDeDados.info()) - Conferindo 
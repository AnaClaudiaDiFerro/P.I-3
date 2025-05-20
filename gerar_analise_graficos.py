import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random
import os

# Garante que a pasta 'data/' exista
os.makedirs("data", exist_ok=True)

nomes_femininos = ["Ana", "Beatriz", "Camila", "Daniela", "Eduarda", "Fernanda"]
nomes_masculinos = ["Carlos", "Eduardo", "Fernando", "Gabriel", "Henrique", "Igor"]
sobrenomes = ["Silva", "Santos", "Oliveira", "Pereira", "Almeida", "Costa"]
series = ["1º Ano", "2º Ano", "3º Ano"]

dados = []

for i in range(200):
    sexo = random.choice(["Feminino", "Masculino"])
    nome = random.choice(nomes_femininos if sexo == "Feminino" else nomes_masculinos)
    sobrenome = random.choice(sobrenomes)
    nome_completo = f"{nome} {sobrenome}"
    email = f"{nome.lower()}.{sobrenome.lower()}{i}@gmail.com"
    chapa = random.choices(["Escola Avante", "Mudança Já"], weights=[0.4, 0.6])[0]
    idade = random.randint(15, 25)
    serie = random.choice(series)

    dados.append({
        "nome_completo": nome_completo,
        "email": email,
        "sexo": sexo,
        "chapa_votada": chapa,
        "idade": idade,
        "serie": serie
    })

df = pd.DataFrame(dados)

caminho_csv = "data/votacao_simulada.csv"
df.to_csv(caminho_csv, index=False)

# Estatísticas simples

print("Distribuição por sexo:")
print(df['sexo'].value_counts(normalize=False))
print("\nDistribuição por chapa votada:")
print(df['chapa_votada'].value_counts(normalize=False))
print("\nDistribuição por série:")
print(df['serie'].value_counts(normalize=False))
print("\nEstatística descritiva da idade:")
print(df['idade'].describe())

# Gráficos

plt.figure(figsize=(6,4))
sns.countplot(data=df, x='sexo')
plt.title('Distribuição de Sexo')
plt.savefig('data/grafico_sexo.png')
plt.close()

plt.figure(figsize=(6,4))
sns.countplot(data=df, x='chapa_votada')
plt.title('Distribuição de Votos por Chapa')
plt.savefig('data/grafico_chapa.png')
plt.close()

plt.figure(figsize=(6,4))
sns.countplot(data=df, x='serie', order=series)
plt.title('Distribuição por Série Escolar')
plt.savefig('data/grafico_serie.png')
plt.close()

plt.figure(figsize=(6,4))
sns.histplot(df['idade'], bins=11, kde=True)
plt.title('Distribuição de Idade')
plt.savefig('data/grafico_idade.png')
plt.close()

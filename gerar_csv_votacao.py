import pandas as pd
import random
import os

print("Diretório atual:", os.getcwd())

# Garante que a pasta 'data/' exista
os.makedirs("data", exist_ok=True)

nomes_femininos = ["Ana", "Beatriz", "Camila", "Daniela", "Eduarda", "Fernanda"]
nomes_masculinos = ["Carlos", "Eduardo", "Fernando", "Gabriel", "Henrique", "Igor"]
sobrenomes = ["Silva", "Santos", "Oliveira", "Pereira", "Almeida", "Costa"]

dados = []

for i in range(200):
    sexo = random.choice(["Feminino", "Masculino"])
    nome = random.choice(nomes_femininos if sexo == "Feminino" else nomes_masculinos)
    sobrenome = random.choice(sobrenomes)
    nome_completo = f"{nome} {sobrenome}"
    email = f"{nome.lower()}.{sobrenome.lower()}{i}@gmail.com"
    chapa = random.choices(["Escola Avante", "Mudança Já"], weights=[0.4, 0.6])[0]

    dados.append({
        "nome_completo": nome_completo,
        "email": email,
        "sexo": sexo,
        "chapa_votada": chapa
    })

df = pd.DataFrame(dados)
os.makedirs("data", exist_ok=True)
caminho_csv = "data/votacao_simulada.csv"
df.to_csv(caminho_csv, index=False)


print(f"Arquivo salvo em: {os.path.abspath(caminho_csv)}")
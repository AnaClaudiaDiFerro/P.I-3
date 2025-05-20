import pandas as pd
import random

# Geração dos dados simulados
nomes_masculinos = ['Lucas', 'Pedro', 'João', 'Carlos', 'Mateus', 'Gabriel', 'Felipe', 'André', 'Rafael', 'Bruno']
nomes_femininos = ['Ana', 'Maria', 'Julia', 'Larissa', 'Beatriz', 'Camila', 'Fernanda', 'Patricia', 'Rafaela', 'Juliana']

sexos = ['Masculino', 'Feminino']
chapas = ['Escola Avante', 'Mudança Já']

dados = []

for i in range(1, 201):
    sexo = random.choice(sexos)
    if sexo == 'Masculino':
        nome = random.choice(nomes_masculinos)
    else:
        nome = random.choice(nomes_femininos)
    sobrenome = f"Aluno{i}"
    nome_completo = f"{nome} {sobrenome}"
    email = f"{nome.lower()}.{sobrenome.lower()}@gmail.com"
    chapa = random.choices(chapas, weights=[0.55, 0.45])[0]  # Leve vantagem para Escola Avante
    dados.append([nome_completo, email, sexo, chapa])

df = pd.DataFrame(dados, columns=["Nome", "Email", "Sexo", "Chapa Votada"])
caminho_csv = "/mnt/data/votacao_simulada.csv"
df.to_csv(caminho_csv, index=False)
caminho_csv

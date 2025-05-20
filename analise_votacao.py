import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Garante que a pasta 'data/' exista
os.makedirs("data", exist_ok=True)

# Lê os dados do CSV gerado
df = pd.read_csv("data/votacao_simulada.csv")

# 1) Gráfico: Votos por sexo
plt.figure(figsize=(6,4))
sns.countplot(data=df, x="sexo", palette="pastel")
plt.title("Número de Votos por Sexo")
plt.xlabel("Sexo")
plt.ylabel("Número de Votos")
plt.tight_layout()
plt.savefig("data/votos_por_sexo.png")
plt.close()

# 2) Gráfico: Proporção de votos por chapa (pizza)
plt.figure(figsize=(6,6))
df['chapa_votada'].value_counts().plot.pie(
    autopct='%1.1f%%', colors=sns.color_palette("pastel"), startangle=140)
plt.title("Proporção de Votos por Chapa")
plt.ylabel("")  # Remove label y
plt.tight_layout()
plt.savefig("data/proporcao_votos_chapa.png")
plt.close()

# 3) Gráfico: Votos por sexo divididos por chapa (barra agrupada)
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="sexo", hue="chapa_votada", palette="pastel")
plt.title("Votos por Sexo e Chapa")
plt.xlabel("Sexo")
plt.ylabel("Número de Votos")
plt.legend(title="Chapa")
plt.tight_layout()
plt.savefig("data/votos_por_sexo_e_chapa.png")
plt.close()

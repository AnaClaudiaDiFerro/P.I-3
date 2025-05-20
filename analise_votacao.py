import pandas as pd

caminho_csv = "data/votacao_simulada.csv"

df = pd.read_csv(caminho_csv)

total_votos = len(df)
votos_por_chapa = df['chapa_votada'].value_counts()
votos_por_sexo = df['sexo'].value_counts()
chapa_vencedora = votos_por_chapa.idxmax()
votos_vencedora = votos_por_chapa.max()

print(f"Total de votos: {total_votos}")
print("\nVotos por chapa:")
print(votos_por_chapa)
print("\nVotos por sexo:")
print(votos_por_sexo)
print(f"\nChapa vencedora: {chapa_vencedora} com {votos_vencedora} votos")

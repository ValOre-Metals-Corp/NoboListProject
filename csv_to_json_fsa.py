import pandas as pd
import os

# Caminho do CSV
file_path = os.path.join("data", "Nobo_List_Map.csv")

# 1. Carregar a base
df = pd.read_csv(file_path)

# 2. Selecionar colunas relevantes
cols = [
    "FSA", "PROVINCE", "lat", "lon",
    "NUMBER OF SHARES", "AVERAGE_INCOME"
]
df = df[cols].dropna(subset=["FSA", "lat", "lon"])

# 3. Agrupar por FSA + PROVÍNCIA (e contar investidores)
df_fsa = (
    df.groupby(["FSA", "PROVINCE"], as_index=False)
      .agg({
          "NUMBER OF SHARES": "sum",    # soma total de shares
          "AVERAGE_INCOME": "mean",    # média de renda
          "lat": "mean",               # média de latitude
          "lon": "mean",               # média de longitude
      })
)

# 4. Adicionar coluna com contagem de investidores
investor_count = (
    df.groupby(["FSA", "PROVINCE"])
      .size()
      .reset_index(name="investor_count")
)

# 5. Unir com o DataFrame agregado
df_fsa = pd.merge(df_fsa, investor_count, on=["FSA", "PROVINCE"], how="left")

# 6. Renomear colunas
df_fsa = df_fsa.rename(columns={
    "FSA": "fsa",
    "PROVINCE": "province",
    "NUMBER OF SHARES": "shares",
    "AVERAGE_INCOME": "income"
})

# 7. Exportar para JSON
output_path = os.path.join("investors_fsa.json")
df_fsa.to_json(output_path, orient="records", indent=2)

print("✅ Arquivo 'investors_fsa.json' criado com sucesso!")
print(f"Total de FSA agrupados: {len(df_fsa)}")

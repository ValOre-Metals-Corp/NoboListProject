import pandas as pd
import os

# Caminho corrigido
file_path = os.path.join("data", "Nobo_List_Map.csv")

# 1. Carregar a base
df = pd.read_csv(file_path)

# 2. Manter colunas importantes
df_small = df[[
    "INVESTOR (CONSOLIDATED)",
    "FSA",
    "CITY",
    "PROVINCE",
    "NUMBER OF SHARES",
    "lat",
    "lon",
    "INVESTOR TIER",
    "Investor Cluster",
    "AVERAGE_INCOME",
    "AVERAGE_AGE_ESTIMATED"
]].dropna(subset=["lat", "lon"])

# 3. Renomear colunas
df_small = df_small.rename(columns={
    "INVESTOR (CONSOLIDATED)": "name",
    "FSA": "fsa",
    "CITY": "city",
    "PROVINCE": "province",
    "NUMBER OF SHARES": "shares",
    "INVESTOR TIER": "tier",
    "Investor Cluster": "cluster",
    "AVERAGE_INCOME": "income",
    "AVERAGE_AGE_ESTIMATED": "age"
})

# 4. Exportar para JSON
output_path = os.path.join("investors.json")
df_small.to_json(output_path, orient="records", indent=2)

print("✅ Arquivo 'investors.json' criado com sucesso!")
print(f"Total de investidores com coordenadas: {len(df_small)}")

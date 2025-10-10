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

# 3.5. 🧹 Padronizar nomes dos clusters
df_small["cluster"] = df_small["cluster"].str.strip().replace({
    "Pending Contact Method (Consent Without Email)": "Pending Contact Method",
    "Pending contact method": "Pending Contact Method",
    "Pending": "Pending Contact Method",
    "Do not contact": "Do Not Contact",
    "Non-contactable": "Do Not Contact",
    "Non Contactable Investors": "Do Not Contact",
    "High potential contacts": "High-Potential Contacts",
    "Low potential contacts": "Low-Potential Contacts",
    "Potential contacts": "Potential Contacts",
    "Top priority contacts": "Top Priority Contacts"
})

# 4. Exportar para JSON
output_path = os.path.join("investors.json")
df_small.to_json(output_path, orient="records", indent=2)

print("✅ Arquivo 'investors.json' criado com sucesso!")
print(f"Total de investidores com coordenadas: {len(df_small)}")
print("\nCategorias de cluster encontradas:")
print(df_small['cluster'].value_counts())


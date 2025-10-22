import pandas as pd
import os

# Caminho da base principal
file_path = os.path.join("data", "Nobo_List_Map.csv")

# 1️⃣ Carregar a base
df = pd.read_csv(file_path)

# 2️⃣ Selecionar as colunas principais + novas categorias de distância e duração
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
    "AVERAGE_AGE_ESTIMATED",
    "NEAREST_CITY",
    "DIST_TO_CITY_HALL_KM",
    "TIME_TO_CITY_HALL_MIN",
    "DIST_TO_AIRPORT_KM",
    "TIME_TO_AIRPORT_MIN",
    "Airport_Distance_Category",
    "Airport_Duration_Category",
    "CityHall_Distance_Category",
    "CityHall_Duration_Category"
]].dropna(subset=["lat", "lon"])

# 3️⃣ Renomear colunas
df_small = df_small.rename(columns={
    "INVESTOR (CONSOLIDATED)": "name",
    "FSA": "fsa",
    "CITY": "city",
    "PROVINCE": "province",
    "NUMBER OF SHARES": "shares",
    "INVESTOR TIER": "tier",
    "Investor Cluster": "cluster",
    "AVERAGE_INCOME": "income",
    "AVERAGE_AGE_ESTIMATED": "age",
    "NEAREST_CITY": "nearest_city",
    "DIST_TO_CITY_HALL_KM": "dist_to_cityhall_km",
    "TIME_TO_CITY_HALL_MIN": "time_to_cityhall_min",
    "DIST_TO_AIRPORT_KM": "dist_to_airport_km",
    "TIME_TO_AIRPORT_MIN": "time_to_airport_min",
    "Airport_Distance_Category": "airport_distance_category",
    "Airport_Duration_Category": "airport_duration_category",
    "CityHall_Distance_Category": "cityhall_distance_category",
    "CityHall_Duration_Category": "cityhall_duration_category"
})

# 4️⃣ Padronizar nomes dos clusters
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

# 5️⃣ Exportar JSON atualizado
output_path = os.path.join("data", "investors.json")
df_small.to_json(output_path, orient="records", indent=2, force_ascii=False)

print("✅ Arquivo 'investors.json' criado com sucesso!")
print(f"Total de investidores com coordenadas: {len(df_small)}")
print("\nCategorias de cluster encontradas:")
print(df_small['cluster'].value_counts())
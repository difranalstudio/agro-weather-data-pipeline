import pandas as pd


def transformar_dados(data):
  df = pd.DataFrame({
    "data_hora": data["hourly"]["time"],
    "temperatura": data["hourly"]["temperature_2m"],
    "chuva": data["hourly"]["precipitation"],

  })

  df["data_hora"] = pd.to_datetime(df["data_hora"])

  print("\n=== QUALITY CHECK ===")
  print(f"Valores nulos:\n{df.isnull().sum()}\n")
  print(f"Linhas duplicadas: {df.duplicated().sum()}")
  print(f"Temperatura mínima: {df['temperatura'].min()}")
  print(f"Temperatura máxima: {df['temperatura'].max()}")
  print(f"Chuva mínima: {df['chuva'].min()}")
  print(f"Chuva máxima: {df['chuva'].max()}")

  return df




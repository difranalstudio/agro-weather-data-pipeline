import requests

def extrair_dados():
  url = "https://api.open-meteo.com/v1/forecast"

  params = {
            "latitude": -19.59, #Exemplo de Araxá MG
            "longitude": -46.94,
            "hourly": "temperature_2m,precipitation",
            "timezone": "America/Sao_Paulo"

  }


  response = requests.get(url, params=params)

  return response.json()

#print(data["hourly"].keys())

#print(data["hourly"]["time"][:5])
#print(data["hourly"]["temperature_2m"][:5])
#print(data["hourly"]["precipitation"][:5])
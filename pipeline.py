from extract import extrair_dados
from transform import transformar_dados
from load import carregar_dados


data = extrair_dados()

df = transformar_dados(data)

carregar_dados(df)

#print(df.head())
#print(df.info())
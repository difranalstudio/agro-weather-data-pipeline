import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def carregar_dados(df):
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO clima (
                data_hora,
                temperatura,
                chuva
            )
            VALUES (%s, %s, %s)

            ON CONFLICT (data_hora)

            DO UPDATE SET
                temperatura = EXCLUDED.temperatura,
                chuva = EXCLUDED.chuva
        """, (
            row["data_hora"],
            row["temperatura"],
            row["chuva"]
        ))

    conn.commit()

    cursor.close()
    conn.close()

    print(f"{len(df)} registros sincronizados com sucesso.")
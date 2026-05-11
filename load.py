import psycopg2


def carregar_dados(df):
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="weather_pipeline",
        user="postgres",
        password="postgres",
        port=5432
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

    print(f"{len(df)} registros inseridos com sucesso.")
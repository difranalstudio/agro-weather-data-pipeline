import pandas as pd

from src.transform import transformar_dados


def dados_fake():
    return {
        "hourly": {
            "time": [
                "2026-05-11T00:00",
                "2026-05-11T01:00"
            ],
            "temperature_2m": [
                17.0,
                16.7
            ],
            "precipitation": [
                0.0,
                0.2
            ]
        }
    }


def test_transformar_dados():

    data = dados_fake()

    df = transformar_dados(data)

    assert isinstance(df, pd.DataFrame)

    assert len(df.columns) == 3

    assert "data_hora" in df.columns
    assert "temperatura" in df.columns
    assert "chuva" in df.columns

    assert pd.api.types.is_datetime64_any_dtype(
        df["data_hora"]
    )

    assert df.isnull().sum().sum() == 0

    assert len(df) == 2
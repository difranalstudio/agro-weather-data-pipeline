# Weather Data Pipeline

Pipeline de engenharia de dados para coleta e processamento de dados climáticos com foco em aplicações no agronegócio.

## Stack

- Python
- pandas
- PostgreSQL
- Docker
- SQL

## Arquitetura

```text
API → Extract → Transform → Load → PostgreSQL
```

## Estrutura do projeto

```text
weather_data_pipeline/
├── src/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── pipeline.py
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md
```

## Como executar

### 1. Subir o banco

```bash
docker compose up -d
```

### 2. Ativar ambiente virtual

Windows:

```bash
venv\Scripts\activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar pipeline

```bash
python -m src.pipeline
```

## Features

- API ingestion
- Data validation
- Quality checks
- UPSERT strategy
- Environment variables
- Dockerized database

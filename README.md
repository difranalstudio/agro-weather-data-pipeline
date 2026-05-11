# Weather Data Pipeline

Pipeline de engenharia de dados para coleta e processamento de dados climáticos.

## Tecnologias

- Python
- pandas
- PostgreSQL
- Docker
- SQL

## Arquitetura

API → Extract → Transform → Load → PostgreSQL

## Features

- Coleta via API
- Quality checks
- Containerização
- UPSERT
- Prevenção de duplicidade

## Como executar

### Subir banco

```bash
docker compose up -d
```

### Ativar ambiente

```bash
venv\Scripts\activate
```

### Rodar pipeline

```bash
python pipeline.py
```

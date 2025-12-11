# Book Collection API

Простое API для управления коллекцией книг на FastAPI и SQLAlchemy.

## Установка

```bash
# Установка uv 
curl -LsSf https://astral.sh/uv/install.sh | sh

# Клонирование и запуск
git clone https://github.com/Nettallina/innowise_laboratory.git
cd book_api
uv add fastapi uvicorn sqlalchemy
uv run uvicorn main:app --reload --port 8080
# Simple HTTP Server

Простой HTTP сервер на стандартной библиотеке Python, возвращающий hostname.

## Запуск

```bash
# Локально
python app.py

# Docker
docker build -t simple-http .
docker run -p 8000:8000 simple-http
```

Проверка:
```bash
curl http://localhost:8000/
```

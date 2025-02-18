В этом небольшом проекте я попытался применить опыт работы с гексагональной архитектурой и фреймворк FastApi. 
Основная идея в том, чтобы разнести приложение на смысловые блоки, или они же "слои". В ходе работы над одним из проектов, довелось видеть чудеса гибкости подобного подхода, позволявшие быстро и недорого реагировать на самые неожиданные вызовы со стороны бизнеса и окружающих обстоятельств. 

Получилось не без небольших костылей, таких как файл api_project/aplication/app.py, нарушающий логику единой точки инициализации приложения. Однако остановился на этом варианте, так как на мой взгляд, другие подходы (например отсюда: https://github.com/fastapi/fastapi/discussions/8991) либо выглядят не лучше, либо нарушают исходный синтаксис фреймворка. 

Для тестового запуска необходимо:

1. Создать и заполнить файл с переменными окружения:

```
DATABASE_HOST=postgres
DATABASE_NAME=my_db
DATABASE_PASS=root
DATABASE_PORT=5432
DATABASE_USER=root
```

2. Запустить проект командой

```
docker-compose up -d --build
```

3. Работа с API

Документация будет доступна по "http://localhost:8004/docs"

Примеры запросов:

Запрос рассчёта стоимости страхования. Введя разные года (с 2000 по 2024) получите разную стоимость. 
- http://localhost:8004/rates/insurance_costs
```
{
  "name": "Glass",
  "date": "2024-12-05",
  "amount": 100
}
```

Запрос на заведение новых тарифных планов 

```
{
    "2021-01-01": [
        {
            "cargo_type": "Air",
            "rate": 0.012
        },
        {
            "cargo_type": "Box",
            "rate": 0.012
        }
    ],
    "2023-01-01": [
        {
            "cargo_type": "Air",
            "rate": 1.012
        },
        {
            "cargo_type": "Box",
            "rate": 1.012
        }
    ]
}
```

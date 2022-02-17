# Yamdb_final

## Описание 

Упаковка проекта **YaMDb**, который собирает **отзывы** (**Review**) пользователей на **произведения** (**Titles**), в контейнеры и настройка для приложения Continuous Integration и Continuous Deployment, а именно:
- автоматический запуск тестов,
- обновление образов на Docker Hub,
- автоматический деплой на боевой сервер при пуше в главную ветку main

## Технологии
-   Docker
-   Docker-compose
-   DockerHub
-   Workflow
-   Python
-   Django
-   Nginx
-   Gunicorn
-   PostgreSQL

## Запуск приложения
1. Если у вас уже установлены docker и docker-compose, этот шаг можно пропустить, иначе можно воспользоваться официальной [инструкцией](https://docs.docker.com/engine/install/).
2. Собрать контейнер и запустить
```
docker-compose up -d --build
```
3. Выполнить миграцию базы данных
```
docker-compose exec web python manage.py migrate --noinput
```
4. Собрать статические файлы
```
docker-compose exec web python manage.py collectstatic --no-input
```
5. Остановить контейнер
```
docker-compose down
```
## Создание суперпользователя
```
docker-compose run web python manage.py createsuperuser
```
## Заполнение базы начальными данными
```
docker-compose exec -ti container_name python manage.py loaddata fixtures.json
```
## Документация
Документация будет доступна после запуска проекта по адресу `/redoc/`.

## Workflow
![example workflow](https://github.com/ElizavetaAanisimova/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## Адрес проекта
http://130.193.52.48/admin/

## Автор
Елизавета Анисимова
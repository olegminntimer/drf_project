# drf_project

## Описание:

LMS-система, в которой каждый желающий может размещать свои полезные материалы или курсы.

## Возможности
- Регистрация пользователей
- Аутентификация пользователей
- Управление курсами
- Управление уроками
- Управление пользователями (автоматическая блокировка неактивных пользователей)
- Платежный сервис
- Подписка на курсы
- Документация API

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/olegminntimer/drf_project.git
```
2. Настройте переменные env в соответствии с .envexample

## Использование:

1. Запустите контейнер:
```commandline
docker-compose up --build --force-recreate -d
```
Использование отдельного сервиса для инициализации (рекомендуется)

yaml
version: '3.8'

services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    depends_on:
      - init

  init:
    build: .
    command: >
      sh -c "python manage.py migrate &&
      python manage.py createsuperuser --noinput --email admin@example.com --username admin"
    environment:
      - DJANGO_SUPERUSER_PASSWORD=adminpassword
    volumes:
      - .:/code
После первого запуска сервис init завершит работу, а основной сервис web продолжит работать.

2. Регистрация: http://localhost:8000/users/register/ и создайте учетную запись пользователя.
3. Вход: http://localhost:8000/users/login/ и создайте учетную запись пользователя.


## Документация:

После запуска контейнера откройте документацию API по адресу:

Swagger UI: http://localhost:8000/swagger/
или
Redoc UI: http://localhost:8000/redoc/

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).

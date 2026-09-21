# Практическая работа №3

Готовый каркас Django-проекта по заданию: PostgreSQL, Redis (Memurai), кастомный пользователь, справочники и Django Admin.

## 1. Создать и активировать виртуальное окружение (Windows PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Если PowerShell запрещает запуск скриптов, можно активировать через cmd:

```cmd
.venv\Scripts\activate
```

## 2. Установить зависимости

```powershell
pip install -r requirements.txt
```

## 3. Подготовить PostgreSQL

В `psql -U postgres`:

```sql
CREATE USER ams WITH PASSWORD 'ams';
CREATE DATABASE ams OWNER ams;
GRANT ALL ON SCHEMA public TO ams;
```

## 4. Подготовить переменные окружения

```powershell
copy .env.example .env
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Вставьте полученный ключ в `.env` вместо `dev-secret-change-me`.

## 5. Redis / Memurai

Установите Memurai Developer и оставьте порт `6379`.

## 6. Миграции

```powershell
python manage.py makemigrations
python manage.py migrate
```

## 7. Создать суперпользователя

```powershell
python manage.py createsuperuser
```

## 8. Запуск

```powershell
python manage.py runserver
```

Откройте:
- http://127.0.0.1:8000/admin/

## Что должно быть в админке

- Пользователи
- Локации
- Категории
- Производители
- Модели

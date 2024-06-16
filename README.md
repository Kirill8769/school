## Установка и запуск

### Склонируйте репозиторий:

```bash
git clone https://github.com/Kirill8769/school.git
```

### Перейдите в папку с проектом

```bash
cd school
```

### Установите зависимости:

Сначала активируем poetry
```bash
poetry shell
```

Затем установим все зависимости из pyproject.toml
```bash
poetry install
```

Для определения необходимых переменных окружения воспользуйтесь шаблоном
```bash
.env.sample
```

Сделайте миграции
```bash
python manage.py makemigrations
python manage.py migrate
```

Создайте суперпользователя
```bash
python manage.py csu
```

Загрузите фикстуры
```bash
python manage.py loaddata fixture/user_data.json
python manage.py loaddata fixture/lesson_data.json
python manage.py loaddata fixture/course_data.json
python manage.py loaddata fixture/payment_data.json
python manage.py loaddata fixture/group_data.json
```

## Запуск программы

### Сервер сайта
Для запуска сервера сайта выполните команду:
```bash
python manage.py runserver
```

## Лицензия

Проект распространяется под лицензией MIT.

---

Этот README файл предоставляет основную информацию о проекте, его установке и использовании.

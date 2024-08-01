<h1><span style="color:red">Ya</span>Cut</h1>

<h2>YaCut - это сервис для создания которких ссылок для удобного использования. ID короткой ссылки может содержать только цыфры и буквы латинского алфавита.</h2>

<h3>Чтобы запустить проект следуйте инструкции ниже.</h3>

Клонировать репозиторий и перейти в него в командной строке:

```
git clone 
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Запустить проект

```
flask run
```

<h3>Примеры запросов к API</h3>

Создание короткой ссылки

POST http://127.0.0.1:8000//api/id/

*Запрос

    ```
    {
    "url": "string",
    "custom_id": "string"
    }
    ```

*Ответ

```
    {
    "url": "string",
    "short_link": "string"
    }
```

Получение полной ссылки

GET http://127.0.0.1:8000//api/id/{short_id}/

```
{
  "url": "string",
  "short_link": "string"
}
```

Технологии использованные в прокете:

flask, sqlalchemy

### Автор vechanka

### tg: https://t.me/Vecha1337
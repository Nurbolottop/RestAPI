# Техническое задание на позицию Intern Backend Developer

## Mango Read

#### **Функциональность**

###### - Регистрация и аутентификация пользователей
###### - Фильтрация карточек по жанрам
###### - Пагинация карточек с отображением 12 карточек на странице
###### - Поиск карточек по названию
###### - Возможность оставить рецензию на карточку

#### **Требования к установке**
###### - Python 3.6 или выше
###### - Django 3.0 или выше
###### - Django REST Framework 3.0 или выше
###### - Другие зависимости указаны в файле requirements.txt

#### **Инструкции по установке и запуску**
###### - Клонируйте репозиторий на свой компьютер.
###### - Создайте виртуальное окружение.
###### - Активируйте виртуальное окружение.
###### - Установите необходимые зависимости: pip install -r requirements.txt.
###### - Проведите миграции: python manage.py migrate.
###### - Создайте администратора: python manage.py createsuperuser.
###### - Запустите сервер: python manage.py runserver.
###### - Откройте в браузере страницу http://localhost:8000/.

#### **Используемые технологии**

###### - Django
###### - Python
###### - PostgreSQL (или другая база данных)
###### - Django REST Framework

#### **1. Карты**


```api/card/```
**- Получить все карты**


```api/card/<int:pk>/```
**- Получить детальную информацию о карте**


```api/card/?genres=<str:genre>/```
**- Получить список карт по жанру**


```api/card/search/?search=<str:search_query>/```
**- Поиск  карт, соответствующих запросу**


#### **1.Пользователи**

```api/users/```
 **- Получить список всех пользователей**
api/users/register/ 
**- Регистрация нового пользователя**
```api/users/<int:pk>/ ```
**- Получить детальную информацию о пользователе с определенным идентификатором**
```api/users/<int:pk>/edit/ ```
**- Редактирование пользователя с определенным идентификатором**
```api/users/<int:pk>/delete/ ```
**- Удаление пользователя с определенным идентификатором**
```api/login/ ```
**- Аутентификация пользователя**
```api/refresh/ ```
**- Обновление access токена**
Рецензии
```api/reviews/``` - Получить список всех рецензий
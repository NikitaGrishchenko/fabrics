```
django-admin startproject fabrics - создание проекта
python manage.py startapp showroom - создание приложение "пользователи"

python -m venv .venv – создание виртуального окружения Windows
source .venv/Scripts/activate – активация виртуального окружения Windows
pip install -r requirements.txt – установка зависимостей из requirements.txt
python manage.py runserver - запуск сервера
python manage.py collectstatic - сгенерировать статику

python manage.py makemigrations - создать миграции
python manage.py migrate - применить миграции

pip freeze – вывести установленные модули в консоль
pip freeze > requirements.txt – сохранить установленные модули в файл

python manage.py createsuperuser

python manage.py runserver 0.0.0.0:8000

sudo nano /etc/nginx/sites-available/fabrics

sudo ln -s /etc/nginx/sites-available/fabrics /etc/nginx/sites-enabled

sudo systemctl restart nginx
sudo systemctl restart gunicorn



```

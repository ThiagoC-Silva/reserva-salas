pip install -r requirements.txt
python manage.py migrate
python manage.py populate_salas
python manage.py collectstatic --noinput
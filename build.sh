
pip install -r requirements.txt

python manage.py migrate

python manage.py populate_salas

if [ -n "$STATIC_ROOT" ]; then
    python manage.py collectstatic --noinput
else
    echo "STATIC_ROOT não está configurado. Pulando coleta de arquivos estáticos."
fi
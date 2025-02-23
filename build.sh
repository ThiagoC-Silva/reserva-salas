
pip install -r requirements.txt

python manage.py migrate

if [ -n "$STATIC_ROOT" ]; then
    python manage.py collectstatic --noinput
else
    echo "STATIC_ROOT não está configurado. Pulando coleta de arquivos estáticos."
fi
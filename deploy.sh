#!/bin/bash
echo "--- Iniciando script de despliegue ---"

echo "1. Ejecutando migraciones..."
python manage.py migrate --no-input
if [ $? -eq 0 ]; then
    echo "✔ Migraciones completadas con éxito."
else
    echo "✘ Error en las migraciones."
fi

echo "2. Creando superusuario administrador..."
python manage.py create_admin
if [ $? -eq 0 ]; then
    echo "✔ Comando create_admin ejecutado."
else
    echo "✘ Error en create_admin."
fi

echo "3. Iniciando servidor Gunicorn..."
gunicorn config.wsgi

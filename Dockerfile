from ubuntu:20.04

run apt-get update 

run apt-get install -y  \
        python3-dev \
        python3-pip

workdir /app

copy requirements.txt requirements.txt

run pip3 install -r requirements.txt

copy . .

run python3 manage.py collectstatic

cmd gunicorn --bind 0.0.0.0:8000 gis.wsgi



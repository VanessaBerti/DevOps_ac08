from ubuntu:latest
run apt-get update -y
run apt-get install -y python-pip python-dev build-essential 
copy./app
workdir/app
run pip intall --no-cache-dir -r app/requirements.txt 
expose 5000
cmd ["python", "app/faculdadeimpacta/calculadora/app_web_start.py"]

# Di1 – Lab 6.2.7 (Build a Sample Web App in a Docker Container)

## Doel van dit experiment
In dit lab maak ik een eenvoudige webapp met Flask.
Daarna zet ik de webapp in een Docker container.

Docker controleren:
```bash
docker --version
```

## Stap 1: Flask installeren
Installeer Flask:
```bash
pip3 install flask
```

## Stap 2: Webapp starten (zonder Docker)
Start de webapp:
```bash
python3 sample_app.py
```

Test in een tweede terminal:
```bash
curl http://0.0.0.0:8080
```

Stop de webapp met:
```bash
CTRL + C
```

## Stap 3: Website bestanden gebruiken
De webapp gebruikt een HTML template en een CSS bestand.
Deze staan in:
- `templates/index.html`
- `static/style.css`

## Stap 4: Bash script gebruiken om de container te bouwen en te starten
Geef uitvoerrechten aan het script:
```bash
chmod a+x sample-app.sh
```

script uitvoeren:
```bash
bash ./sample-app.sh
```

Het script doet deze stappen:
- maakt een tijdelijke map `tempdir`
- kopieert de bestanden naar `tempdir`
- maakt een Dockerfile in `tempdir`
- bouwt de Docker image
- start een Docker container op poort 8080

## Stap 5: Controleren of de container draait
alle containers bekijken:
```bash
docker ps -a
```

logs bekijken van de container:
```bash
docker logs samplerunning
```

webapp testen:
```bash
curl http://localhost:8080
```

## Stap 6: In de container kijken
in de container gaan:
```bash
docker exec -it samplerunning /bin/bash
```

Bekijk de bestanden:
```bash
ls /home/myapp/
```

Ga terug uit de container:
```bash
exit
```

## Stap 7: Container stoppen en verwijderen
Stop de container:
```bash
docker stop samplerunning
```

Verwijder de container:
```bash
docker rm samplerunning
```
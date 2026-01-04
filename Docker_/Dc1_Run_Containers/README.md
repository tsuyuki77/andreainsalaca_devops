# Dc1 – Run containers-experiment (meerdere containers)

## Beschrijving
In dit experiment toon ik dat ik meerdere Docker containers tegelijk kan starten op basis van één Docker image.
Ik gebruik hiervoor de officiële nginx-image.

De focus van dit experiment ligt op:
- `docker run`
- verschil tussen **image** en **container**
- poort mapping
- meerdere containers tegelijk laten draaien

---

## Stap 1: Docker controleren
```bash
docker --version
docker ps
```

---

## Stap 2: Image ophalen
Ik gebruik de image `nginx:latest`.

Deze image wordt automatisch gedownload van **Docker Hub**
wanneer ik `docker run` uitvoer.


image controleren:
```bash
docker images
```

---

## Stap 3: Meerdere containers starten van dezelfde image
```bash
docker run -d --name web1 -p 8081:80 nginx:latest
docker run -d --name web2 -p 8082:80 nginx:latest
docker run -d --name web3 -p 8083:80 nginx:latest
```

---

## Stap 4: Controleren
```bash
docker ps
```

---

## Stap 5: Testen
Browser:
- http://localhost:8081
- http://localhost:8082
- http://localhost:8083

---

## Stap 6: Logs bekijken
```bash
docker logs web1
```

---

## Stap 7: Containers stoppen en verwijderen
```bash
docker stop web1 web2 web3
docker rm web1 web2 web3
```
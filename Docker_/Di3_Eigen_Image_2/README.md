# Di2 – Eigen image-experiment 2

## Beschrijving
In dit experiment heb ik een tweede eigen Docker image gemaakt.

Ik gebruik bewust een **eenvoudige Flask applicatie**
en dezelfde Dockerfile-structuur als in Di2.

---

## Stap 1: Docker image bouwen
Ik ga naar de map waar het Dockerfile staat en bouw de image:

```bash
docker build -t imageweb_app_v2 .
```

---

## Stap 2: Container starten
Start een container op basis van de image.
De applicatie draait op poort 5555.

```bash
docker run -d -p 5555:5555 --name imageweb_container_v2 imageweb_app_v2
```

---

## Stap 3: Testen
Ik test het deze keer via curl aangezien ik geen website heb toegevoegd:

```bash
curl http://localhost:5555
```

---

## Stap 4: Controleren
Controleer of de container draait:

```bash
docker ps
```

---

## Stap 5: Stoppen en remove
Stop de container:

```bash
docker stop imageweb_container_v2
```

Verwijder de container:

```bash
docker rm imageweb_container_v2
```

---

## Resultaat
- De Docker image wordt correct gebouwd
- De container draait correct
- De Flask applicatie is bereikbaar op poort 5555
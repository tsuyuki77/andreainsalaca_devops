# Dm1 – Docker management-experiment

## Beschrijving
In dit experiment toon ik dat ik Docker containers en images kan beheren.
De focus ligt niet op nieuwe containers maken, controleren, bekijken en opruimen van Docker.

---

## Stap 1: Overzicht van containers
Eerst bekijk ik welke containers draaien:

```bash
docker ps
```

Daarna bekijk ik **alle containers**, ook degene die gestopt zijn:

```bash
docker ps -a
```

---

## Stap 2: Container details bekijken (inspect)
Ik bekijk de details van een container, bijvoorbeeld web1:

```bash
docker inspect web1
```

Hier zie ik onder andere:
- welke image gebruikt wordt
- het IP-adres
- de poorten
- netwerk-informatie

---

## Stap 3: Logs bekijken
Ik bekijk de logs van een container:

```bash
docker logs web1
```

Zo kan ik zien wat de container doet
en of er fouten zijn.

---

## Stap 4: Resources monitoren
Ik controleer het gebruik van CPU en geheugen
van alle draaiende containers:

```bash
docker stats
```

Ik stop deze met:
```bash
Ctrl + c
```

---

## Stap 5: Images bekijken
Ik bekijk welke Docker images aanwezig zijn op het systeem:

```bash
docker images
```

---

## Stap 6: Container stoppen en verwijderen
Ik stop een container:

```bash
docker stop web1
```

Daarna kan ik de container verwijderen (niet gedaan):

```bash
docker rm web1
```

---

## Stap 7: Image verwijderen
Als er geen containers meer draaien van een image,
kan ik de image verwijderen:

```bash
docker rmi nginx:latest
```

---

## Stap 8: Docker opruimen (cleanup)
Ik kan ongebruikte Docker objecten verwijderen met:

```bash
docker system prune
```

En dan bevestigen met `y`.

---

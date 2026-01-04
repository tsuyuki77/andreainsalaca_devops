# Di2 – Eigen image-experiment (Docker)

## Beschrijving
In dit experiment heb ik een **eigen Docker image** gemaakt.
Ik heb een eenvoudige Flask webapp verpakt in een Docker image
en deze laten draaien in een container.

---

## Stap 1: Docker image bouwen
Ik ga naar de map waar het Dockerfile staat en build mijn image:

```bash
docker build -t imageweb_app:latest .
```

---

## Stap 2: Container starten
Daarna start ik een container op basis van mijn image.

Omdat poort **5050** al in gebruik was op mijn VM,
heb ik een andere host-poort gebruikt (**5051**):

```bash
docker run -d -p 5051:5050 --name imageweb_container imageweb_app:latest
```

---

## Stap 3: Testen
Ik test de webapp via de browser:

```
http://localhost:5051
```

---

## Stap 4: Controleren
Met dit commando controleer ik of de container draait:

```bash
docker ps
```

---

## Probleem en oplossing
Tijdens het experiment kreeg ik een foutmelding
dat poort **5050** al in gebruik was.

Oplossing:
- Ik heb een andere host-poort gebruikt (`5051:5050`)

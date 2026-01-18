# Di3 – Eigen image-experiment 2 (SQL met SQLite)

## Doel
In dit experiment maak ik een Docker image met een Flask applicatie.
De applicatie gebruikt een SQL database met SQLite (`sqlite3`).

---

## Stap 1: Image bouwen
Ga naar deze folder en build de image:

```bash
docker build -t di3-sqlite .
```

---

## Stap 2: Container starten
Start de container en map poort 5555:

```bash
docker run -d --name di3-sqlite-container -p 5555:5555 di3-sqlite
```

## Extra stap: Status controleren
### 2.1) Controleren of de container draait
```bash
docker ps
```

### 2.2) Logs bekijken
```bash
docker logs di3-sqlite-container
```

### 2.3) Poort mapping controleren
```bash
docker port di3-sqlite-container
```

---

## Stap 3: Testen

### 3.1) Health check
```bash
curl http://localhost:5555/health
```

### 3.2) Data toevoegen (SQL INSERT)
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"title":"Test","body":"Hallo"}' \
  http://localhost:5555/posts
```

### 3.3) Data opvragen (SQL SELECT)
```bash
curl http://localhost:5555/posts
```

---

## Stap 4: Container stoppen en verwijderen
```bash
docker stop di3-sqlite-container
docker rm di3-sqlite-container
```

---

## Stap 5: Image verwijderen
```bash
docker rmi di3-sqlite
```
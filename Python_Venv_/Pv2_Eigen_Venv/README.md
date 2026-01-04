# Pv2 – Eigen Python Virtual Environment experiment

## Beschrijving
In dit experiment installeer ik een Python library, namelijk request
en gebruik ik deze in een Python script.

---

## Stap 1: Python virtual environment aanmaken
Ik heb eerst een nieuwe Python virtual environment aangemaakt.

```bash
python3 -m venv python_env
```

---

## Stap 2: Virtual environment activeren
Daarna heb ik de virtual environment geactiveerd.

```bash
source venv/bin/activate
```

---

## Stap 3: Python library installeren
In deze virtual environment heb ik de requests library geïnstalleerd.
Deze library wordt vaak gebruikt voor API-calls.

```bash
pip install requests
```

---

## Stap 4: Python script uitvoeren
Ik heb een Python script uitgevoerd dat een eenvoudige HTTP GET-request doet
naar een publieke test-API die ik gebruikte in mijn vorig opdracht.

```bash
python test_requests.py
```

---

## Stap 5: Virtual environment afsluiten
Na het uitvoeren van het script heb ik de virtual environment afgesloten.

```bash
deactivate
```
# Ap4 – Eigen API-experiment 2 (Python) – DummyJSON

## Beschrijving
In dit experiment heb ik een tweede eigen API-experiment uitgevoerd met Python.
Ik gebruik een andere online REST API dan bij Ap3, namelijk de DummyJSON API.
Met deze API heb ik posts beheerd via verschillende HTTP-methodes (CRUD).

---

## Gebruikte API
Naam: DummyJSON test API  
URL:
```
https://dummyjson.com/posts
```

Deze API is publiek en vereist geen API-key.

---

## Installatie
- Python 3
- Python library `requests` => pip3 install requests

---

## Stap 1: READ – Posts opvragen
Bestand: `get_posts.py`

Dit script haalt alle posts op via een GET-request.

```bash
python3 get_posts.py
```

---

## Stap 2: CREATE – Post toevoegen
Bestand: `add_post.py`

Dit script vraagt een titel en body via de terminal
en stuurt deze data naar de API met een POST-request.

```bash
python3 add_post.py
```

---

## Stap 3: UPDATE – Post aanpassen
Bestand: `update_post.py`

Dit script vraagt:
- het post ID
- een nieuwe titel
- een nieuwe body

Daarna wordt de post aangepast met een PUT-request.

```bash
python3 update_post.py
```

---

## Stap 4: DELETE – Post verwijderen
Bestand: `delete_post.py`

Dit script vraagt het post ID
en verwijdert de post via een DELETE-request.

```bash
python3 delete_post.py
```

# Ap4 – Eigen API-experiment 2 (Python) – Postman Echo (Webforms)

## Beschrijving
In dit experiment heb ik een tweede eigen API-experiment uitgevoerd met Python.
Ik gebruik een andere online REST API dan bij Ap3, namelijk de Postman Echo API.

Ik toon ook het verschil tussen JSON en webforms.
In dit experiment verstuur ik de data als webforms met `data=` in Python requests.

Met deze API test ik verschillende HTTP-methodes (GET, POST, PUT, DELETE).

---

## Gebruikte API
Naam: POSTMAN echo API  
URL:
```
https://postman-echo.com/
```

Deze API is publiek en vereist geen API-key.

---

## Installatie
- Python 3
- Python library `requests` => pip3 install requests

---

## Stap 1: READ – Posts opvragen
Bestand: `get_post.py`

Dit script doet een GET request naar `/get` met parameters.

```bash
python3 get_post.py
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

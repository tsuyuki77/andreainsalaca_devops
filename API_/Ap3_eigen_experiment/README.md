
## Beschrijving
In dit experiment heb ik een eigen API-experiment uitgevoerd met Python.
Ik gebruik een online REST API (JSONPlaceholder) om CRUD-operaties uit te voeren.


De API werkt online en heeft geen API-key nodig.
Alle scripts zijn interactief en vragen input via de terminal.

---

## Gebruikte API
URL van de API:

```
https://jsonplaceholder.typicode.com/posts
```

---

## Installatie
- Python 3
- Python library `requests` => pip3 install requests

---

## Bestanden
In dit experiment gebruik ik deze bestanden:

- get_posts.py
- add_post.py
- update_post.py
- delete_post.py

Elk bestand voert één CRUD-actie uit.

---

## Stap 1: READ – Posts opvragen
Bestand: `get_posts.py`

Dit script vraagt alle posts op van de API.

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
- het id van de post
- een nieuwe titel
- een nieuwe body

Daarna wordt de post aangepast met een PUT-request.

```bash
python3 update_post.py
```

---

## Stap 4: DELETE – Post verwijderen
Bestand: `delete_post.py`

Dit script vraagt het id van de post
en verwijdert deze via een DELETE-request.

```bash
python3 delete_post.py
```
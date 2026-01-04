# W1 – Webex Python script (Lab 8.6.7)

## Beschrijving
In dit experiment heb ik gewerkt met de **Webex REST API**.
Ik heb Python scripts gebruikt om Webex Teams te beheren,
zoals gezien in **Lab 8.6.7** van NetAcad.

---

## Bestanden
In deze map staan meerdere Python scripts.

---

## Token en room ID
Voor de authenticatie gebruik ik een apart bestand:
`token_auth.py`.

Dit maakt het gemakkelijk om het token te wijzigen en een andere room te testen zonder de andere scripts aan te passen. De andere scripts importeren deze waarden.

Voorbeeld van `token_auth.py`:

```python
token = "ZjM4OGQzNDIt..."
room = "Y2lzY29zcGFya..."
```
---

## Stap 1: Personen opvragen
Met dit script vraag ik alle personen op:

```bash
python3 list-people.py
```

---

## Stap 2: Rooms opvragen
Met dit script vraag ik alle rooms op:

```bash
python3 list-rooms.py
```

---

## Stap 3: Room details bekijken
Met dit script vraag ik details op van één room:

```bash
python3 get-room-details.py
```

---

## Stap 4: Memberships bekijken
Met dit script bekijk ik wie lid is van een room:

```bash
python3 list-memberships.py
```

---

## Stap 5: Lid toevoegen aan een room
Met dit script voeg ik een persoon toe aan een room:

```bash
python3 create-membership.py
```

---

## Stap 6: Bericht sturen (markdown)
Met dit script stuur ik een markdown-bericht naar een room:

```bash
python3 creat-markdown-message.py
```
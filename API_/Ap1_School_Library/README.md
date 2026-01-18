# Ap1 – School Library API experiment

## Beschrijving
In dit experiment heb ik gewerkt met de School Library REST API in de DEVASC VM.
Met Python scripts heb ik verschillende HTTP-methodes getest:
GET, POST, PUT en DELETE.
De API gebruikt token-based authenticatie.

---

## API-gegevens
In het bestand auth.py worden deze gegevens gebruikt:

```python
APIHOST = "http://library.demo.local"
LOGIN = "cisco"
PASSWORD = "Cisco123!"
```

---

## Stap 1: Python virtual environment aanmaken
Ik heb eerst een virtual environment aangemaakt.
Dit zorgt ervoor dat de Python libraries lokaal worden gebruikt
en het systeem niet wordt beïnvloed.

```bash
python3 -m venv devfun
source devfun/bin/activate
pip3 install requests
```

---

## Stap 2: Token ophalen via de API
In auth.py wordt een POST-request gestuurd naar de login endpoint
om een token op te halen.
Dit token wordt gebruikt in de headers van alle volgende API-calls.

---

## Stap 3: Alle boeken opvragen (GET)
Met dit commando vraag ik alle boeken op uit de School Library API.

```bash
python3 get_books.py
```

---

## Stap 4: Nieuw boek toevoegen (POST)
Met dit script voeg ik een nieuw boek toe aan de library.

```bash
python3 add_book.py
```

---

## Stap 5: Boek aanpassen (PUT)
Om een bestaand boek aan te passen,
pas ik eerst het book_id aan in het bestand update_book.py
en voer daarna dit commando uit:

```bash
python3 update_book.py
```

---

## Stap 6: Boek verwijderen (DELETE)
Om een boek te verwijderen,
pas ik het book_id aan in delete_book.py
en voer daarna dit commando uit:

```bash
python3 delete_book.py
```
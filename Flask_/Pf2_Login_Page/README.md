# Pf2 – Logon-page experiment (lab 6.5.10)

## Beschrijving
In dit experiment heb ik het login-page experiment uitgevoerd,
gebaseerd op lab 6.5.10.
Ik heb gewerkt met een bestaande Flask loginapp map.

---

## Stap 1: Virtual environment aanmaken
In de map heb ik een Python virtual environment aangemaakt.

```bash
python3 -m venv login_env
```

Daarna heb ik de virtual environment geactiveerd:

```bash
source login_env/bin/activate
```

---

## Stap 2: Flask installeren
Wanneer de virtual environment actief was,
heb ik Flask geïnstalleerd.

```bash
pip install flask
```

---

## Stap 3: Flask applicaties
Ik werkte met twee Flask bestanden:

- `flask_app.py`  
  Deze toont de webpagina’s (account en login) op poort **8802**.

- `flask_app_login.py`  
  Deze verwerkt het aanmelden en inloggen op poort **5555**.

---

## Stap 4: Formulier-velden aanpassen
De namen van de velden in het formulier moesten aangepast worden.
Ik gebruikte eerst `USERNAME` en `PASSWORD`,
maar Flask verwacht:

- `username`
- `password`

Na deze wijziging werden de gegevens correct doorgestuurd.

---

## Stap 5: Flask servers starten
Om alles te testen heb ik eerst de loginserver gestart:

```bash
python3 flask_app_login.py
```

Daarna heb ik de webserver voor de HTML-pagina’s gestart:

```bash
python3 flask_app.py
```

Opmerking: In het begin werkte dit niet,
omdat de server in de verkeerde virtual environment werd gestart.

---

## Stap 6: Testen in de browser
In de browser heb ik eerst een account aangemaakt via:

```
http://127.0.0.1:8802/account
```

Daarna heb ik het inloggen getest via:

```
http://127.0.0.1:8802/login
```

---

## Resultaat
- Account aanmaken werkt correct.
- Inloggen werkt correct.
- Beide Flask servers communiceren met elkaar.

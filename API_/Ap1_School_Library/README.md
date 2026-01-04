# Pv1 – Python Virtual Environment (Lab-experiment)

## Beschrijving
In dit experiment heb ik het lab uit de PowerPoint gevolgd over Python Virtual Environments (venv).

---

## Stap 1: Python virtual environment aanmaken
Ik heb eerst een Python virtual environment aangemaakt.
Dit zorgt ervoor dat Python packages geïsoleerd worden
en het systeem niet wordt beïnvloed.

```bash
python3 -m venv venv
```

---

## Stap 2: Virtual environment activeren
Na het aanmaken heb ik de virtual environment geactiveerd.
Wanneer de environment actief is, verschijnt `(venv)` in de terminal.

```bash
source venv/bin/activate
```

---

## Stap 3: Controleren van de Python omgeving
Ik heb gecontroleerd dat Python vanuit de virtual environment wordt gebruikt.

```bash
python --version
```

---

## Stap 4: Virtual environment afsluiten
Na het testen heb ik de virtual environment afgesloten.

```bash
deactivate
```
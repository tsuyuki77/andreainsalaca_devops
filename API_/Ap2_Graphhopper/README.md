# Ap2 – Graphhopper API experiment (Lab 4.9.2)

## Beschrijving
In dit experiment heb ik gewerkt met de Graphhopper REST API.
Ik heb met Python locaties omgezet naar GPS-coördinaten
en routes opgevraagd tussen twee plaatsen.

De API gebruikt een API-key voor authenticatie.

---

## API-gegevens
In elk Python-bestand wordt deze API-key gebruikt:

```python
key = "a3c0ad04-6d1f-4de5-889d-97e8b1b15be1"
```
---

## Stap 1

De Python library `requests` is nodig om HTTP-requests te sturen.

```bash
pip3 install requests
```

---

## Stap 2: Eerste versie – JSON ophalen
Bestand: `graphhopper_parse-json_1.py`

In deze stap bouw ik een geocoding URL
en haal ik JSON-data op van de Graphhopper API.

```bash
python3 graphhopper_parse-json_1.py
```

---

## Stap 3: Tweede versie – geocoding functie
Bestand: `graphhopper_parse-json_2.py`

In deze versie gebruik ik een functie `geocoding()`
die latitude en longitude ophaalt voor twee vaste locaties.

```bash
python3 graphhopper_parse-json_2.py
```

---

## Stap 4: Derde versie – invoer van gebruiker
Bestand: `graphhopper_parse-json_3.py`

De gebruiker kan nu zelf een start- en eindlocatie ingeven.
Het programma blijft lopen tot `q` of `quit` wordt ingegeven.

```bash
python3 graphhopper_parse-json_3.py
```

---

## Stap 5: Vierde versie – foutafhandeling
Bestand: `graphhopper_parse-json_4.py`

In deze versie controleert het script
of de API een geldig resultaat teruggeeft
en toont het een foutmelding indien nodig.

```bash
python3 graphhopper_parse-json_4.py
```

---

## Stap 6: Vijfde versie – route opvragen
Bestand: `graphhopper_parse-json_5.py`

Hier wordt de Routing API gebruikt
om een route te berekenen tussen twee locaties.

```bash
python3 graphhopper_parse-json_5.py
```

---

## Stap 7: Zesde versie – afstand en tijd
Bestand: `graphhopper_parse-json_6.py`

In deze versie toont het script:
- totale afstand
- totale reistijd
- stap-voor-stap instructies

```bash
python3 graphhopper_parse-json_6.py
```

---

## Stap 8: Zevende versie – vervoermiddel kiezen
Bestand: `graphhopper_parse-json_7.py`

De gebruiker kan kiezen tussen car, bike of foot.
De route wordt berekend op basis van het gekozen vervoermiddel.

```bash
python3 graphhopper_parse-json_7.py
```
# U1 – Python Unittest experiment (Lab 3.5.7)

## Beschrijving
In dit experiment heb ik gewerkt met Python unittest om een functie te testen die door een JSON-object zoekt.

Het doel is om te controleren of de functie een bestaande key kan vinden, geen resultaat geeft bij een niet-bestaande key, en altijd een list teruggeeft

---

## Bestanden in dit experiment
Dit experiment bestaat uit drie Python-bestanden:

- `test_data.py`  
  Bevat een groot JSON-object (voorbeelddata van Cisco DNA Center).

- `recursive_json_search.py`  
  Bevat de functie `json_search()` die door het JSON-object zoekt.

- `test_json_search.py`  
  Bevat de unittests die de functie automatisch testen.

---

## Stap 1: Eerste versie van recursive_json_search.py
In de eerste versie stond `ret_val = []` in de functie.
Daardoor werd de lijst telkens opnieuw leeggemaakt bij elke recursieve oproep.

Gevolg ervan is dat de functie wel data vond, maar de lijst werd telkens overschreven, de unittest **test_search_found** faalde

Resultaat bij unittest:
```
.F.
FAILED (failures=1)
```

---

## Stap 2: Tweede versie (tijdelijke fix met globale variabele)
Ik heb `ret_val = []` buiten de functie geplaatst.
Dit zorgde ervoor dat resultaten niet meer overschreven werden.

Probleem:
- `ret_val` werd een **globale variabele**
- Resultaten bleven bestaan tussen meerdere functie-oproepen
- Hierdoor faalde **test_search_not_found**

Dit toont aan waarom globale variabelen geen goede idee zijn.

---

## Stap 3: Definitieve versie met inner_function
De correcte oplossing is het gebruik van een **inner function**.
Zo blijft `ret_val` lokaal en wordt deze correct opgebouwd. 
Ik heb het in een aparte bestand gemaakt zodat ik het verschil zag tussen de twee.

Structuur:
- `json_search()` maakt een lege lijst
- `inner_function()` doet de recursieve zoeklogica
- Na afloop wordt de lijst teruggegeven

Alle unittests slagen nu

---

## Stap 4: Unittest uitvoeren
De unittests heb ik uitgevoerd met:

```bash
python3 test_json_search.py
```

En ook met test discovery:

```bash
python3 -m unittest
```

Unittest voert automatisch alle bestanden uit die beginnen met `test_`.


## Betekenis van unittest opties

| Optie | Betekenis | Waarom gebruiken |
|------|----------|------------------|
| `-m` | Module uitvoeren | Laat Python de unittest-module uitvoeren en automatisch alle testbestanden zoeken |
| `-v` | Verbose | Toont extra informatie over welke tests worden uitgevoerd en of ze slagen |

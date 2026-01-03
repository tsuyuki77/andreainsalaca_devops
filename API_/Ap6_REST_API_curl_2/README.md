# Ap5 – Eigen REST-API experiment met curl

## Beschrijving
In dit experiment heb ik een eigen REST-API experiment uitgevoerd met `curl`.
Ik heb verschillende HTTP-methodes getest op een online REST API.

---

## Gebruikte API
DummyJSON test API  
Base URL:
```
https://dummyjson.com/posts
```

Dit API is publiek beschikbaar en vereist geen API-key.

---

Alle scripts zijn uitvoerbaar gemaakt met:

```bash
chmod +x *.sh
```

---

## Stap 1: GET – Posts opvragen
Bestand: `get_posts.sh`

```bash
./get_posts.sh
```

---

## Stap 2: POST – Post toevoegen
Bestand: `add_post.sh`

```bash
./add_post.sh
```

---

## Stap 3: PUT – Post aanpassen
Bestand: `update_post.sh`

```bash
./update_post.sh
```

---

## Stap 4: DELETE – Post verwijderen
Bestand: `delete_post.sh`

```bash
./delete_post.sh
```
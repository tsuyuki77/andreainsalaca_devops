# Ap5 – Eigen REST-API experiment met curl (gebaseerd op Ap3)

## Beschrijving
In dit experiment heb ik een REST-API experiment uitgevoerd met `curl`.
Dit experiment is gebaseerd op Ap3 (CRUD met JSONPlaceholder), 
maar nu voer ik alle acties uit met `curl` en shell scripts zonder Python te gebruiken.

---

## Gebruikte API
Naam: JSONPlaceholder test API  
Base URL:
```
https://jsonplaceholder.typicode.com/posts
```

Deze API is publiek beschikbaar en vereist geen API-key.

---

Alle scripts zijn uitvoerbaar gemaakt met:

```bash
chmod +x *.sh
```

---

## Stap 1: GET – Alle posts opvragen
Bestand: `get_posts.sh`

```bash
./get_posts.sh
```

---

## Stap 2: GET – Eén post opvragen (met id)
Bestand: `get_post_id.sh`

Dit script vraagt een post id via de terminal.

```bash
./get_post_id.sh
```

---

## Stap 3: POST – Post toevoegen
Bestand: `add_post.sh`

Dit script vraagt een titel en body via de terminal
en stuurt deze data naar de API met een POST-request.

```bash
./add_post.sh
```

---

## Stap 4: PUT – Post aanpassen
Bestand: `update_post.sh`

Dit script vraagt:
- het post id
- een nieuwe titel
- een nieuwe body

Daarna wordt de post aangepast met een PUT-request.

```bash
./update_post.sh
```

---

## Stap 5: DELETE – Post verwijderen
Bestand: `delete_post.sh`

Dit script vraagt een post id
en verwijdert deze via een DELETE-request.

```bash
./delete_post.sh
```
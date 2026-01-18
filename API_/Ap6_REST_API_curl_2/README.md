# Ap6 – Eigen REST-API experiment met curl 2 (forms)

## Beschrijving
In dit experiment toon ik een tweede REST-API experiment met `curl`.
Hier gebruik ik **forms** (form data) in plaats van JSON.

Ik verstuur data met:
- `Content-Type: application/x-www-form-urlencoded`
- `-d "key=value"` in curl

## Gebruikte API
Naam: Postman Echo API  
Basis URL:
```
https://postman-echo.com
```

Deze API is publiek en vereist geen API-key.
De API stuurt de ontvangen data terug in de response. Zo kan ik bewijzen dat ik forms verstuur.

## Bestanden
- `get_posts.sh` : GET request met parameters
- `add_post.sh` : POST request met forms
- `update_post.sh` : PUT request met forms
- `delete_post.sh` : DELETE request met forms

Maak de scripts uitvoerbaar:
```bash
chmod +x *.sh
```

## Stap 1: GET – request testen
```bash
./get_posts.sh
```
In de JSON response zie je de parameters in `args`.

## Stap 2: POST – forms versturen
```bash
./add_post.sh
```

In de JSON response zie je de form data in `form`. (Dit geldt ook voor put en delete)

## Stap 3: PUT – forms versturen
```bash
./update_post.sh
```

## Stap 4: DELETE – request testen
```bash
./delete_post.sh
```

Eigen verduidelijking
=> 

args = data in de URL (?a=b)

form = data in de body als webforms (-d a=b)
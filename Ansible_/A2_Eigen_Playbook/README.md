# A2 – Eigen Ansible playbook-experiment

## Beschrijving
In dit experiment heb ik een eigen Ansible playbook gemaakt.
Dit playbook installeert Apache op een webserver
en plaatst automatisch een eigen webpagina met een afbeelding.

---

## Structuur
Het bestand `hosts` is de inventory.
Hierin staat de webserver waarop het playbook wordt uitgevoerd.
De server zit in de groep `webservers`.

Voorbeeld:
```ini
[webservers]
192.0.2.3 ansible_user=devasc ansible_password=Cisco123!
```
---

## Playbook: install_apache_website.yaml
Dit playbook voert de volgende stappen uit:

1. Apache installeren met `apt`
2. Apache modules activeren
3. `index.html` kopiëren naar `/var/www/html/index.html`
4. Afbeelding kopiëren naar `/var/www/html/streetview.png`
5. Apache herstarten met een handler

Dit toont hoe Ansible wordt gebruikt voor
serverconfiguratie en deployment.

---

## Bestanden kopiëren
De bestanden staan lokaal in de map `files/`.

- `files/index.html` wordt gekopieerd naar `/var/www/html/index.html`
- `files/images/streetview.png` wordt gekopieerd naar `/var/www/html/streetview.png`

In `index.html` wordt de afbeelding geladen met:
```html
<img src="streetview.png">
```

Omdat `index.html` en `streetview.png` in "dezelfde" map staan,
kan de browser de afbeelding correct tonen.

---

## Playbook uitvoeren
Het playbook wordt uitgevoerd met:

```bash
ansible-playbook install_apache_website.yaml
```

---

## Testen
Na het uitvoeren van het playbook:

1. Controleer of Apache draait (op de webserver):
```bash
sudo systemctl status apache2
```

2. Controleer of de bestanden aanwezig zijn:
```bash
ls -l /var/www/html
```

3. Test in de browser:
```
http://192.0.2.3
```

De webpagina en afbeelding moeten zichtbaar zijn.
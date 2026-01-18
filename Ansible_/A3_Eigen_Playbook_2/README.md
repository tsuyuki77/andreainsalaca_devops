# A3 – Eigen Ansible playbook-experiment 2

## Beschrijving
In dit experiment heb ik een tweede eigen Ansible playbook gemaakt.
Dit playbook installeert `Nginx` op een andere server
en plaatst automatisch een eigen webpagina met een afbeelding.

---

## Structuur
Het bestand `hosts` is de inventory.
Hierin staat de andere server waarop het playbook wordt uitgevoerd.
De server zit in de groep `otherservers`.

---

## Uitvoeren
Ik voer dit uit:

Eerst en vooral SSH opstarten:

```bash
sudo systemctl start ssh
sudo systemctl status ssh
```

1. Test de connectie:
```bash
ansible otherservers -m ping
```

2. Run het playbook:
```bash
ansible-playbook install_nginx_website.yaml
```

---

## Controle (bewijs)
1. Controleer de status van Nginx:
```bash
sudo systemctl status nginx
```

2. Controleer of de bestanden aanwezig zijn:
```bash
ls -l /var/www/html
```

3. Test in de browser of met curl:
```bash
curl http://192.0.2.4
```
of in de browser:
```
http://192.0.2.4
```

De webpagina en afbeelding moeten zichtbaar zijn.

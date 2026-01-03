# A1 – Ansible Lab 7.4.8

## Beschrijving
In dit experiment heb ik Lab 7.4.8 uitgevoerd.
Het doel is om te tonen dat:
- Ansible correct werkt
- Ansible verbinding kan maken met de webserver (groep `webservers`)
- playbooks correct uitgevoerd worden

Dit lab focust op Ansible

---

## 1. ansible.cfg
`ansible.cfg` bevat basisinstellingen voor Ansible (zoals in het lab).
Hierdoor moet ik niet telkens extra opties meegeven bij een command of playbook.

---

## 2. hosts (inventory)
Het bestand `hosts` is de inventory.
Hierin staat welke server(s) Ansible beheert.
In Lab 7.4.8 staat de webserver in de groep `webservers`.

Voorbeeld (zoals in het lab):
```ini
[webservers]
192.0.2.3 ansible_user=devasc ansible_password=Cisco123!
```

- De groepsnaam `webservers` komt overeen met `hosts: webservers` in de playbooks.
- De IP en login moeten juist zijn, anders kan Ansible niet verbinden

---

## 3. Testen van de verbinding
Voor ik een playbook run, test ik eerst of Ansible de host kan bereiken.

### 3.1 Ping test
```bash
ansible webservers -m ping
```

### 3.2 Eenvoudige command test
Dit hoort bij het lab: een echo uitvoeren op de webserver.
```bash
ansible webservers -m command -a "/bin/echo hello world"
```

---

## 4. Playbook 1: test_apache_playbook.yaml
Dit playbook voert dezelfde echo-test uit, maar dan via een playbook.

Inhoud (zoals in het lab):
```yaml
---
- hosts: webservers
  tasks:
    - name: run echo command
      command: /bin/echo hello world
```

Uitvoeren:
```bash
ansible-playbook test_apache_playbook.yaml\
```

---

## 5. Playbook 2: install_apache_playbook.yaml
Dit playbook installeert Apache en gebruikt een handler om Apache te herstarten.

Uitvoeren:
```bash
ansible-playbook install_apache_playbook.yaml
```
---

## 6. Controleren of Apache draait
Na het playbook controleer ik de status van Apache.

### 6.1 Controleren op de webserver
Op de webserver:
```bash
sudo systemctl status apache2
```
En dan navigeer ik op Chrome : http://192.0.2.3/ , en daar zien ik mijn website
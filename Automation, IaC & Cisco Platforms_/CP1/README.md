# CP1 – Automation, IaC & Cisco Platforms (Spreadsheet)

## Uitleg per product

### 1) Ansible
**Wat is het?**  
Ansible is een automation tool (IaC) om servers automatisch te configureren.

**Waarvoor gebruikte ik het?**  
Ik gebruikte Ansible om:
- Apache2 te installeren
- bestanden te kopiëren (index.html en afbeeldingen)
- services te herstarten met handlers

**Hoe verbind ik?**  
Via **SSH** naar de server.

**Authenticatie**  
Met een **SSH key** of een SSH password.

**Data format**  
Playbooks zijn geschreven in **YAML**.

---

### 2) Docker
**Wat is het?**  
Docker is een platform om applicaties in containers te runnen.

**Waarvoor gebruikte ik het?**  
Ik gebruikte Docker om:
- een Docker image te bouwen (met een Dockerfile)
- een container te starten met poort mapping
- mijn Flask webapp te runnen in een container

**Hoe verbind ik?**  
Via de **Docker CLI** (`docker build`, `docker run`, `docker ps`).

**Authenticatie**  
Lokaal meestal geen login nodig.

**Data format**  
Docker gebruikt een **Dockerfile** om een image te bouwen.

---

### 3) Git
**Wat is het?**  
Git is een version control systeem. Hiermee kan ik versies van mijn code bewaren.

**Waarvoor gebruikte ik het?**  
Ik gebruikte Git om:
- bestanden toe te voegen (`git add`)
- wijzigingen op te slaan (`git commit`)
- mijn repo up-to-date te houden

**Hoe verbind ik?**  
Git werkt lokaal via de terminal.

**Authenticatie**  
Lokaal geen login nodig.
Pas bij push naar GitHub heb ik login/token nodig.

---

### 4) GitHub
**Wat is het?**  
GitHub is een online platform om Git repositories te hosten en te delen.

**Waarvoor gebruikte ik het?**  
Ik gebruikte GitHub om:
- mijn DevOps repository online te zetten
- mijn experimenten te delen met de leerkracht
- README’s en code te bewaren

**Hoe verbind ik?**  
Via **HTTPS** of **SSH**.

**Authenticatie**  
Met username + **token** (Personal Access Token) of SSH key.

---

### 5) Jenkins
**Wat is het?**  
Jenkins is een CI/CD tool. Dit betekent dat Jenkins automatisch builds en tests kan uitvoeren.

**Waarvoor gebruikte ik het?**  
Ik gebruikte Jenkins om:
- mijn sample app te builden
- automatisch tests te runnen
- een pipeline te maken (CI/CD)

**Hoe verbind ik?**  
Via de **Jenkins Web UI** (browser) en via GitHub.

**Authenticatie**  
Met Jenkins login (admin user).

**Data format / pipeline**
Jenkins gebruikt jobs en pipelines (GUI of pipeline script).

---

### 6) Linux
**Wat is het?**  
Linux is het besturingssysteem van mijn DEVASC VM.

**Waarvoor gebruikte ik het?**  
Ik gebruikte Linux om:
- Python scripts uit te voeren
- Ansible playbooks te runnen
- Docker containers te beheren
- commando’s te testen in de terminal

**Hoe verbind ik?**  
Via terminal en soms via SSH naar andere machines.

**Authenticatie**  
Met username + password of SSH key.

---

### 7) RESTCONF
**Wat is het?**  
RESTCONF is een manier om netwerk devices te beheren via een REST API.

**Waarvoor gebruikte ik het?**  
Ik gebruikte RESTCONF in de theorie om te leren hoe je:
- netwerk data kan opvragen
- configuratie kan aanpassen via API calls

**Hoe verbind ik?**  
Via **HTTPS** met REST API calls.

**Authenticatie**  
Vaak met Basic Auth of token.

**Data format**
RESTCONF gebruikt meestal **JSON** of **XML**.

---

### 8) Webex Teams (Webex API)
**Wat is het?**  
Webex is een Cisco platform voor messaging en collaboration.
De Webex API laat mij toe om automatisch acties te doen met Python.

**Waarvoor gebruikte ik het?**  
Ik gebruikte Webex API om:
- rooms op te vragen
- memberships te bekijken
- messages te sturen (ook met markdown)

**Hoe verbind ik?**  
Via **HTTPS** naar de Webex REST API.

**Authenticatie**  
Met een **Bearer Token**.

**Data format**
Webex API gebruikt **JSON**.
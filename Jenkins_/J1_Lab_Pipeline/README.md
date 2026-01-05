# Lab 6.3.6 – CI/CD Pipeline met Jenkins (alle stappen + commando’s)

## Beschrijving
In dit lab heb ik een **CI/CD pipeline** gebouwd met **GitHub + Docker + Jenkins**.
Ik heb een sample-app in GitHub gezet, Jenkins in Docker gestart, en daarna in Jenkins:
- een **build job** gemaakt
- een **test job** gemaakt
- een **pipeline job** gemaakt die alles automatisch start
---

## Stap 1: Git instellen (naam en e-mail)
Ik heb Git lokaal ingesteld zodat commits een naam en e-mail hebben:

```bash
git config --global user.name "tsuyuki77"
git config --global user.email andrea.insalaca@student.odisee.be
```
---

## Stap 2: Naar sample-app map gaan en Git repository maken
Ik ben naar de sample-app (J1_Lab_Pipeline) map gegaan en heb Git gestart:

```bash
cd labs/devnet-src/Jenkins/sample-app/
git init
```

**Uitleg:** `git init` maakt van deze map een Git repository.

---

## Stap 3: Git koppelen aan GitHub repository
Ik heb de remote `origin` ingesteld (met mijn GitHub username):

```bash
git remote add origin https://github.com/<github-username>/sample-app.git
```

**Uitleg:** hierdoor kan ik pushen naar mijn GitHub repository.

---

## Stap 4: Eerste upload naar GitHub (add, status, commit, push)
Ik heb alle bestanden toegevoegd, gecontroleerd en gepusht:

```bash
git add *
git status
git commit -m "Committing sample-app files."
git push origin master
```

Tijdens `git push` vroeg GitHub om login:

- mijn GitHub username: **tsuyuki77** 
- mijn token: **secret**

**Uitleg:**
- `git add *` zet bestanden klaar
- `git commit` slaat wijziging op
- `git push` upload naar GitHub

---

## Stap 5: Poort aanpassen van 8080 naar 5050
Omdat Jenkins op **8080** draait, heb ik de app-poort aangepast naar **5050**.

### 5.1 In `sample_app.py`
Ik veranderde de port naar 5050 (1 keer):

```python
sample.run(host="0.0.0.0", port=5050)
```

### 5.2 In `sample-app.sh`
Ik veranderde poort 8080 naar 5050 (3 keer). Belangrijke regels:

```bash
echo "EXPOSE 5050" >> tempdir/Dockerfile
docker run -t -d -p 5050:5050 --name samplerunning sampleapp
```

**Uitleg:** zo kan de app draaien op poort 5050, zonder conflict met Jenkins.

---

## Stap 6: App bouwen en testen met het build-script
Ik heb het script uitgevoerd om een Docker image te bouwen en de container te starten:

```bash
bash ./sample-app.sh
```

**Uitleg:** dit script doet o.a.:
- maakt een tijdelijke map
- kopieert bestanden
- maakt een Dockerfile
- bouwt een image
- start een container

Belangrijke Docker commando’s die in het script gebeuren:

```bash
docker build -t sampleapp .
docker run -t -d -p 5050:5050 --name samplerunning sampleapp
docker ps -a
```

Daarna heb ik in de browser getest:
- `http://localhost:5050`

---

## Stap 7: Wijzigingen pushen naar GitHub
Na de poort-wijziging heb ik opnieuw gepusht:

```bash
git add *
git status
git commit -m "Changed port from 8080 to 5050."
git push origin master
```

---

## Stap 8: Jenkins Docker image downloaden
Ik heb de Jenkins image gedownload:

```bash
docker pull jenkins/jenkins:lts
```

**Uitleg:** hiermee download ik de laatste versie.

---

## Stap 9: Jenkins container starten (met Docker-in-Docker mounts)
Ik heb Jenkins gestart met exact dit commando in één lijn:

```bash
docker run --rm -u root -p 8080:8080 -v jenkins-data:/var/jenkins_home -v $(which docker):/usr/bin/docker -v /var/run/docker.sock:/var/run/docker.sock -v "$HOME":/home --name jenkins_server jenkins/jenkins:lts
```

**Uitleg (vanuit het lab):**
- `--rm` = container wordt verwijderd bij stoppen
- `-u root` = Jenkins draait als root (nodig om Docker commando’s te mogen uitvoeren)
- `-p 8080:8080` = Jenkins via localhost:8080
- `-v jenkins-data:/var/jenkins_home` = Jenkins-data blijft bewaard
- `-v $(which docker):/usr/bin/docker` + `-v /var/run/docker.sock:/var/run/docker.sock` = Docker gebruiken **in** Jenkins container
- `-v "$HOME":/home` = home map beschikbaar maken
- `--name jenkins_server` = containernaam

---

## Stap 10: Initial admin password tonen
ik was het wachtwoord kwijt, en haalde het ik opnieuw op:

```bash
docker exec -it jenkins_server /bin/bash
cat /var/jenkins_home/secrets/initialAdminPassword
exit
```

**Uitleg:** hiermee ga ik in de Jenkins container en lees ik het wachtwoordbestand.

---

## Stap 11: Jenkins web setup
Ik ging naar:

- `http://localhost:8080/`

**Login gegevens:**
- **Username:** `admin`
- **Password:** e47cc7b1d8c345c58b7ae7df2868f178

Daarna:
- Ik installeerde **suggested plugins**
- Ik klikte **Skip and continue as admin**
- Instance configuration: **Save and Finish**
- Daarna: **Start using Jenkins**

---

## Stap 12: Jenkins job 1 maken – BuildAppJob (Freestyle)
In Jenkins maakte ik een nieuwe job:

- **Naam:** `BuildAppJob`
- **Type:** Freestyle project
- **SCM:** Git
- **Repository URL:** `https://github.com/<github-username>/sample-app.git`
- **Credentials:** GitHub username + PAT

### Build stap (Execute shell)
Ik voegde dit commando toe:

```bash
bash ./sample-app.sh
```

**Uitleg:** Jenkins haalt de code op en bouwt de app door het script te runnen.

---

## Stap 13: Jenkins job 2 maken – TestAppJob (Freestyle)
Nieuwe job:

- **Naam:** `TestAppJob`
- **Type:** Freestyle project
- **SCM:** None
- **Build Triggers:** “Build after other projects are built”
  - **Projects to watch:** `BuildAppJob`

### Test stap (Execute shell)
Ik gebruikte deze test (if moet op één lijn):

```bash
if curl http://172.17.0.1:5050/ | grep "You are calling me from 172.17.0.1"; then
  exit 0
else
  exit 1
fi
```

**Uitleg:**
- `curl` haalt de webpagina op
- `grep` zoekt de juiste tekst
- exit 0 = test OK
- exit 1 = test FAIL

### Voor de test: oude app-container stoppen en verwijderen
Volgens het lab moest ik eerst de container opruimen:

```bash
docker stop samplerunning
docker rm samplerunning
```

---

## Stap 14: Pipeline job maken – SamplePipeline
Ik maakte een job:

- **Naam:** `SamplePipeline`
- **Type:** Pipeline

### Pipeline script
Ik plakte dit script:

```groovy
node {
  stage('Preparation') {
    catchError(buildResult: 'SUCCESS') {
      sh 'docker stop samplerunning'
      sh 'docker rm samplerunning'
    }
  }
  stage('Build') {
    build 'BuildAppJob'
  }
  stage('Results') {
    build 'TestAppJob'
  }
}
```

**Uitleg:**
- Preparation: stopt/verwijdert oude container (fouten worden genegeerd met `catchError`)
- Build: start de BuildAppJob
- Results: start de TestAppJob

---

## Resultaat
- Jenkins kan de app **automatisch bouwen**
- Jenkins kan de app **automatisch testen**
- De pipeline voert alles uit in de juiste volgorde

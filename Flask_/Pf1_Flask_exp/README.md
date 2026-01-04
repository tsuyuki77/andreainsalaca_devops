# Pf1 – Flask-experiment (Sample App)

## Beschrijving
In dit experiment heb ik een eenvoudige Flask webapp gebruikt,
zoals gezien in de lessen bij de Sample App.
De applicatie toont het IP-adres van de client.

---

## Stap 2: Flask applicatie

De Flask app bevat één route (`/`) die een HTML template terugstuurt, ik heb hier van 8080 naar 5050 aangepast.

```python
from flask import Flask, request, render_template

microweb_app = Flask(__name__)

@microweb_app.route("/")
def main():
    return render_template(
        "index.html",
        client_ip=request.remote_addr
    )

if __name__ == "__main__":
    microweb_app.run(host="0.0.0.0", port=5050)
```

---

## Stap 3: Flask app starten
```bash
python3 flask_app.py
```
---

De Flask webpagina toont het IP-adres van de client.
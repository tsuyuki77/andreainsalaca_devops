# Pf3 – Eigen Flask microservice-experiment

## Beschrijving
In dit experiment heb ik mijn Flask microservice uitgebreid
met eigen logica.
Naast het IP-adres van de client toon ik ook de huidige datum en tijd.

---

## Flask applicatie met datetime

```python
from flask import Flask, request, render_template
import datetime

microweb_app = Flask(__name__)

@microweb_app.route("/")
def main():
    return render_template(
        "index.html",
        client_ip=request.remote_addr,
        datetime_now=datetime.datetime.now()
    )

if __name__ == "__main__":
    microweb_app.run(host="0.0.0.0", port=5050)
```

---

## Resultaat
De microservice toont dynamische datum en tijd.

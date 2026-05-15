# URL e routing

## File `urls.py`

In DSite gli URL vengono gestiti dal file urls.py.

Questo file collega un indirizzo web a una View Python.

Ad esempio:

```python
from dsite.urls import path
from . import views
urlpatterns = [
    path("/", views.home),
    path("/about", views.about),
]
```

In questo esempio:

| URL | View |
|-----|------|
| / | `home` |
| /about | `about` |

Quando un utente apre **http://127.0.0.1:8000/about** DSite eseguirà **views.about**

---

## Views

Le Views sono funzioni Python che gestiscono le pagine.

Si trovano nel file views.py.

Ad esempio:

```python
from dsite.shortcuts import render
def home(request):
    return render(
        request,
        "homepage.xml"
    )
def about(request):
    return render(
        request,
        "about.xml"
    )
```

La funzione render():

1. Apre il file XML
2. Processa i tag
3. DSite genera HTML
4. Invia la pagina al browser


---

## Creare una nuova pagina

Creiamo **pages/about.xml** col codice:

```xml
<expand file="diario_di_viaggio:base.xml" />

<html-block>

<h1>Chi siamo</h1>

<p>
Diario Di Viaggio è un sito creato con DSite.
</p>

</html-block>
```

- `expand` - Prende il layout base
- `html-block` - Quello che l'utente vede
  - `h1` - Titolo
  - `p` - Paragrafo

Ora la pagina sará disponibile su **http://127.0.0.1:8000/about**.

---

## PythonTag XML

DSite supporta tag XML speciali per eseguire Python dentro le pagine.

Ad esempio:

```xml
<pyfunct>
<pycontent>

name = "Domenico"
print(f"Ciao {name}!")

</pycontent>
</pyfunct>
```

- `pyfunct` - Il PythonTag
  - `pycontent` - Il codice Python
    - `name = "Domenico"` - Una variabile
    - `print(f"Ciao {name}!")` - Restitusce una stringa (per l'HTML dato al browser, `p`)


E il risultato sará:

```xml
<p>Ciao Domenico!</p>
```

Infatti, quando DSite incontra `pyfunct`, DSite:

1. Legge <pyfunct>
2. Esegue il codice Python
3. Inserisce il risultato nella pagina


---

## Variabili dinamiche

Puoi creare contenuti dinamici:

```xml
<pyfunct>
<pycontent>

for i in range(5):
    print(f"<p>Viaggio numero {i}</p>")

</pycontent>
</pyfunct>
```

Il risultato sará:

```xml
<p>Viaggio numero 0</p>
<p>Viaggio numero 1</p>
<p>Viaggio numero 2</p>
<p>Viaggio numero 3</p>
<p>Viaggio numero 4</p>
```

---

## Attenzione alla sicurezza

I PythonTag permettono di eseguire codice Python.

Per questo motivo DSite:

- Deve controllare il codice
- Deve proteggere il server
- Deve limitare funzioni pericolose

Esempio di codice da bloccare:

```python
import os
os.remove("file_importante.txt")
```

---

## Complimenti!

Ora sai usare:

- URL
- Routing
- ViewsXML dinamico
- PythonTag

Nel prossimo capitolo:

- Forms
- Models
- Database
- AdminSite

# DSite FAQs

Benvenuto nelle FAQ ufficiali di DSite!

Qui trovi le domande più frequenti sul framework.

---

# Installazione

## Come installo DSite?

Usa PIP:

```bash
pip install dsite
```

---

## Come controllo la versione installata?

```bash
dsite --version
```

---

## Come creo un progetto DSite?

```bash
dsite createproject nome_progetto
```

---

## Qual è la struttura iniziale di un progetto?

```text
nome_progetto/
│
├── manage.py
│
└── nome_progetto/
    ├── urls.py
    ├── views.py
    ├── adminsite.py
    ├── models.py
    ├── forms.py
    ├── settings.py
    │
    └── pages/
        ├── homepage.xml
        └── base.xml
```

---

## Come avvio il server?

```bash
python manage.py runserver nome_progetto
```

---

## Dove apro il sito?

Apri:

```text
http://127.0.0.1:8000
```

---

# URL e Routing

## Dove si gestiscono gli URL?

Nel file:

```python
urls.py
```

---

## Esempio di routing

```python
from dsite.urls import path
from . import views

urlpatterns = [
    path("/", views.home),
    path("/about", views.about),
]
```

---

## Come funzionano le Views?

Le Views sono funzioni Python che gestiscono le pagine.

Esempio:

```python
from dsite.shortcuts import render

def home(request):
    return render(
        request,
        "homepage.xml"
    )
```

---

## Cosa fa render()?

La funzione `render()`:

* apre il file XML
* processa i tag DSite
* genera HTML
* invia la pagina al browser

---

# DSite Pages

## Dove si trovano le pagine XML?

Dentro:

```text
pages/
```

---

## Esempio di homepage

```xml
<expand file="diario_di_viaggio:base.xml" />

<html-block>
<h1>Benvenuto!</h1>

<p>
Questo è il mio primo sito creato con DSite.
</p>
</html-block>
```

---

## Cos’è `<html-block>`?

È un tag DSite che permette di scrivere HTML normale dentro una pagina XML.

---

# Expand System

## Cos’è `<expand />`?

Permette di usare un layout condiviso.

Esempio:

```xml
<expand file="diario_di_viaggio:base.xml" />
```

---

## Come funziona `<expand />`?

DSite:

1. apre `base.xml`
2. cerca `<file-html />`
3. inserisce il contenuto della pagina corrente

---

## A cosa serve?

Serve per creare:

* layout
* navbar
* footer
* temi condivisi

---

## Esempio di base.xml

```xml
<add-base-classification />

<html-block>
<p>
<b>DSite</b> -
<a href="diario_di_viaggio:home">Home</a>
</p>

<hr>

<file-html />
</html-block>
```

---

# PythonTag XML

## Cos’è `<pyfunct>`?

Permette di eseguire Python dentro le pagine XML.

---

## Esempio base

```xml
<pyfunct>
<pycontent>
name = "Domenico"
print(f"Ciao {name}!")
</pycontent>
</pyfunct>
```

---

## Come funziona?

DSite:

1. legge `<pyfunct>`
2. esegue Python
3. inserisce il risultato nella pagina

---

## Posso creare contenuti dinamici?

Sì!

Esempio:

```xml
<pyfunct>
<pycontent>
for i in range(5):
    print(f"<p>Viaggio numero {i}</p>")
</pycontent>
</pyfunct>
```

---

## I PythonTag sono sicuri?

DSite deve:

* controllare il codice
* limitare funzioni pericolose
* proteggere il server

---

## Esempio di codice da bloccare

```python
import os
os.remove("file_importante.txt")
```

---

# Forms

## Dove si creano i Forms?

Nel file:

```python
forms.py
```

---

## Esempio di Form

```python
from dsite.forms import Form
from dsite.forms import TextField

class TravelForm(Form):
    title = TextField(
        label="Titolo del viaggio"
    )

    description = TextField(
        label="Descrizione"
    )
```

---

## Come usare un Form in XML?

```xml
<form method="POST">

<form-token type="ea" />

<input type="text" name="title" />

<textarea name="description"></textarea>

<button>
Salva
</button>

</form>
```

---

## Cos’è `<form-token />`?

Serve a proteggere il database e controllare i permessi.

---

## Tipi disponibili di form-token

| Tipo | Significato              |
| ---- | ------------------------ |
| ea   | Edit App                 |
| eug  | Edit Users and/or Groups |

---

# Models e Database

## Dove si creano i Models?

Nel file:

```python
models.py
```

---

## Esempio di Model

```python
from dsite.db import Model
from dsite.db import TextColumn

class Travel(Model):
    title = TextColumn(
        max_length=100
    )

    description = TextColumn()
```

---

## Come salvo dati?

```python
travel = Travel()

travel.title = "Milano"
travel.description = "Viaggio bellissimo"

travel.save()
```

---

## Come leggere tutti gli elementi?

```python
travels = Travel.objects.all()
```

---

## Come leggere un elemento?

```python
travel = Travel.objects.get(id=1)
```

---

## Come eliminare un elemento?

```python
travel.delete()
```

---

## DSite usa SQL manuale?

No.

DSite utilizza un ORM (Object Relational Mapper).

---

# Migrazioni

## Come creo una migrazione?

```bash
python manage.py makemigrations nome_progetto
```

---

## Come applico le migrazioni?

```bash
python manage.py migrate nome_progetto
```

---

# AdminSite

## Cos’è AdminSite?

È il pannello amministratore di DSite.

---

## A cosa serve?

Permette di:

* gestire database
* modificare utenti
* creare contenuti
* controllare il sito

---

## Come registro un Model?

Nel file `adminsite.py`:

```python
from dsite.admin import register
from .models import Travel

register(Travel)
```

---

## Come avvio AdminSite?

```bash
python manage.py adminsite diario_di_viaggio
```

---

## Dove si trova AdminSite?

```text
http://127.0.0.1:8000/admin
```

---

# Generale

## DSite è open source?

Sì.

---

## DSite usa XML?

Sì, usa DSite Pages XML.

---

## DSite è adatto ai principianti?

Sì!
È progettato per essere semplice e potente.

---

# Altro

## Perché MacOS mi dá problemi di permessi ai comandi `dsite` e `dsite-admin`?

Se stai usando Mac OS X, puoi ricevere messaggio "permesso negato" quando tenti di usare `dsite` e `dsite-admin`. 
Questo è dovuto al fatto che, nei sistemi basati su Unix, come OS X, un file deve essere marcato come "eseguibile" prima di poter essere usato come programma. Per fare ciò, apri `Terminal.app` e naviga (usando il comando `cd`) fino alla directory dove è installato `dsite` e `dsite-admin`.
Esegui il comando 

```bash
sudo chmod +x dsite
```

e 

```bash
sudo chmod +x dsite-admin
```
---

## Non trova i comandi `dsite` e `dsite-admin`, cosa devo fare?

`dsite` e `dsite-admin` dovrebbe essere nella path di sistema se hai installato DSite tramite pip. Se non è nella path, fai questo:

- **Su Windows:** vai in Start, cerca "Variabili" e apri "Modifica le variabili di ambiente relative all'utente" o simile. Poi, clicca sulla variabile **Path**, clicca "modifica" e aggiungi il percorso `C:\(Percorso di Python)\Scripts`
- **Su MacOS/Linux:** vai nella cartella utente, apri il file `~/.bashrc` (o se usi zsh `~/.zshrc`), e aggiungi la riga `export PATH="$PATH:/(Percorso di Python)/bin`
- **Se non vuoi modificare il PATH:** Usa i comandi equivalenti `python -m dsite.cli` per `dsite`, `python -m dsite.admin_cli` per `dsite-admin`

---

## Non trovo risposta alle mie domande. Cosa devo fare
Se non trova risposta alle sue domande, compili il [Form di assistenza](https://forms.gle/jKukCSMzPgCELgUf7)

---

# Fine

Grazie per usare DSite 🚀

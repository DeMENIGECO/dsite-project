## Forms, Models, Database e AdminSite

## Forms

In DSite i Forms permettono agli utenti di inviare dati al server.

I Forms vengono definiti in **forms.py**.

Ad esempio:

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

## Usare un Form in una pagina XML

Ad esempio:

```xml
<expand file="diario_di_viaggio:base.xml" />

<html-block>

<h1>Nuovo Viaggio</h1>

<form method="POST">

<form-token type="ea" />

<input type="text" name="title" />

<textarea name="description"></textarea>

<button>
Salva
</button>

</form>

</html-block>
```

- `expand` - Importa un layout base
- `html-block` - Quello che l'utente vede
  - `h1` - Titolo
  - `form` - Il modulo
    - `form-token` - Il token e tipo di token per modificare il Database
    - `input` - Input di testo
    - `textarea` - Campo di testo
      
---

## Curiositá: form-token

Il tag:

```xml
<form-token type="ea" />
```

serve a proteggere il database.

I tipi sono:

| Tipo | Significato |
|------|-------------|
| ea | Edit App |
| eug | Edit Users and/or Groups |

DSite controllerà automaticamente:

- Autorizzazioni
- Sicurezza
- Validità della richiesta

---

## Models

I Models rappresentano i dati del database.

Si trovano in models.py.

Ad esempio:

```python
from dsite.db import Model
from dsite.db import TextColumn

class Travel(Model):
    title = TextColumn(
        max_length=100
    )

    description = TextColumn()
```

Questo creerà una tabella database simile a:

| id | title | description |
|----|-------|-------------|
| 1 | Roma | Bellissimo viaggio |

---

## Salvate dati

Ecco un esempio di una view:

```python
from .models import Travel

def create_travel(request):

    if request.method == "POST":

        travel = Travel()

        travel.title = request.POST["title"]
        travel.description = request.POST["description"]

        travel.save()
```

DSite salverà automaticamente i dati nel database.

---

## Database

DSite utilizza un sistema ORM (Object Relational Mapper), infatti Questo permette di usare Python invece di scrivere SQL manuale.

---

## Esempio Query

Per creare un elemento:

```python
travel = Travel()

travel.title = "Milano"
travel.description = "Viaggio bellissimo"

travel.save()
```

E per leggere tutti gli elementi:

```python
travels = Travel.objects.all()
```

Poi, per leggere un’elemento:

```python
travel = Travel.objects.get(id=1)
```

Infine, per elimare:

```python
travel.delete(id=1)
```

---

## Migrazioni Database

Quando modifichi i Models, DSite deve aggiornare il database. Facciamo una migrazione:

```bash
python manage.py makemigrations diario_di_viaggio
```

e poi le applichiamo:

```bash
python manage.py migrate diario_di_viaggio
```

---

## AdminSite

DSite include un pannello amministratore chiamato **AdminSite**.

Serve per:

- Gestire database
- Modificare utenti
- Creare contenuti
- Controllare il sito

---

## Registrare un model

Apri **adminsite.py** e scrivi:

```python
from dsite.admin import register
from .models import Travel

register(Travel)
```

---

## Avviare l’AdminSite

Usate il comando:

```bash
python manage.py adminsite diario_di_viaggio
```

DSite creerá **http://127.0.0.1:8000/admin**.

---

## Come appare AdminSite

AdminSite permetterà di:

- Vedere tutti i viaggi
- Modificare elementi
- Eliminare dati
- Creare utenti
- Gestire permessi

---

## Complimenti!

Ora conosci:

- Forms
- Models
- ORM
- Database
- AdminSite

Il tuo progetto “Diario Di Viaggio” sta diventando una vera web app 🎉

# Installazione e creazione dell’app

Benvenuto in DSite!
In questa guida creeremo la nostra prima applicazione: **Diario Di Viaggio**.

---

## Installazione

Installa DSite con PIP, e visto che questa è la guida della 1.0.0:

```bash
pip install dsite==1.0.0
```

E verifica che sia installato correttamente:

```bash
dsite --version
```

---

## Creare un progetto

Creiamo un nuovo progetto DSite!

```bash
dsite createproject diario_di_viaggio
```

Entriamo nella cartella del progetto:

```bash
cd diario_di_viaggio
```

La struttura sarà:

```text
diario_di_viaggio/
│
├── manage.py
│
└── diario_di_viaggio/
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

- `manage.py` - Potremo gestire con questo file il progetto
- `urls.py` - Gli URLs che avrá
- `views.py` - Le viste degli URLs
- `adminsite.py` - Registra i Models
- `models.py` - I Models
- `forms.py` - I moduli
- `settings.py` - Impostazioni del progetto
- `homepage.xml` - La home iniziale
- `base.xml` - La base per le pagine iniziale

---

## Avviare il server

Avviamo il server:

```bash
python manage.py runserver diario_di_viaggio
```

DSite mostrerà:

```text
[DSite] Server avviato!
[DSite] URL: http://127.0.0.1:8000/
```

Apri il browser e visita **http://127.0.0.1:8000/**

Vedrai una pagina vuota al momento.

---

## La tua prima pagina

Apri `pages/homepage.xml` e scrivi:

```xml
<expand file="diario_di_viaggio:base.xml" />
<html-block>
<h1>Benvenuto in Diario Di Viaggio!</h1>
<p>
Questo è il mio primo sito creato con DSite.
</p>
</html-block>
```

- `expand` - Aggiunge una pagina template
- `html-block` - Quello che l'utente vede
  - `h1` - Titolo
  - `p` - Paragrafo

---

## Creare un layout base

Ora apri `pages/base.xml` e scrivi:

```xml
<add-base-classification />

<html-block>
<p>
<b>Diario Di Viaggio</b> -
<a href="diario_di_viaggio:home">Home</a>
</p>

<hr>

<file-html />
</html-block>
```

- `add-base-classifification` - Per poterlo usare in `expand`
- `html-block` - Quello che l'utente vede
  - `p` - Paragrafo
    - `b` - Grassetto
    - `a` - Link
  - `hr` - Linea separatoria
  - `file-html` - Il `html-block` usato nella pagina che usa il template

---

## Curiositá: Come funziona `expand`

Il tag:

```xml
<expand file="diario_di_viaggio:base.xml" />
```

permette di usare un file base condiviso.

DSite:

1. Apre base.xml
2. Cerca `file-html`
3. Inserisce il contenuto della pagina corrente

Questo sistema permette di creare:

- Layout
- Navbar
- Footer
- Temi condivisi

---

## Complimenti!

Hai creato la tua prima app con DSite 🎉

Nel prossimo capitolo imparerai:

- URL e routing
- Views
- Pythontag XML

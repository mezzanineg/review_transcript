# Editor Web per la Revisione di Trascrizioni Audio

Questa applicazione Flask consente di visualizzare, ascoltare e correggere trascrizioni testuali sincronizzate con file audio. È particolarmente utile per rivedere trascrizioni automatiche e confrontarle con i relativi file audio.

## Funzionalità

- Visualizzazione e riproduzione di file audio (.mp3)
- Caricamento e modifica di trascrizioni (.txt)
- Navigazione tra i file con pulsanti "precedente" e "successivo"
- Salvataggio automatico delle modifiche durante la navigazione
- Interfaccia utente semplice e reattiva

## Struttura del progetto

project-root/
├── app.py
├── templates/
│   └── index.html
├── static/
│   ├── audio/           # Contiene i file audio .mp3
│   └── transcripts/     # Contiene i file di testo .txt
└── README.md

I file .mp3 e .txt devono avere lo stesso nome base, ad esempio: "spot1.mp3" ↔ "spot1.txt".

## Requisiti

- Python 3.8 o superiore
- Flask

Installa i pacchetti richiesti:

pip install Flask

## Avvio dell'applicazione

1. Clona il repository:

git clone https://github.com/tuo-username/editor-trascrizioni.git
cd editor-trascrizioni

2. Avvia il server Flask:

python app.py

3. Apri il browser su http://127.0.0.1:5000

## Caricamento dei file

Inserisci i tuoi file:

- Audio in static/audio/
- Trascrizioni in static/transcripts/

Entrambi i file devono avere lo stesso nome base (es. "intervista01.mp3" e "intervista01.txt").

## Salvataggio

Le modifiche vengono salvate automaticamente quando si passa da un file all’altro.

## Compatibilità

Testato su:

- Chrome 
- macOS 

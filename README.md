# Convertitore
Applicazione per convertire unità di misura (lunghezza, massa, velocità, forza, temperatura, potenza) su macOS e Windows.

# Convertitore

Applicazione grafica per convertire unità di misura su macOS e Windows.  
Supporta le seguenti categorie: lunghezza, massa, velocità, forza, temperatura e potenza.

## Funzionalità

- Conversioni rapide tra unità comuni.
- Interfaccia grafica semplice e “Apple-like” su macOS.
- Supporto Windows con icona personalizzata.
- Possibilità di creare DMG (macOS) o EXE (Windows) direttamente dai sorgenti.

## Codice sorgente

Il codice sorgente è incluso nel repository:

- `gui.py` → interfaccia grafica
- `unit_converter.py` → modulo di conversione delle unità

### Requisiti per eseguire da sorgente

- Python 3.13+
- Tkinter (incluso in Python)
- PyInstaller (opzionale, per creare eseguibili)

### Esecuzione

```bash
python gui.py

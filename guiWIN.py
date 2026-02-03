# gui.py
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox
from unit_converterWIN import parse_and_convert, list_units

# --- Funzione Converti ---
def convert_action():
    try:
        cat = categoria_var.get()
        val = valore_var.get()
        from_u = from_var.get()
        to_u = to_var.get()
        if not cat or not val or not from_u or not to_u:
            raise ValueError("Compila tutti i campi")
        result = parse_and_convert(cat, val, from_u, to_u)
        output_var.set(f"Risultato: {result}")
    except Exception as e:
        messagebox.showerror("Errore", str(e))

# --- Aggiorna unità quando cambia categoria ---
def update_units(event=None):
    cat = categoria_var.get()
    units = list_units(cat)
    from_combo.config(values=units)
    to_combo.config(values=units)
    from_var.set('')
    to_var.set('')
    output_var.set('')

# --- Finestra principale ---
root = tb.Window(themename="flatly")
root.title("Convertitore di unità")
root.geometry("850x700")

frame = tb.Frame(root, padding=20)
frame.pack(expand=True, fill="both")

# Titolo
tb.Label(frame, text="Convertitore di unità", font=("Segoe UI", 16, "bold")).pack(pady=(0,15))

# Dropdown categoria
categoria_var = tb.StringVar()
tb.Label(frame, text="Categoria:").pack(anchor=W)
cat_combo = tb.Combobox(frame, values=["Lunghezza","Massa","Potenza","Velocità","Forza","Temperatura"],
                        textvariable=categoria_var, bootstyle="info")
cat_combo.pack(fill=X, pady=5)
cat_combo.bind("<<ComboboxSelected>>", update_units)

# Input valore
tb.Label(frame, text="Valore:").pack(anchor=W)
valore_var = tb.StringVar()
tb.Entry(frame, textvariable=valore_var, font=("Segoe UI", 12)).pack(fill=X, pady=5)

# Dropdown unità
tb.Label(frame, text="Da unità:").pack(anchor=W)
from_var = tb.StringVar()
from_combo = tb.Combobox(frame, textvariable=from_var, bootstyle="secondary")
from_combo.pack(fill=X, pady=5)

tb.Label(frame, text="A unità:").pack(anchor=W)
to_var = tb.StringVar()
to_combo = tb.Combobox(frame, textvariable=to_var, bootstyle="secondary")
to_combo.pack(fill=X, pady=5)

# Bottone Converti
tb.Button(frame, text="Converti", bootstyle="success", command=convert_action).pack(pady=10)

# Output
output_var = tb.StringVar()
tb.Label(frame, textvariable=output_var, font=("Segoe UI", 12, "bold")).pack(pady=5)

root.mainloop()

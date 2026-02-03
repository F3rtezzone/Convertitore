# gui.py
import tkinter as tk
from tkinter import ttk, messagebox
from unit_converterMacOS import (
    convert_length, convert_mass, convert_power,
    convert_temperature, convert_force, convert_speed
)

# --- Unità e categorie ---
CATEGORIES = {
    "Lunghezza": sorted(['m','km','cm','mm','um','nm','nmi','mi','ft','in']),
    "Massa": sorted(['g','kg','t']),
    "Potenza": sorted(['w','kw','mw','hp']),
    "Temperatura": ['C','F','K'],
    "Forza": sorted(['n','kn','lbf','dyn']),
    "Velocità": sorted(['mps','kmh','mph','kt']),
}

CONVERTERS = {
    "Lunghezza": convert_length,
    "Massa": convert_mass,
    "Potenza": convert_power,
    "Temperatura": convert_temperature,
    "Forza": convert_force,
    "Velocità": convert_speed,
}

class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Convertitore di unità")
        self.root.geometry("480x380")
        self.root.resizable(False, False)

        style = ttk.Style(root)
        style.theme_use("aqua")
        style.configure("TFrame", background="#f2f2f2")
        style.configure("TLabel", background="#f2f2f2", font=("Helvetica", 12))
        style.configure("TButton", font=("Helvetica", 12))
        style.configure("TCombobox", font=("Helvetica", 12))

        self.main_frame = ttk.Frame(root, padding=20)
        self.main_frame.pack(expand=True, fill="both")

        ttk.Label(self.main_frame, text="Scegli Categoria", font=("Helvetica", 16, "bold")).pack(pady=(0, 10))
        self.category_var = tk.StringVar()
        self.category_cb = ttk.Combobox(self.main_frame, textvariable=self.category_var, state="readonly")
        self.category_cb['values'] = list(CATEGORIES.keys())
        self.category_cb.pack(pady=5)
        self.category_cb.bind("<<ComboboxSelected>>", self.show_unit_inputs)

        self.unit_frame = ttk.Frame(self.main_frame)
        self.unit_frame.pack(pady=15)

    def show_unit_inputs(self, event):
        for widget in self.unit_frame.winfo_children():
            widget.destroy()

        cat = self.category_var.get()
        units = CATEGORIES[cat]
        self.converter = CONVERTERS[cat]

        ttk.Label(self.unit_frame, text="Unità Sorgente").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.src_var = tk.StringVar()
        self.src_cb = ttk.Combobox(self.unit_frame, textvariable=self.src_var, values=units, state="readonly", width=12)
        self.src_cb.grid(row=0, column=1, padx=5, pady=5)
        self.src_cb.current(0)

        ttk.Label(self.unit_frame, text="Unità Destinazione").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.dst_var = tk.StringVar()
        self.dst_cb = ttk.Combobox(self.unit_frame, textvariable=self.dst_var, values=units, state="readonly", width=12)
        self.dst_cb.grid(row=1, column=1, padx=5, pady=5)
        self.dst_cb.current(1 if len(units)>1 else 0)

        ttk.Label(self.unit_frame, text="Primo Valore").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.val1_entry = ttk.Entry(self.unit_frame, width=15, font=("Helvetica", 12))
        self.val1_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self.unit_frame, text="Secondo Valore (opzionale)").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.val2_entry = ttk.Entry(self.unit_frame, width=15, font=("Helvetica", 12))
        self.val2_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Button(self.unit_frame, text="Converti", command=self.convert).grid(row=4, column=0, columnspan=2, pady=10)

        self.output_var = tk.StringVar()
        ttk.Label(self.unit_frame, textvariable=self.output_var, font=("Helvetica", 12, "bold")).grid(row=5, column=0, columnspan=2, pady=5)

    def convert(self):
        vals = [self.val1_entry.get().strip(), self.val2_entry.get().strip()]
        results = []
        for i, v in enumerate(vals, start=1):
            if not v: continue
            try:
                fval = float(v)
                out = self.converter(fval, self.src_var.get().lower(), self.dst_var.get().lower())
                results.append(f"Valore {i}: {out}")
            except Exception as e:
                results.append(f"Valore {i}: Errore ({e})")
        self.output_var.set("\n".join(results) if results else "<nessun valore>")

if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConverterApp(root)
    root.mainloop()

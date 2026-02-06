# gui.py
import tkinter as tk
from tkinter import ttk, messagebox
from unit_converter import CATEGORIES, convert, convert_temperature


class ConvertitoreApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Convertitore")
        self.geometry("420x420")
        self.resizable(False, False)

        self.style = ttk.Style(self)
        self.style.theme_use("default")

        self.container = ttk.Frame(self, padding=20)
        self.container.pack(fill="both", expand=True)

        self.show_home()

    # ---------- HOME ----------
    def show_home(self):
        self.clear()
        ttk.Label(
            self.container,
            text="Convertitore",
            font=("Helvetica", 22, "bold")
        ).pack(pady=15)

        for cat in CATEGORIES:
            ttk.Button(
                self.container,
                text=cat,
                command=lambda c=cat: self.show_converter(c)
            ).pack(fill="x", pady=4)

    # ---------- CONVERTER ----------
    def show_converter(self, category):
        self.clear()

        ttk.Button(
            self.container,
            text="← Indietro",
            command=self.show_home
        ).pack(anchor="w")

        ttk.Label(
            self.container,
            text=category,
            font=("Helvetica", 18, "bold")
        ).pack(pady=10)

        value_var = tk.StringVar()
        from_var = tk.StringVar()
        to_var = tk.StringVar()
        result_var = tk.StringVar(value="—")

        ttk.Entry(self.container, textvariable=value_var).pack(fill="x", pady=5)

        units = (
            ["°C", "°F", "K"]
            if category == "Temperatura"
            else list(CATEGORIES[category].keys())
        )

        from_box = ttk.Combobox(self.container, values=units, textvariable=from_var, state="readonly")
        to_box = ttk.Combobox(self.container, values=units, textvariable=to_var, state="readonly")

        from_box.pack(fill="x", pady=5)
        to_box.pack(fill="x", pady=5)

        def do_convert():
            try:
                value = float(value_var.get())
                f = from_var.get()
                t = to_var.get()

                if not f or not t:
                    raise ValueError

                if category == "Temperatura":
                    res = convert_temperature(value, f, t)
                else:
                    res = convert(value, f, t, CATEGORIES[category])

                result_var.set(f"{res:.6g}")
            except:
                messagebox.showerror("Errore", "Valori non validi")

        ttk.Button(self.container, text="Converti", command=do_convert).pack(pady=10)

        ttk.Label(
            self.container,
            textvariable=result_var,
            font=("Helvetica", 16, "bold")
        ).pack(pady=10)

    def clear(self):
        for w in self.container.winfo_children():
            w.destroy()


if __name__ == "__main__":
    ConvertitoreApp().mainloop()

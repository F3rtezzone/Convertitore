# unit_converter.py
"""
Modulo conversioni unità – completo e cross-platform
"""

# ---------- LUNGHEZZA ----------
LENGTH = {
    "mm": 1e-3,
    "cm": 1e-2,
    "m": 1.0,
    "km": 1e3,
    "in": 0.0254,
    "ft": 0.3048,
    "yd": 0.9144,
    "mi": 1609.344,
    "nmi": 1852
}

# ---------- MASSA ----------
MASS = {
    "mg": 1e-3,
    "g": 1.0,
    "kg": 1e3,
    "t": 1e6,
    "lb": 453.59237,
    "oz": 28.3495
}

# ---------- TEMPO ----------
TIME = {
    "s": 1.0,
    "min": 60,
    "h": 3600,
    "day": 86400
}

# ---------- AREA ----------
AREA = {
    "mm²": 1e-6,
    "cm²": 1e-4,
    "m²": 1.0,
    "km²": 1e6,
    "ha": 10000,
    "acre": 4046.8564224
}

# ---------- VOLUME ----------
VOLUME = {
    "ml": 1e-6,
    "l": 1e-3,
    "m³": 1.0,
    "gal": 0.00378541
}

# ---------- VELOCITÀ ----------
SPEED = {
    "m/s": 1.0,
    "km/h": 0.2777777778,
    "mph": 0.44704,
    "kt": 0.514444
}

# ---------- ENERGIA ----------
ENERGY = {
    "J": 1.0,
    "kJ": 1e3,
    "Wh": 3600,
    "kWh": 3.6e6,
    "cal": 4.184
}

# ---------- PRESSIONE ----------
PRESSURE = {
    "Pa": 1.0,
    "kPa": 1e3,
    "bar": 1e5,
    "atm": 101325,
    "psi": 6894.76
}

# ---------- DATI ----------
DATA = {
    "B": 1,
    "KB": 1024,
    "MB": 1024**2,
    "GB": 1024**3,
    "TB": 1024**4
}

# ---------- TEMPERATURA ----------
def convert_temperature(value, f, t):
    if f == t:
        return value
    if f == "°C":
        c = value
    elif f == "°F":
        c = (value - 32) * 5 / 9
    elif f == "K":
        c = value - 273.15
    else:
        raise ValueError("Unità non supportata")

    if t == "°C":
        return c
    if t == "°F":
        return c * 9 / 5 + 32
    if t == "K":
        return c + 273.15

    raise ValueError("Unità non supportata")


# ---------- GENERICO ----------
def convert(value, from_u, to_u, table):
    base = value * table[from_u]
    return base / table[to_u]


CATEGORIES = {
    "Lunghezza": LENGTH,
    "Massa": MASS,
    "Tempo": TIME,
    "Area": AREA,
    "Volume": VOLUME,
    "Velocità": SPEED,
    "Energia": ENERGY,
    "Pressione": PRESSURE,
    "Dati": DATA,
    "Temperatura": None
}

# unit_converter.py
"""
Modulo per conversione unità.
Include: Lunghezza, Massa, Potenza, Temperatura, Forza, Velocità
"""

# --- Fattori di conversione ---
LENGTH_FACTORS = {
    'm': 1.0, 'km': 1e3, 'cm': 1e-2, 'mm': 1e-3,
    'um': 1e-6, 'nm': 1e-9, 'nmi': 1852.0, 'mi': 1609.344,
    'ft': 0.3048, 'in': 0.0254
}

POWER_FACTORS = {
    'w': 1.0, 'kw': 1e3, 'mw': 1e6, 'hp': 745.699872
}

MASS_FACTORS = {
    'g': 1.0, 'kg': 1e3, 't': 1e6
}

TEMPERATURE_UNITS = {'c', 'f', 'k'}

FORCE_FACTORS = {
    'n': 1.0, 'kn': 1e3, 'lbf': 4.4482216152605, 'dyn': 1e-5
}

SPEED_FACTORS = {
    'mps': 1.0, 'kmh': 1000.0/3600.0, 'mph': 0.44704, 'kt': 0.5144444444444444
}

# --- Funzioni di conversione ---
def convert_length(value, from_u, to_u):
    return value * LENGTH_FACTORS[from_u] / LENGTH_FACTORS[to_u]

def convert_power(value, from_u, to_u):
    return value * POWER_FACTORS[from_u] / POWER_FACTORS[to_u]

def convert_mass(value, from_u, to_u):
    return value * MASS_FACTORS[from_u] / MASS_FACTORS[to_u]

def convert_temperature(value, from_u, to_u):
    f = from_u.lower()
    t = to_u.lower()
    if f == t:
        return value
    if f == 'c': c = value
    elif f == 'f': c = (value - 32) * 5/9
    elif f == 'k': c = value - 273.15
    else: raise ValueError('Unità temperatura non supportata')
    if t == 'c': return c
    if t == 'f': return c * 9/5 + 32
    if t == 'k': return c + 273.15
    raise ValueError('Unità temperatura non supportata')

def convert_force(value, from_u, to_u):
    return value * FORCE_FACTORS[from_u] / FORCE_FACTORS[to_u]

def convert_speed(value, from_u, to_u):
    return value * SPEED_FACTORS[from_u] / SPEED_FACTORS[to_u]

# --- Funzione generale ---
def parse_and_convert(category, value, from_u, to_u):
    value = float(value)
    category = category.lower()
    if category == "lunghezza":
        return convert_length(value, from_u, to_u)
    elif category == "massa":
        return convert_mass(value, from_u, to_u)
    elif category == "potenza":
        return convert_power(value, from_u, to_u)
    elif category == "temperatura":
        return convert_temperature(value, from_u, to_u)
    elif category == "forza":
        return convert_force(value, from_u, to_u)
    elif category == "velocità":
        return convert_speed(value, from_u, to_u)
    else:
        raise ValueError("Categoria non supportata")

# --- Liste unità per dropdown ---
def list_units(category):
    category = category.lower()
    if category == "lunghezza":
        return list(LENGTH_FACTORS.keys())
    elif category == "massa":
        return list(MASS_FACTORS.keys())
    elif category == "potenza":
        return list(POWER_FACTORS.keys())
    elif category == "temperatura":
        return list(TEMPERATURE_UNITS)
    elif category == "forza":
        return list(FORCE_FACTORS.keys())
    elif category == "velocità":
        return list(SPEED_FACTORS.keys())
    else:
        return []

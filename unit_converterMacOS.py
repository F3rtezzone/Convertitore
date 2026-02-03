# unit_converterMacOS.py
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
    meters = value * LENGTH_FACTORS[from_u]
    return meters / LENGTH_FACTORS[to_u]

def convert_power(value, from_u, to_u):
    watts = value * POWER_FACTORS[from_u]
    return watts / POWER_FACTORS[to_u]

def convert_mass(value, from_u, to_u):
    grams = value * MASS_FACTORS[from_u]
    return grams / MASS_FACTORS[to_u]

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
    newtons = value * FORCE_FACTORS[from_u]
    return newtons / FORCE_FACTORS[to_u]

def convert_speed(value, from_u, to_u):
    mps = value * SPEED_FACTORS[from_u]
    return mps / SPEED_FACTORS[to_u]

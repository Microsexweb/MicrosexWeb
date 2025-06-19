# Configuración base segura para UBC en entorno web
# Configuración inicial por defecto (no usar como estado compartido)
def get_config():
    return {
        "A": [0]*8,
        "B": [0]*8,
        "var_op": [[0]*8, [0]*8],
        "S": [0]*6,
        "intr": [[0]*8 for _ in range(4)],
        "R": [0]*8,
        "C": [0]*9,
        "val_h": ["00"]*2,
        "val_b": ["00000000"]*2,
        "val_d": ["0"]*2,
        "val_s": ["0"]*2
    }

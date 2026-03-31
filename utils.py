import os
import json

# ---------------------------------------------------
#               FUNCTION CLEAR SCREEN
def clear_screen(msg="Tecle ENTER para continuar..."):
    input(msg)
    os.system('cls' if os.name == 'nt' else 'clear')

# ----------------------------------------------------
#               FUNCTION NORMALIZED FORMART TEXT
def normalized_text(text):
    return text.strip().lower()

# ----------------------------------------------------
#               FUNCTION FOR DISPLAY TEXT
def display_text(text):
    return text.strip().capitalize()

# ----------------------------------------------------
                # FUNTION TO SAVE DATA

FILE_NAME = "database.json"

def save_data(data):
    """Guarda a lista de clientes num ficheiro JSON."""
    try:
        with open(FILE_NAME, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Erro ao salvar: {e}")

def load_data():
    """Lê os dados do ficheiro JSON. Se não existir, retorna lista vazia."""
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return []
# ---------------------------------------------------------
#           Created with AI Support: Generate unique IDs
# 

def get_next_appointment_id(customers_list):
    highest_id = 0
    for customer in customers_list:
        # Verifica se o cliente tem a chave 'schedule' e se ela não está vazia
        if 'schedule' in customer:
            for app in customer['schedule']:
                if app.get('appointment_id', 0) > highest_id:
                    highest_id = app['appointment_id']
    return highest_id + 1

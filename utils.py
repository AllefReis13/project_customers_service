import os
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
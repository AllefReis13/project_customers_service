from utils import clear_screen
from customers import function_menu_customer


while True:
    try:
        verificador = input("1- Clientes \n2- Agenda \n3- Financeiro \n4- Sair \nEscolha sua opção: ")
        verificador = int(verificador)
        if verificador == 1:
            clear_screen()
            function_menu_customer()
            
        elif verificador == 2:
            ...
        elif verificador == 3:
            ...
        elif verificador == 4:
            clear_screen(msg="Tecle ENTER para sair...")
            break
        else:
            print("Escolha opções validas...")
            clear_screen()

    except ValueError as v:
        print(f"ERROR --> {v}")
    except Exception as e:
        print(f"ERROR --> {e}")
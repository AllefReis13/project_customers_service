customers_list = []
from utils import clear_screen, display_text, normalized_text
# ---------------------------------------------------
#       FUNTION ADD CUSTOMER

def add_customers():
    name = normalized_text(input("Nome do cliente: "))
    phone = normalized_text(input("Telefone do cliente: "))
    street = normalized_text(input("Rua: "))
    street_2 = normalized_text(input("Referencia: "))
    city = normalized_text(input("Cidade: "))
    state = normalized_text(input("Estado: "))
    zip_code = normalized_text(input("Código postal: "))
    country = normalized_text(input("País: "))
    
    customer = {
        'name':name,
        'phone':phone,
        'addresses':[],
        'schedule':[],
    }
    address = {
        'street': street,
        'street_2': street_2,
        'city': city,
        'state':state,
        'zip_code':zip_code,
        'country':country,        
    }
    customer['addresses'].append(address)
    customers_list.append(customer)
    print(f'{name} foi adicionado com sucesso.')
    clear_screen(msg="Tecle ENTER para continuar")


# -----------------------------------------------
        # FUNCTION TO SEE ALL CUSTOMERS SIGNED UP

def all_customers():
    if not customers_list:
        print("No customers registered")
        
        clear_screen(msg="Tecle ENTER para voltar...")
        return

    for c in customers_list:
        print("-" * 30)
        print(f"Name: {c['name']}")
        print(f"Phone: {c['phone']}")
        print('\n')
        for adrss in c['addresses']:
            print(f"    Rua: {display_text(adrss['street'])}")
            print(f"    complemento: {display_text(adrss['street_2'])}")
            print(f"    Cidade: {display_text(adrss['city'])}")
            print(f"    Estado: {display_text(adrss['state'])}")
            print(f"    Código postal: {adrss['zip_code']}")
            print(f"    País: {display_text(adrss['country'])}")
            print('-' * 30)
    clear_screen(msg="Tecle ENTER para continuar...")
            

# -----------------------------------------------
#       FUNCTION MENU TO ACCESS ALL OF THE OTHERS FUNCTIONS ABOUT CUSTOMER
        
def function_menu_customer():
    while True:
        try:
            verify = input("1- Adicionar cliente \n2- Ver clientes \n3- Procurar cliente \n4- Sair \nEscolha sua opção: " )
            verify = int(verify)
            if verify == 1:
                add_customers()
            elif verify == 2:
                all_customers()
            elif verify == 3:
                ...
            elif verify == 4:
                clear_screen(msg="Tecle ENTER para volta ao menu anterior...")
                break
            else:
                print("Opção invalida...")
                clear_screen()
        except ValueError as v:
            print(f"ERROR --> {v}")
        except Exception as e:
            print(f"ERROR --> {e}")
            


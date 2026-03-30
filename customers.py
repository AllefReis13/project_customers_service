
from utils import clear_screen, display_text, normalized_text

customers_list = []
excluded_customer = []
next_id = 1
# ---------------------------------------------------
#       FUNTION ADD CUSTOMER

def add_customers():
    global next_id 
    name = normalized_text(input("Nome do cliente: "))
    phone = normalized_text(input("Telefone do cliente: "))
    street = normalized_text(input("Rua: "))
    street_2 = normalized_text(input("Referencia: "))
    city = normalized_text(input("Cidade: "))
    state = normalized_text(input("Estado: "))
    zip_code = normalized_text(input("Código postal: "))
    country = normalized_text(input("País: "))
    
    customer = {
        'id':next_id,
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
    next_id += 1



# -----------------------------------------------
        # FUNCTION TO SEE ALL CUSTOMERS SIGNED UP

def all_customers():
    if not customers_list:
        print("No customers registered.")        
        clear_screen(msg="Tecle ENTER para voltar...")
        return

    for c in customers_list:
        print("-" * 30)
        print(f"ID: {c['id']}")
        print(f"Name: {c['name']}")
        print(f"Phone: {c['phone']}")
        print()
        for addrss in c['addresses']:
            print(f"    Rua: {display_text(addrss['street'])}")
            print(f"    complemento: {display_text(addrss['street_2'])}")
            print(f"    Cidade: {display_text(addrss['city'])}")
            print(f"    Estado: {display_text(addrss['state'])}")
            print(f"    Código postal: {addrss['zip_code']}")
            print(f"    País: {display_text(addrss['country'])}")
            print('-' * 30)
    clear_screen(msg="Tecle ENTER para continuar...")

#  ----------------------------------------------------------------------
#       FUNCTION UPDATE CUSTOMERS
 

def update_customers():
    if not customers_list:
        print("No customers registered")
        clear_screen(msg="Tecle ENTER para voltar")
        return

    # Listagem para o utilizador ver quem atualizar
    # for cliente in customers_list:
    #     print("-" * 30)
    #     print(f"ID: {cliente['id']}")
    #     print(f"Nome: {display_text(cliente['name'])}")
    #     print(f"Telefone: {display_text(cliente['phone'])}")
    #     print()
    #     for addrss in cliente['addresses']:
    #         print(f"    Rua: {display_text(addrss['street'])}")
    #         print(f"    Complemento: {display_text(addrss['street_2'])}")
    #         print(f"    Cidade: {display_text(addrss['city'])}")
    #         print(f"    Estado: {display_text(addrss['state'])}")
    #         print(f"    Código postal: {addrss['zip_code']}")
    #         print(f"    País: {display_text(addrss['country'])}")
    #         print("-" * 30)
    print("Procure o ID do cliente que você quer para que possa fazer mudanças:")
    all_customers()

    while True:
        try:
            verify = input("\n1- Update name \n2- Update phone \n3- Update Address \n4- Leave \nEscolha sua opção: ")
            verify = int(verify)

            if verify == 4:
                clear_screen(msg="Voltando ao menu anterior...")
                break

            if verify in [1, 2, 3]:
                id_procurado = int(input("Digite o ID do cliente que deseja atualizar: "))
                cliente_alvo = None

                # BUSCA O CLIENTE PELO ID
                for c in customers_list:
                    if c['id'] == id_procurado:
                        cliente_alvo = c
                        break

                if not cliente_alvo:
                    print("Erro: ID de cliente não encontrado.")
                    clear_screen()
                    continue

                # Ações baseadas na escolha (usando cliente_alvo)
                if verify == 1:
                    new_name = input("New name: ")
                    cliente_alvo['name'] = normalized_text(new_name)
                    print(f"Done, name updated.")
                
                elif verify == 2:
                    new_phone = input("New phone number: ")
                    cliente_alvo['phone'] = normalized_text(new_phone)
                    print("Done, phone updated.")
                
                elif verify == 3:
                    new_street = input("Nova rua: ")
                    new_street_2 = input("Complemento: ")
                    new_city = input("Nova cidade: ")
                    new_state = input("Novo estado: ")
                    new_zip_code = input("Novo código postal: ")
                    new_country = input("País: ")
                    
                    new_address = {
                        'street': new_street,
                        'street_2': new_street_2,
                        'city': new_city,
                        'state': new_state,
                        'zip_code': new_zip_code,
                        'country': new_country
                    }

                    if not cliente_alvo['addresses']:
                        cliente_alvo['addresses'].append(new_address)
                    else:
                        cliente_alvo['addresses'][0] = new_address
                    print("Address updated.")

                clear_screen()
            else:
                print("Choose a valid option.")
                clear_screen()

        except ValueError:
            print("ERROR --> Por favor, digite um número válido.")
        except Exception as e:
            print(f"ERROR --> {e}")

    

# -----------------------------------------------------------------------
#       FUNTION DELETE_CUSTOMERS
def delete_customers():
    for c in customers_list:
        print(f"ID: {c['id']}")
        print(f"{c['name']}")
        print("=" * 30)
    try:
        verify = int(input("Digite o ID do cliente a ser excluido: "))
    except ValueError:
        print("Digite um número válido.")
        return
    for c in customers_list:
        if c['id'] == verify:
            customers_list.remove(c)
            print(f"Cliente {c['name']} removido com sucesso!")
            excluded_customer.append(c)
            print(f"o cliente {c['name']} foi adicionado numa lista, para que caso ele volte a necessitar de nossos serviços.")            
            return
    print("ID")

    


# -----------------------------------------------------------------------
#       FUNCTION MENU TO ACCESS ALL OF THE OTHERS FUNCTIONS ABOUT CUSTOMER
        
def function_menu_customer():
    while True:
        try:
            verify = input("1- Adicionar cliente \n2- Ver clientes \n3- Atualizar cliente \n4- Excluir cliente \n5- Sair \nEscolha sua opção: " )
            verify = int(verify)
            if verify == 1:
                add_customers()
            elif verify == 2:
                all_customers()
            elif verify == 3:
                update_customers()
            elif verify == 4:
                delete_customers()
            elif verify == 5:
                clear_screen(msg="Tecle ENTER para volta ao menu anterior...")
                break
            else:
                print("Opção invalida...")
                clear_screen()
        except ValueError as v:
            print(f"ERROR --> {v}")
        except Exception as e:
            print(f"ERROR --> {e}")
            


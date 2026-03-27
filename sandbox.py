    # if not customers_list:
    #     print("No customers registered")
    #     clear_screen(msg="Tecle ENTER para voltar")
    #     return
    # for i, cliente in enumerate(customers_list):
    #     print("-" * 30)
    #     print(f"        Índice {i}")
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

    # while True:
    #     try:
    #         verify = input("1-Update name \n2- Update phone \n3- update Address \n4- Leave \nEscolha sua opção: ")
    #         verify =  int(verify)

    #         if verify == 1:
    #             try:
    #                 index_customer = input("Digite o índice do cliente para atualizar o nome: ")
    #                 index_customer = int(index_customer)

    #                 if 0 <=index_customer < len(customers_list):
    #                     new_name = input(" New name: ")
    #                     customers_list[index_customer]['name'] = new_name
    #                     print(f"Done, customer updated.")
    #                 else:
    #                     print("Erro: Invalid index")
    #                 clear_screen()

    #             except IndexError as ind:
    #                 print(f"ERROR --> {ind}")
    #             except ValueError as v:
    #                 print(f"ERROR --> {v}")
    #             except Exception as e:
    #                 print(f"ERROR --> {e}")
    #         elif verify == 2:
    #             try:
    #                 index_customer = input("Digite o índice do cliente para atualizar telefone: ")
    #                 index_customer = int(index_customer)
    #                 if 0 <= index_customer < len(customers_list):
    #                     new_phone = input("Digite o novo número de telefone: ")
    #                     customers_list[index_customer]['phone'] = new_phone
    #                     print("Done, customer updated")
    #                 else:
    #                     clear_screen(msg="Invalid index")
    #                 clear_screen()

    #             except IndexError as ind:
    #                 print(f"ERROR --> {ind}")
    #             except ValueError as v:
    #                 print(f"ERROR --> {v}")
    #             except Exception as e:
    #                 print(f"ERROR --> {e}")
                    
    #         elif verify == 3:
    #                 try:
    #                     index_customer = input("Digite o indice do cliente para atualizar o endereço: ")
    #                     index_customer = int(index_customer)
    #                     if 0 <= index_customer < len(customers_list):
    #                         new_street = input("Digite a nova rua: ")
    #                         new_street_2 = input("Digite o complemento: ")
    #                         new_city = input("Digite a nova cidade: ")
    #                         new_state = input("Digite o novo estado: ")
    #                         new_zip_code = input("Digite o novo código postal: ")
    #                         new_country = input("Digite o País: ")
    #                         new_address = {
    #                             'street': new_street,
    #                             'street_2': new_street_2,
    #                             'city': new_city,
    #                             'state': new_state,
    #                             'zip_code': new_zip_code,
    #                             'country': new_country
    #                         }
                        
                            

    #                         if not customers_list[index_customer]['addresses']:
    #                             customers_list[index_customer]['addresses'].append(new_address)
    #                             print("Address updated")
    #                         else:
    #                             customers_list[index_customer]['addresses'][0] = new_address
    #                             print("Address updated")
    #                     else:
    #                         clear_screen(msg="Invalid index")  
    #                     clear_screen()

    #                 except IndexError as ind:
    #                     print(f"ERROR --> {ind}")
    #                 except ValueError as v:
    #                     print(f"ERROR --> {v}")
    #                 except Exception as e:
    #                     print(f"ERROR --> {e}")                   
               
    #         elif verify == 4:
    #             clear_screen(msg="Voltando ao menu anterior...")
    #             break
    #         else:
    #             clear_screen(msg="Choose a valid option")                

    #     except IndexError as ind:
    #         print(f"ERROR --> {ind}")
    #     except ValueError as v:
    #         print(f"ERROR --> {v}")
    #     except Exception as e:
    #         print(f"ERROR --> {e}")
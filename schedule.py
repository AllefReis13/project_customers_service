from utils import clear_screen, normalized_text, display_text, save_data, get_next_appointment_id
from customers import customers_list


appointment_id = get_next_appointment_id(customers_list)
all_appointment = []


# -------------------------------------------------------------------------------------------------------
#           FUNCTION TO CREATE CUSTOMER'S SCHEDULE
def create_schedule():
    global appointment_id
    
    while True:
        try:
            verify = input("1- Ver clientes \n2- Selecionar clientes \n3- Voltar \nSelecione sua opção: ")
            verify = int(verify)

            if verify == 1:
                for customer in customers_list:
                    print("=" * 30)
                    print(f"ID: {(customer['id'])}")
                    print(f"Nome: {display_text(customer['name'])}")
                    for addrss in customer['addresses']:
                        print(f"Address: {display_text(addrss['street'])}")
                        print(f"Address Landpark: {display_text(addrss['street_2'])}")
                        print(f"city: {display_text(addrss['city'])}")
                    print("=" * 30)
                clear_screen(msg="Pegue o ID desejado e prossida...")
            elif verify == 2:
                try:

                    
                    selected_id = input("Digite o ID do cliente que deseja agendar: ")
                    selected_id = int(selected_id)

                    found = False
                    
                    for c in customers_list:
                        if c['id'] == selected_id:
                            date = normalized_text(input("Digite a data do serviço: "))
                            time = normalized_text(input("Digite a hora do serviço: "))
                            description = normalized_text(input("Digite uma breve descrição do serviço: "))
                            status = normalized_text(input("Digite o status do serviço [PENDENTE, CONCLUIDO, PAGO]: "))

                            

                            while True: 
                                try:
                                    define_price = normalized_text(input("1- Calculo por hora \n2- Calculo de valor fixo \nEscolha sua opção: "))
                                    define_price = int(define_price)
                                    if define_price == 1: 

                                        value_hour = float(input("Valor da hora: "))
                                        many_hours = float(input("Quantidade de horas: "))
                                        final_price = value_hour * many_hours
                                        break

                                    elif define_price == 2:

                                        final_price = float(input("Digite o valor do serviço: "))
                                        break

                                    else:
                                        print("Opção invalida...")
                                except ValueError as v:
                                    print(f"ERROR --> {v}")
                                except Exception as e:
                                    print(f"ERROR --> {e}")


                            schedule = {

                                'customer_id': selected_id,
                                'appointment_id': appointment_id,
                                'name':c['name'],
                                'phone':c['phone'],
                                'date': date,
                                'time':time,
                                'description': description,
                                'price': final_price,
                                'status':status
                            }
                            
                            found = True
                            c['schedule'].append(schedule)
                            save_data(customers_list)
                            all_appointment.append(schedule)
                            appointment_id = get_next_appointment_id(customers_list)
                            print("Agendamento realizado...")
                            print(f"    ID do serviço: {schedule['appointment_id']}")
                            print(f"    Nome: {schedule['name']}")
                            print(f"    Data: {schedule['date']}")
                            print(f"    Hora: {schedule['time']}")
                            print(f"    Descrição: {schedule['description']}")
                            print(f"    preço: €: {schedule['price']}")
                            print(f"    Status: {schedule['status']}")
                            print("=" * 30)

                            clear_screen()
                            break                
                        
                    if not found:
                        print("ID não encontrado. Chame a função novamente...")
                        clear_screen()
                
                except ValueError as v:
                    print(f"ERROr --> {v}")
                except Exception as e:
                    print(f"ERROR --> {e}") 
            elif verify == 3:
                clear_screen(msg="Tecle ENTER para voltar...")
                break
                          
        except ValueError as v:
            print(f"ERROr --> {v}")
        except Exception as e:
            print(f"ERROR --> {e}")   

def all_schedule():
    if not customers_list:
        print("não há clientes na lista.")
        return
    for c in customers_list:
        print(f"ID: {c['id']}")
        print(f"Nome: {c['name']}")
        print('=' * 30)
        print(f"")
        if not c['schedule']:
            print("Sem agendamentos registrados.")
        else:    
            for add in c['schedule']:
                print(f"=" * 30)
                print(f"    ID do serviço: {add['appointment_id']}")
                print(f"    Data: {add['date']}")
                print(f"    Hora: {add['time']}")
                print(f"    Descrição: {add['description']}")
                print(f"    Preço: {add['price']}")
                print(f"    Status: {add['status']}")
                print("=" * 30)

                
    clear_screen(msg="Tecle ENTER para voltar ao menu anterior...")

def menu_schedule():
    while True: 
        try: 
            verify = input("1- Criar agendamento \n2- Ver agendamento \n3- Editar Agendamento \n4- Deletar agendamento \n5- Sair \nEscolha sua opção: ")
            verify = int(verify)

            if verify == 1:
                create_schedule()
            elif verify == 2:
                all_schedule()
            elif verify == 3:
                ...
            elif verify == 4:
                ...
            elif verify == 5:
                clear_screen(msg="Tecle ENTER para voltar ao menu principal...")
                break
            else:
                clear_screen(msg="Selecione opções validas...")

        except ValueError as v:
            print(f"ERROR --> {v}")
        except Exception as e:
            print(f"ERROR --> {e}") 
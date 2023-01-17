from eventos import (cria_evento,
                     imprime_lista_de_eventos,
                     nome_ficheiro_lista_de_eventos
                     )
from io_ficheiros import (
    guarda_em_ficheiro,
    le_de_ficheiro
)
from io_terminal import (
    imprime_lista_de_dicionarios
)


def menu():
    """ main menu da aplicação"""

    lista_de_eventos = []

    while True:
        print("""
        *********************************************************************
        :       myTicketPT - Bilheteira de eventos                          : 
        *********************************************************************
        :                                                                   :
        : ne - novo evento          le - listar eventos                     :
        :                                                                   :
        : g - guarda tudo           c - carrega tudo                        :
        :                                                                   :
        : x - sair                                                          :
        :                                                                   :
        *********************************************************************
        """)

        op = input("Opção? ").lower()

        if op == "x":
            exit()
        elif op == "ne":
            nova_evento = cria_evento()
            lista_de_eventos.append(nova_evento)
        elif op == "le":
            imprime_lista_de_eventos(lista_de_eventos)
        elif op == "g":
            guarda_as_listas_em_ficheiros(lista_de_eventos)
        elif op == "c":
            lista_de_eventos = carrega_as_listas_dos_ficheiros()

def pergunta_id(questao, lista):
    imprime_lista_de_dicionarios(lista)
    while True:
        idx = int(input(questao))
        if 0 <= idx < len(lista):
            return idx
        else:
            print(f"id inexistente. Tente de novo. Valores admitidos {0} - {len(lista)}")


def carrega_as_listas_dos_ficheiros():
    """ ...todo... """

    lista_de_evento = le_de_ficheiro(nome_ficheiro_lista_de_eventos)
    return lista_de_evento


def guarda_as_listas_em_ficheiros(lista_de_evento):
    """ ... todo ....
    :param lista_de_evento:
    :return:
    """

    op = input("Os dados nos ficheiros serão sobrepostos. Continuar (S/n)?")
    if op in ['s', 'S', '']:
        guarda_em_ficheiro(nome_ficheiro_lista_de_eventos, lista_de_evento)
    else:
        print("Cancelada.")


if __name__ == "__main__":
    menu()


def pagamento(metodos):
    metodos = ['MasterCard', 'Visa', 'Paypal',
               'MBway', 'Transferencia bancaria']
    print(metodos)

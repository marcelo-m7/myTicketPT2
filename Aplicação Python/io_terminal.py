from tabulate import tabulate


def imprime_lista(cabecalho, lista):

    cabecalho = f":::::::::::::::::: {cabecalho} ::::::::::::::::::"
    comprimento_cabecalho = len(cabecalho)

    print(cabecalho)
    imprime_lista_de_dicionarios(lista)
    print(comprimento_cabecalho * ":")


def imprime_lista_de_dicionarios(lista):

    if len(lista) > 0:
        # cabecalho da tabela
        lista_a_imprimir = [["id"] + list(lista[0].keys())]
        # dados
        lista_a_imprimir.extend([[id] + list(d.values()) for id, d in enumerate(lista)])

        print(tabulate(lista_a_imprimir, headers="firstrow"))
    else:
        print("lista vazia")

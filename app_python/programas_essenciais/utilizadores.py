"""
Funções de utilizadores

:Date: 1 Jan 2023
:Version: 0.1
:Authors: Gonçalo Gomes, Ricardo Policarpo, Marcelo Santos
"""


from io_terminal import imprime_lista

nome_ficheiro_lista_de_utilizadores = "lista_de_utilizadores.pk"


def cria_novo_utilizador():  # criação de utilizador na app
    """ pede os dados de um novo utilizador

    :return: dicionario com o novo utilizador na forma
        "nome": <<nome>>, "email": <<email>>
    """
    # todo
    pass


# def para ver todos os utilizadores disponiveis na app
def imprime_lista_de_utilizadores(lista_de_utilizadores):
    """ ..."""

    imprime_lista(cabecalho="Lista de Utilizadores",
                  lista=lista_de_utilizadores)

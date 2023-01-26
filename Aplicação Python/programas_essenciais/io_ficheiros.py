"""
Funções de i/o de ficheiros

:Date: 1 Jan 2023
:Version: 0.1
:Authors: Gonçalo Gomes, Ricardo Policarpo, Marcelo Santos
"""

import pickle


def le_de_ficheiro(nome_ficheiro):
    """ Lê os dados de um ficheiro

    :param nome_ficheiro: nome do ficheiro onde estao os dados
    :return: o que leu do ficheiro (depende dos dados guardados)
    """

    with open(nome_ficheiro, "rb") as f:
        return pickle.load(f)


def guarda_em_ficheiro(nome_do_ficheiro, dados):
    """ Guardar os dados num ficheiro

    :param nome_do_ficheiro: nome do ficheiro onde vai guardar os dados
    :param dados: dados a serem guardados
    """

    with open(nome_do_ficheiro, "wb") as f:
        pickle.dump(dados, f)

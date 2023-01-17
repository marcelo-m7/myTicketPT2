import pickle


def le_de_ficheiro(nome_ficheiro):

    with open(nome_ficheiro, "rb") as f:
        return pickle.load(f)


def guarda_em_ficheiro(nome_do_ficheiro, dados):
    with open(nome_do_ficheiro, "wb") as f:
        pickle.dump(dados, f)

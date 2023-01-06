from io_terminal import imprime_lista

nome_ficheiro_lista_de_eventos = "lista_de_eventos.pk"


def cria_evento():
    nome_evento = input("Nome do evento ")
    artista = input("Artista ")
    sala = input("Sala ").upper()
    pvp = float(input("PVP do bilhete "))
    data_inicio = input("Data de início (DD-MM-AAA)? ")

    return {"Artista ": artista, "Sala ": sala, "Nome do evento: ": nome_evento, "Data do evento": data_inicio, "PVP do bilhete": pvp}


def imprime_lista_de_eventos(lista_de_eventos):
    imprime_lista(cabecalho="Lista de Eventos", lista=lista_de_eventos)
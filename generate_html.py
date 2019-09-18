from random import choice
from glob import glob


def create_html(qtd):

    files = glob('bases*')[0]
    # Abertura dos arquivos
    name_1 = open(files+"/nome.txt")
    name_2 = open(files+"/sobrenome.txt")
    name_3 = open(files+"/terceiro nome.txt")
    street = open(files+"/ruas e avenidas.txt")
    street_n = open(files+"/numeros de ruas.txt")
    phone = open(files+"/telefones.txt")
    country = open(files+"/Países.txt")
    city = open(files+"/cidades.txt")
    cep = open(files+"/cep.txt")
    state = open(files+"/UF.txt")

    file_lines = [cep.readlines(), city.readlines(),
                  name_1.readlines(), street_n.readlines(),
                  country.readlines(), street.readlines(),
                  name_2.readlines(), phone.readlines(),
                  name_3.readlines(), state.readlines()]

    # Fechamento dos arquivos
    name_1.close()
    name_2.close()
    name_3.close()
    state.close()
    cep.close()
    city.close()
    country.close()
    phone.close()
    street.close()
    street_n.close()

    data = {}
    more_data = []
    for i in range(qtd):
        d = []
        d = ["\t<dt>Address</dt>\n",
             "\t\t<dd>" +
             choice(file_lines[5]).strip("\n") +
             ', ' +
             choice(file_lines[3]).strip("\n") + "</dd>\n",
             "\t<dt>Phone</dt>\n",
             "\t\t<dd>" + choice(file_lines[7]).strip("\n") + "</dd>\n",
             "\t<dt>Country</dt>\n",
             "\t\t<dd>" + choice(file_lines[4]).strip("\n") + "</dd>\n",
             "\t<dt>City</dt>\n",
             "\t\t<dd>" + choice(file_lines[1]).strip("\n") + "</dd>\n",
             "\t<dt>CEP</dt>\n",
             "\t\t<dd>" + choice(file_lines[0]).strip("\n") + "</dd>\n",
             "\t<dt>UF</dt>\n",
             "\t\t<dd>" + choice(file_lines[9]).strip("\n") + "</dd>\n",
             "</dl>\n"]
        more_data.append(''.join(d))

    yield "<!doctype html>\n"
    yield "<html lang=\"en\">\n"
    yield "<head>\n"
    yield "<title>Generate Data</title>\n"
    yield "</head>\n"
    # Atribuindo os dados a um dicionario
    # Nome completo como key pra garantir a nao repeticao de nomes
    i = 0
    while len(data.keys()) < qtd:
        name = ' '.join(["<dl>\n\t<dt>Name</dt>\n\t\t<dd>" +
                         choice(file_lines[2]).strip("\n"),
                         choice(file_lines[6]).strip("\n"),
                         choice(file_lines[8]).strip("\n") +
                         "</dd>\n"])
        # Impede que o indice da lista ultrapasse o do dicionario
        if name not in data:
            data[name] = more_data[i]
            i += 1
            row = [name, data[name]]
            yield ''.join(row)

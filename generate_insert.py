from random import choice
from glob import glob


def create_insert_sql(qtd):

    INSERT_STATEMENT = ["INSERT\nINTO\n\tPERSON\n",
                        "\t(Name,Address,Phone,",
                        "Country,City,CEP,UF)\nVALUES\n\t("]
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
        more_data.append('","'.join([choice(file_lines[5]).strip("\n") +
                                     ', ' +
                                     choice(file_lines[3]).strip("\n"),
                                     choice(file_lines[7]).strip("\n"),
                                     choice(file_lines[4]).strip("\n"),
                                     choice(file_lines[1]).strip("\n"),
                                     choice(file_lines[0]).strip("\n"),
                                     choice(file_lines[9]).strip("\n")]))

    # Atribuindo os dados a um dicionario
    # Nome completo como key pra garantir a nao repeticao de nomes
    i = 0
    while len(data.keys()) < qtd:
        name = ' '.join([choice(file_lines[2]).strip("\n"),
                         choice(file_lines[6]).strip("\n"),
                         choice(file_lines[8]).strip("\n")])
        # Impede que o indice da lista ultrapasse o do dicionario
        if name not in data:
            data[name] = more_data[i]
            i += 1
            row = [''.join(INSERT_STATEMENT), '"' + name + '","',
                   data[name], '");\n']
            yield ''.join(row)

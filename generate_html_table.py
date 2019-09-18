from random import choice
from glob import glob

columns = ['Nome', 'Rua/Avenida', 'Num da Rua', 'Telefone',
           'Pais', 'Cidade', 'CEP', 'UF']

def create_html_table(qtd):

    files = glob('bases*')[0]
    # Abertura dos arquivos
    name_1 = open(files+"/nome.txt")
    name_2 = open(files+"/sobrenome.txt")
    name_3 = open(files+"/terceiro nome.txt")
    street = open(files+"/ruas e avenidas.txt")
    street_n = open(files+"/numeros de ruas.txt")
    phone = open(files+"/telefones.txt")
    country = open(files+"/Paises.txt")
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
    while(len(data) < qtd):
        key = "{} {} {}".format(choice(file_lines[2]).strip("\n"), 
                                choice(file_lines[6]).strip("\n"), 
                                choice(file_lines[8]).strip("\n"))
        data[key] = '''<tr>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
            </tr>'''.format(key, choice(file_lines[5]).strip("\n"),
                       choice(file_lines[3]).strip("\n"), choice(file_lines[7]).strip("\n"),
                       choice(file_lines[4]).strip("\n"), choice(file_lines[1]).strip("\n"),
                       choice(file_lines[0]).strip("\n"), choice(file_lines[9]).strip("\n"))
    yield '''
        <!DOCTYPE html>
        <html lang="pt-br">
  <head>
    <title>Tabela de dados</title>
    <meta charset="utf-8">
  </head>
  <body>
    '''

    yield '''<table>
        <tr>
            <th>{}</th>
            <th>{}</th>
            <th>{}</th>
            <th>{}</th>
            <th>{}</th>
            <th>{}</th>
            <th>{}</th>
            <th>{}</th>
        </tr>'''.format(columns[0], columns[1],
            columns[2], columns[3],
            columns[4], columns[5],
            columns[6], columns[7])
    for key in data.keys():
        yield data[key]
    yield '</table>'
    yield '''</body>
            </html>'''
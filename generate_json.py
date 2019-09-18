from glob import glob
from random import choice


def create_json(number_of_lines):
    arq = glob('bases*')[0]
    first_name = open(arq+"/nome.txt").readlines()
    second_name = open(arq+"/sobrenome.txt").readlines()
    third_name = open(arq+"/terceiro nome.txt").readlines()
    street_name = open(arq+"/ruas e avenidas.txt").readlines()
    street_number = open(arq+"/numeros de ruas.txt").readlines()
    phone_numer = open(arq+"/telefones.txt").readlines()
    country = open(arq+"/Paises.txt").readlines()
    city = open(arq+"/cidades.txt").readlines()
    cep = open(arq+"/cep.txt").readlines()
    state = open(arq+"/UF.txt").readlines()
    json_dic = {}
    cols = ['"name",', '"address",', '"phone",', '"country",',
            '"city",', '"cep", ', '"state"']

    while len(json_dic) < number_of_lines:
        name1 = choice(first_name).strip("\n")
        name2 = choice(second_name).strip("\n")
        name3 = choice(third_name).strip("\n")
        full_name = '"' + name1 + ' ' + name2 + ' ' + name3 + '"'
        elements = []
        elements.append(
                        (choice(street_name).strip("\n") + ", ") +
                        (choice(street_number).strip("\n")))
        elements.append(choice(phone_numer).strip("\n"))
        elements.append(choice(country).strip("\n"))
        elements.append(choice(city).strip("\n"))
        elements.append(choice(cep).strip("\n"))
        elements.append(choice(state).strip("\n"))
        json_dic[full_name] = elements
    x = 0
    yield "{"
    yield '     "cols": ['
    for _ in cols:
        yield ('        %s' % _)
    yield '     ],'
    yield '     "data": ['
    for key in json_dic.keys():
        x += 1
        yield "         ["
        yield ('            %s,' % key)
        for i in range(len(json_dic[key])):
            if i == (len(json_dic[key])-1):
                yield ('            "%s"' % json_dic[key][i])
            else:
                yield ('            "%s",' % json_dic[key][i])
        if x == len(json_dic):
            yield '         ]'    
        else:
            yield '         ],'
    yield '     ]'
    yield '}'

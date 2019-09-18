from glob import glob
import random


# lista com o nome das colunas
columns = ['Nome', 'Rua/Avenida', 'Num da Rua', 'Telefone',
           'Pais', 'Cidade', 'CEP', 'UF']


def create_csv(
                number_of_lines,  # Numero de linhas do csv
                sep=','  # Separacao do csv
               ):
    arquives = glob('bases*')[0]  # Pegando nome da pasta com arquivos
    # Abrindo todos os txt de dados
    first_name = open(arquives+"/nome.txt").readlines()
    second_name = open(arquives+"/sobrenome.txt").readlines()
    third_name = open(arquives+"/terceiro nome.txt").readlines()
    street_name = open(arquives+"/ruas e avenidas.txt").readlines()
    street_number = open(arquives+"/numeros de ruas.txt").readlines()
    phone_number = open(arquives+"/telefones.txt").readlines()
    country = open(arquives+"/Paises.txt").readlines()
    city = open(arquives+"/cidades.txt").readlines()
    cep = open(arquives+"/cep.txt").readlines()
    state = open(arquives+"/UF.txt").readlines()
    csv_lines = {}  # Dicionario que ira conter as linhas
    while(len(csv_lines) < number_of_lines):
        # Criando a chave que e o nome da pessoa
        person_name = "{} {} {}".format(random.choice(first_name).strip("\n"),
                                        random.choice(second_name).strip("\n"),
                                        random.choice(third_name).strip("\n"))
        # Lista que ira conter os elementos
        elements_of_line = []
        # Pegando nome de rua
        elements_of_line.append(random.choice(street_name).strip("\n"))
        # Pegando numero de rua
        elements_of_line.append(random.choice(street_number).strip("\n"))
        # Pegando numero de telefone
        elements_of_line.append(random.choice(phone_number).strip("\n"))
        # Pegando pais
        elements_of_line.append(random.choice(country).strip("\n"))
        # Pegando cidade
        elements_of_line.append(random.choice(city).strip("\n"))
        # Pegando cep
        elements_of_line.append(random.choice(cep).strip("\n"))
        # Pegando estado
        elements_of_line.append(random.choice(state).strip("\n"))
        # Adicionando as informacoes na pessoa
        csv_lines[person_name] = elements_of_line
        line = ''  # Ajudante para criar linhas
    for colun in columns:
        if colun != columns[-1]:
            line += colun+sep
        else:
            line += colun
    yield line
    for key in csv_lines.keys():
        line = key+','
        size_of_line = len(csv_lines[key])
        for i in range(size_of_line):
            if i < size_of_line-1:
                line += csv_lines[key][i] + sep
            else:
                line += csv_lines[key][i]
        yield line

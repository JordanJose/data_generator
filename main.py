import sys
from generate_csv import create_csv
from generate_insert import create_insert_sql
from generate_json import create_json
from generate_html import create_html
from generate_html_table import create_html_table

if sys.argv[2] == '-csv':
    registers = int(sys.argv[1])
    for line in create_csv(registers):
        print(line)

elif sys.argv[2] == '-insert':
    registers = int(sys.argv[1])
    for line in create_insert_sql(registers):
        print(line)

elif sys.argv[2] == '-json':
    registers = int(sys.argv[1])
    for line in create_json(registers):
        print(line)

elif sys.argv[2] == '-html':
    registers = int(sys.argv[1])
    for line in create_html(registers):
        print(line)
elif sys.argv[2] == '-html_table':
    registers = int(sys.argv[1])
    for line in create_html_table(registers):
        print(line)
else:
    print("Error")

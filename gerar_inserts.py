import csv

with open(r'c:\temp\unidades.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    linhas = list()
    for row in csv_reader:
        linhas.append(f"INSERT INTO licenciamento.unidade_medida (id, sigla, nome) VALUES(nextval('licenciamento.unidade_medida_id_seq'),'{row[0]}','{row[1]}');")
        line_count += 1
    print(f'Foram processadas {line_count} linhas.')

    with open(r'c:\temp\unidades.sql', 'a',encoding="utf8") as arquivo:
        for i in linhas:
            arquivo.write(i + '\n')

        arquivo.close()
        



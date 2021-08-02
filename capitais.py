from random import *

capitais_dict = {
    "Acre (AC)" : "Rio Branco",
    "Amapá (AP)" : "Macapá",
    "Amazonas (AM)" : "Manaus",
    "Pará (PA)" : "Belém",
    "Rondônia (RO)": "Porto Velho",
    "Roraima (RR)" : "Boa Vista",
    "Tocantins (TO)" : "Palmas",
    "Alagoas (AL)" : "Maceió",
    "Bahia (BA)" : "Salvador",
    "Ceará (CE)" : "Fortaleza",
    "Maranhão (MA)" : "São Luís",
    "Paraíba (PB)" : "João Pessoa",
    "Pernambuco (PE)" : "Recife",
    "Piauí (PI)" : "Teresina",
    "Rio Grande do Norte (RN)" : "Natal",
    "Sergipe (SE)" : "Aracaju",
    "Distrito Federal (DF)" : "Brasília",
    "Goiás (GO)" : "Goiânia",
    "Mato Grosso (MT)" : "Cuiabá",
    "Mato Grosso do Sul (MS)":"Campo Grande",
    "Espírito Santo (ES)" : "Vitória",
    "Minas Gerais (MG)": "Belo Horizonte",
    "Rio de Janeiro (RJ)":"Rio de Janeiro",
    "São Paulo (SP)":"São Paulo",
    "Paraná (PR)":"Curitiba",
    "Santa Catarina (SC)":"Florianópolis",
    "Rio Grande do Sul (RS)":"Porto Alegre",
    }

lista_estados = [key for key in capitais_dict]

estado = choice(lista_estados)
capital = capitais_dict[estado]

while(True):
    capital_ins = input(f'Para o estado {estado}, informe a capital:')
    if capital.upper() == capital_ins.upper():
        print("resposta correta")
        break
    elif capital_ins.upper() == 'EXIT':
        print("adeus")
        break
    else:
        print("resposta incorreta")

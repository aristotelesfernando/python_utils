estados = {
	'Para': {
		'capital':'Belem',
		'prato':'maniçoba'
		},
	'Amazonas': {
		'capital':'Manaus',
		'prato':'peixe frito'
		},
	'Rio de Janeiro': {
		'capital':'Rio de Janeiro',
		'prato':'feijoada'
		},
	'São Paulo': {
		'capital':'São Paulo',
		'prato':'pizza'
		}
	}

for estado, estado_info in estados.items():
    print(f"O estado selecionado é o {estado}")
    capital = estado_info['capital']
    prato = estado_info['prato']
    print(f"\tA capital é {capital} e o prato típico é o {prato}")
    print('-'*25)

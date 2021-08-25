import easyocr as er

leitor = er.Reader(['pt'])

resultados = leitor.readtext('imagem.jpg', paragraph = False)

for res in resultados:
    print(f'{res[1]}\n')

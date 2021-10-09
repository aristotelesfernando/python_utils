import base64

imagem_path = input('Informe o path da imagem completo...:')

with open(imagem_path, "rb") as arquivo_imagem:
    texto_base64 = base64.b64encode(arquivo_imagem.read())

print('Saida em Base64')
print(f'Arquivo: {imagem_path}');

arquivo = open(imagem_path[:-4]+".txt", 'w')
arquivo.writelines(str(texto_base64))
arquivo.close()

print(f'Arquivo base64: {imagem_path[:-4]}.txt');

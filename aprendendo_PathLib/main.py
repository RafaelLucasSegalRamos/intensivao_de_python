from pathlib import Path
from time import sleep

caminho = Path()

teste = caminho / "files" / "teste.html"

absoluto = caminho.absolute()
print(absoluto)
print(teste.stem)

print(teste.suffix) # Se o arquivo tiver mais de uma extensão, utilize o .suffixes
print(absoluto.root)
print(absoluto.parent)

print(absoluto.parts)

print(teste.absolute())

teste.touch()  # Cria o arquivo caso não exista

# sleep(10)

# teste.unlink()  # Deleta o arquivo

pasta_0 = caminho / "files" / "pasta_0"
arquivo_0 = pasta_0 / "arquivo_0.txt"
p = Path("files/").glob("*")
lista = list(p)

if not pasta_0.exists():
    pasta_0.mkdir()
    # Para remover a pasta, utilize o rmdir()
arquivo_0.touch()

print(arquivo_0.exists())
print(arquivo_0.is_file())
if arquivo_0.exists() and arquivo_0.is_file():
    arquivo_0.write_text("Olá mundo!")

    print(arquivo_0.read_text())

print(lista)
for i in lista:
    print(i)
# Para renomear um arquivo, utilize o .rename()

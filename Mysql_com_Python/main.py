import mysql.connector
from time import sleep

connection = mysql.connector.connect(host="localhost", user="root", password="", database="bd_teste")

cursor = connection.cursor()


def linhaEspc():
    print('-=-' * 15)


# Create
def criar_novo_Prod():
    linhaEspc()
    nome_produtos = input("Digite o nome do produto: ").strip().title().replace(' ', '_').replace("'", "").replace(")", "").replace("(", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace(":", "").replace(";", "").replace("/", "").replace("=", "").replace("+", "").replace("-", "").replace("*", "").replace("&", "").replace("%", "").replace("$", "").replace("#", "").replace("@", "").replace("--", "")
    preco_produtos = float(input("Digite o preço do produto: "))
    comando = f'insert into vendas (idVendas, Nome_prod, Preço) values (default, "{nome_produtos}", {preco_produtos:.2f})'
    cursor.execute(comando)
    connection.commit()


# Read
def ler_todos_Prod():
    linhaEspc()
    cursor.execute('select * from vendas')
    resultados = cursor.fetchall()
    print(resultados)
    for linha in resultados:
        print(f'O produto de ID {linha[0]} posui o nome de produto: {linha[1]} e custa R${linha[2]:.2f}\n')
        sleep(0.5)


# Update

def atualizar_Prod():
    ler_todos_Prod()
    linhaEspc()
    id_prod = int(input("Digite o ID do produto que deseja atualizar: "))
    nome_prod = input("Digite o novo nome do produto: ")
    preco_prod = float(input("Digite o novo preço do produto: "))
    linhaEspc()
    comando = f"update vendas set Nome_prod = '{nome_prod}', Preço = {preco_prod:.2f} where idVendas = {id_prod}"
    cursor.execute(comando)
    connection.commit()
    print("Produto atualizado com sucesso!")


# Delete

def deleta_Prod():
    ler_todos_Prod()
    linhaEspc()
    id_prod = int(input("Digite o ID do produto que deseja deletar: "))
    comando = f"delete from vendas where idVendas = {id_prod}" # Sempre fazemos a procura via ID, pois é o único dado que não se repete, assim não temos o risco de apagar mais de um produto
    cursor.execute(comando)
    connection.commit()
    print("Produto deletado com sucesso!")


# Menu
if __name__ == '__main__':
    try:
        while True:
            print('-=-' * 10)
            print("1 - Criar novo produto")
            print("2 - Ler todos os produtos")
            print("3 - Atualizar um produto")
            print("4 - Deletar um produto")
            print("5 - Sair")
            print('-=-' * 10)
            opcao = int(input("Digite a opção: "))
            if opcao == 1:
                criar_novo_Prod()
            elif opcao == 2:
                ler_todos_Prod()
            elif opcao == 3:
                atualizar_Prod()
            elif opcao == 4:
                deleta_Prod()
            elif opcao == 5:
                break
            else:
                print("Opção inválida")

        cursor.close()
        connection.close()
    except KeyboardInterrupt:
        print("Programa interrompido pelo usuário")
        cursor.close()
        connection.close()
        exit()
    except Exception as erro:
        print(f"Ocorreu um erro: {erro}. E sua classe é {erro.__class__}")
        cursor.close()
        connection.close()
        exit()


import mysql.connector

con = mysql.connector.connect(host='localhost', database='cadastro', user='root', password='')

if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ", db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ", linha)
    cursor.execute("select * from pessoas;")
    linhas = cursor.fetchall()
    print("Total de registros retornados: ", cursor.rowcount)
    for l in linhas:
        print(l)
'''if con.is_connected():
    cursor.close()
    con.close()
    print("Conexão ao MySQL foi encerrada")'''

import win32com.client as win32

outlook = win32.Dispatch('outlook.application')
titulo = 'Nova menssagem sobre seu Site!'
menssagem = str(input('Digite o conteudo da menssagem: '))
nome = str(input('Digite seu nome: '))

email = outlook.CreateItem(0)

email.To = "rafael.segal81@gmail.com"
email.Subject = titulo
email.HTMLbody = (f"""
                    <h1> Olá Rafael!</h1>
                    
                    <p>{menssagem}</p>
                    
                    <h2> De: </h2> <h1>{nome}</h1>
                    """)
email.Send()
print("Email Enviado")

import win32com.client as win32

outlook = win32.Dispatch('outlook.application')
titulo = 'Nova menssagem sobre seu Site!'
menssagem = "vou te hackiei kkkkk"
nome = "rafael"
r = 0
for r in range(0, 10):
    email = outlook.CreateItem(0)

    email.To = "mamacosupremo.sol@gmail.com"
    email.Subject = titulo
    email.HTMLbody = (f"""
                        <h1> Olá Rafael!</h1>
                        
                        <p>{menssagem}</p>
                        
                        <h2> De: </h2> <h1>{nome}</h1>
                        """)
    email.Send()
    print("Email Enviado")

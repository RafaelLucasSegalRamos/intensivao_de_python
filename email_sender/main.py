import win32com.client as win32

outlook = win32.Dispatch('outlook.application')
titulo = 'Nova menssagem sobre seu Site!'
menssagem = "só trocando a menssagem msm"
nome = "rafael"

email = outlook.CreateItem(0)

email.To = "mamacosupremo.sol@gmail.com"
email.Subject = titulo
email.HTMLbody = (f"""
                    <h1> Olá Rafael!</h1>
                    
                    <p>{menssagem}</p>
                    
                    <h2> De: </h2> <h1>{nome}</h1>
                    """)
email.Send()
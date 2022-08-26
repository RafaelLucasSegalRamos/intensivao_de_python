import smtplib
import email.message

def enviar_email():
    corpo_email = """
    <h1> Parágrafo 1 </h1>
    <h2> Parágrafo 2 </h2>
    """
    
    msg = email.message.Message()
    msg['Subject'] = "Tentando isso"
    msg['From'] = 'rafael.testescodigos@gmail.com'
    msg['To'] = 'mamacosupremo.sol@gmail.com'
    # password = 'hidden :)'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)
    
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado') 
    
enviar_email()
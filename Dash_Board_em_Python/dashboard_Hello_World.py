from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='Hello World'),
    html.P(children='testeando', className='testado'),
    html.A(href='https://www.youtube.com/watch?v=aS64PvDqCbU&list=TLPQMTQwNjIwMjO4XNtTHelN8A&index=2',
           children='Clique em mim!', target='_blank', id='ola')
    
])

if __name__ == '__main__':
    app.run_server(debug=True)

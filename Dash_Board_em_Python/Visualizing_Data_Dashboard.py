# Import packages
from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children='My First App with Data and a Graph'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    dcc.Graph(figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg')),
    dcc.Graph(figure=px.histogram(df, x='continent', y='lifeExp', histfunc='min')),
    dcc.Graph(figure=px.histogram(df, x='continent', y='lifeExp', histfunc='max'))

])



# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)


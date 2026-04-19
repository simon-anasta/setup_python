# Dash app - simple app with close button

import dash
from dash import html, dcc

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Hello Dash!"),
    html.Button("Close", id="close-button")
])

if __name__ == '__main__':
    app.run(debug=True)

# also reuires Ctrl + C to return to terminal after closing the app

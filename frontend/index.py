from dash import html, dcc
from dash.dependencies import Input, Output

from app import app
from pages import url, design, ingredient, report
from components import navbar

# define components
nav = navbar.Navbar()



#footer = footer.Foorter()

# Define the index page layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    nav, 
    html.Div(id='page-content', children=[]), 
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/url':
        return url.layout
    if pathname == '/design':
        return design.layout
    if pathname == '/ingredient':
        return ingredient.layout
    if pathname == '/report':
        return report.layout
    else:
        return " Wellcome to Green Recipe :) "

# Run the app on localhost:8050
if __name__ == '__main__':
    app.run_server(debug=True)

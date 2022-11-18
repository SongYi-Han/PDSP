# Import necessary libraries 
from dash import html
import dash_bootstrap_components as dbc


# Define the page layout
layout = dbc.Container([
    dbc.Row([
        html.Center(html.H1("Ingredient")),
        html.Br(),
        html.Hr(),
        dbc.Col([
            html.P("This is column 1."), 
            dbc.Button("get ingredient from user", color="primary")
        ]), 
        dbc.Col([
            html.P("This is column 2."), 
            html.P("we will recommend top4 similar ingredients based on user input"),
        ])
    ])
])

# Import necessary libraries 
import dash
from dash import html
import dash_bootstrap_components as dbc

### Add the page components here 

# Define the final page layout
layout = dbc.Container([
    dbc.Row([
        html.Center(html.H1("Report")),
        html.Br(),
        html.Hr(),
        dbc.Col([
            html.P("This is column 1."), 
            dbc.Button("Test Button", color="secondary")
        ]), 
        dbc.Col([
            html.P("This is column 2. we will display report here"), 
            
        ])
    ])
])
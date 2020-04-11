# -*- coding: utf-8 -*-
import dash
import dash_table
import plotly.graph_objs as go
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

layout = dbc.Container([
#     dbc.Row(
#     dbc.Navbar(
#     [
#         html.A(
#             # Use row and col to control vertical alignment of logo / brand
#             dbc.Row(
#                 [
#                     dbc.Col(dbc.NavbarBrand("Navbar", className="ml-2")),
#                 ],
#                 align="center",
#                 no_gutters=True,
#             ),
#             href="https://plot.ly",
#         ),
#         dbc.NavbarToggler(id="navbar-toggler"),
#     ],
#     color="dark",
#     dark=True,
#     ),
#     className="ml-auto flex-nowrap mt-md-0",
#     align="center",
# ),
            dbc.Row(
    [
        dbc.Col(
            [
                html.H1('Get an instant data analysis report of your spreadsheets', style={'text-align':'center', "color":"white",
                "font-family": "Verdana; Gill Sans"}),
                html.H3('Using the powerful Pandas Profiling library on Python', style={'text-align':'center', "color":"white",
                "font-family": "Verdana; Gill Sans"})
            ]
        )
    ],
    style ={"padding":"10% 0% 10% 0%", "background-color":"#3CB371"}
),
        dbc.Row(
            [
                dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=False
    ),
            ]
        ),
        dbc.Row(id='output-report',
        style={
            'width': '100%',
            'height': '1000px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderWidth': '1px',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        })
]
, fluid = False)

import dash
from dash import html, dcc
from Charts import pop_ev_make, pop_per_state, pop_per_type, pop_per_e_utility, pop_per_location
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
import pandas as pd
import plotly.express as px

external_stylesheets = [
    {'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css', 'rel': 'stylesheet'},
    {'href': '/assets/my_styles.css', 'rel': 'stylesheet'}
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

header = html.Div(
    children=
    [
        html.H1('Electric Vehicle Population Data Dashboard'),
        html.P('This dataset contains EV registered through Washington State Department of Licensing (DOL)')
    ],
    className='header_container',
)

tab = dbc.Tabs([
    dbc.Tab([
        html.Ul([
            dcc.Graph(
                id='ev_make',
                figure=pop_ev_make(),
                className='chart'
            )
        ])
    ], label='EV Population per Make'),
    dbc.Tab([
        html.Ul([
            dcc.Graph(
                id='ev_make',
                figure=pop_per_state(),
                className='chart'
            )
        ])
    ], label='EV Population per State'),
    dbc.Tab([
        html.Ul([
            dcc.Graph(
                id='ev_make',
                figure=pop_per_type(),
                className='chart'
            )
        ])
    ], label='EV Population per Vehicle Type'),
    dbc.Tab([
        html.Ul([
            dcc.Graph(
                id='ev_make',
                figure=pop_per_e_utility(),
                className='chart'
            )
        ])
    ], label='EV Population per Electric Utility'),
    dbc.Tab([
        html.Ul([
            dcc.Graph(
                id='ev_make',
                figure=pop_per_location(),
                className='chart'
            )
        ])
    ], label='EV Population per Location')
])

app.layout = html.Div(
    children=
    [
        header,
        tab,

    ],
    className='layout_container'

)

if __name__ == '__main__':
    app.run_server(debug=True)

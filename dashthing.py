import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

import json

from q_functions_split import db_interface
steamdb = db_interface('steamdata.db')

steamdb.set_query('genres')
genres = steamdb.get_df().Genre.unique()

geojson = json.loads(open("resources\countries.geojson", 'r').read())

app = dash.Dash(__name__)

app.layout = html.Div([
    html.P("maperino:"),
    dcc.Dropdown(
        id='genre', 
        options=[{'value': x, 'label': x} 
                 for x in genres],
        value=genres[0]
        # ,labelStyle={'display': 'inline-block'}
    ),
    dcc.Graph(id="choropleth"),
])

@app.callback(
    Output("choropleth", "figure"), 
    [Input("genre", "value")])
def display_choropleth(genre):
    print(genre)
    query = 'select * from '
    steamdb.set_query('vw_players_3l')
    df = steamdb.get_df()
    fig = px.choropleth_mapbox(
        df, 
        geojson=geojson, 
        color='players',
        locations="a3", 
        featureidkey="id",
        center={"lat": 0.0, "lon": 0.0}, 
        zoom=1,
        range_color=[0, 2221908],
        mapbox_style='open-street-map'
    )
    fig.update_layout(
        margin={"r":0,"t":0,"l":0,"b":0}
    )

    return fig

app.run_server(debug=True)

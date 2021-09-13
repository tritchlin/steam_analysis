
from dash_bootstrap_components._components.CardBody import CardBody
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from app import app
import plotly.express as px
from q_functions_split import db_interface
from dash.dependencies import Input, Output
import json


#####################################
# Add your data
#####################################

steamdb = db_interface('steamdata.db')

steamdb.set_query(text='select * from games_genres')
genres = steamdb.get_df().Genre.unique()

# geojson = json.loads(open("resources\countries.geojson", 'r').read())
#  Mac 
geojson = json.loads(open("resources/countries.geojson", 'r').read())


#####################################
# Styles & Colors
#####################################

# NAVBAR_STYLE = {
#     "position": "fixed",
#     "top": 0,
#     "left": 0,
#     "bottom": 0,
#     "width": "8rem",
#     "padding": "2rem 1rem",
#     "background-color": "#f8f9fa",
# }

CONTENT_STYLE = {
    "top":0,
    "margin-top":'2rem',
    "margin-left": "2rem",
    "margin-right": "2rem",
}

#####################################
# Create Auxiliary Components Here
#####################################
PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

options = [{'value': x, 'label': x} for x in genres]
items = [dbc.DropdownMenuItem(i) for i in options] #remove curly brackets on this line

dropdown = dbc.Row(
    [
        dbc.Col(dcc.Dropdown(
        id='genre', 
        options=[{'value': x, 'label': x} 
                 for x in genres],
        value=genres[0]
        ),
        ),
    ],
    no_gutters=True,
)

def nav_bar():
    """
    Creates Navigation bar
    """
    navbar = dbc.Navbar(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height='30px')),
                        dbc.Col(dbc.NavbarBrand('Steam Game Database', className='ml-2')),
                    ],
                    align='center',
                    no_gutters=True,
                ),
            ),
            dbc.Col(dropdown, id="navbar-collapse"
            ),
        ],
        color="dark",
        dark=True,
    )   
    return navbar

#graph 1
@app.callback(
    Output("choropleth", "figure"), 
    [Input("genre", "value")])
def display_choropleth(genre):
    query = f"select * from vw_genre_ownership_by_country where genre = '{genre}';"
    steamdb.set_query(text = query)
    df = steamdb.get_df()
    max_value = df['genre_owners'].max()

    fig = px.choropleth_mapbox(
        df, 
        geojson=geojson, 
        color='genre_owners',
        locations="countrycode", 
        featureidkey="id",
        center={"lat": 0.0, "lon": 0.0}, 
        zoom=1,
        range_color=[0, max_value],
        mapbox_style='open-street-map',
        height=250
    )
    fig.update_layout(
        margin={"r":0,"t":0,"l":0,"b":0},
        coloraxis_colorbar=dict(title="Owners")
    )
    
    return fig

#graph 2
@app.callback(
    Output("bar", "figure"), 
    [Input("genre", "value")])
def display_bargraph(genre):
    query = f"select * from vw_genre_ownership_by_country where genre = '{genre}';"
    steamdb.set_query(text = query)
    df = steamdb.get_df()
    max_value = df['genre_owners'].max()
    xval = df['genres']
    yval = df['genre_owners']
    # country = df['countrycode']

    fig = px.bar(
        df,
        x=xval,
        y=yval,
        log_y=True,
        height=250
    )

    fig.update_layout(
        margin={"r":0,"t":0,"l":0,"b":0},
    )
    fig.update_traces(textposition="bottom right")
    return fig

#graph 3 - melissa ( achievement by genre )
pie_query = f"select * from vw_genre_achieve;"
steamdb.set_query(text = pie_query)
pie_df = steamdb.get_df()
pie_labels = pie_df['Genre']
pie_values = pie_df['achievements_percentages']
pie_fig = px.pie(
    pie_df,
    values=pie_values,
    names=pie_labels,
    height=250,
    color='Genre',
    color_discrete_map={'RPG':'#00065b',
                        'Action':'#440a56',
                        'Racing':'#671852',
                        'Adventure':'#85294d',
                        'Strategy':'#a13e49',
                        'Indie':'#b95444',
                        'Free to Play':'#cf6d3f',
                        'Stimulation':'#e28639',
                        'Casual':'#f1a231',
                        'Sports':'#fcc027',
                        'Massively Multiplayer':'#ffdf18',
                        'Early Access':'#ffff00'
                        
})


pie_fig.update_layout(
    title_text="Avg. Achievements Percentage per Genre",
    # Add annotations in the center of the donut pies.
    # annotations=[dict(text='GHG', x=0.18, y=0.5, font_size=20, showarrow=False),
    showlegend=False,
    margin={"r":0,"t":0,"l":0,"b":0},
)

# @app.callback(
#     Output("pie", "figure"), 
#     [Input("genre", "value")])
# def display_linegraph(genre):
#     pie_query = f"select * from vw_genre_achieve where genre = '{genre}';"
#     steamdb.set_query(text = pie_query)
#     pie_df = steamdb.get_df()
#         # max_value = df['Genre'].max()
#     pie_labels = pie_df['Genre']
#     pie_values = pie_df['achievements_percentages']


    # pie_fig = px.pie(pie_df, values= pie_values, names= pie_labels)
    # dcc.Graph(id='pie', figure=pie_fig)

    # fig.update_layout(
    # showlegend=False,
    # plot_bgcolor="white",
    # margin=dict(t=10,l=10,b=10,r=10)

        
# return pie_fig
    # country = df['countrycode']


#####################################
# Create Page Layouts Here
#####################################
first_card = dbc.CardBody(
        [
            dcc.Graph(id="choropleth")
        ],
    ),

second_card = dbc.CardBody(
        [
            dcc.Graph(figure=pie_fig),
        ],
    ),

third_card = dbc.CardBody(
        [
            dcc.Graph(id='bar'),
        ],
    ),

layout1 = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Card(first_card),
                    ],
                    width=8,
                ),
                dbc.Col(
                    [
                        dbc.Card(second_card),
                    ],
                    width=4,
                ),
            ],
            # no_gutters=True,
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Card(third_card),
                    ],   
                    width=8,
                ),
                dbc.Col(
                    [
                        # dbc.Card(second_card),
                    ],   
                    width=4,
                ),
            ],
            # no_gutters=True,
            style={'margin-top': '25px'},
        ),
    ],
)


layout2 = html.Div(
    [
        html.H2('Page 2'),
        html.Hr(),
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.H4('Country'),
                                html.Hr(),
                                dcc.Dropdown(
                                    id='page2-dropdown',
                                    options=[
                                        {'label': '{}'.format(i), 'value': i} for i in [
                                        'United States', 'Canada', 'Mexico'
                                        ]
        ]
                                ),
                                html.Div(id='selected-dropdown')
                            ],
                            width=6
                        ),
                        dbc.Col(
                            [
                                html.H4('Fruit'),
                                html.Hr(),
                                dcc.RadioItems(
                                    id='page2-buttons',
                                    options = [
                                        {'label':'{}'.format(i), 'value': i} for i in [
                                        'Yes ', 'No ', 'Maybe '
                                        ]
                                    ]
                                ),
                                html.Div(id='selected-button')
                            ],
                        )
                    ]
                ),
            ]
        )
    ])
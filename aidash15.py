#!/usr/bin/env python
# coding: utf-8

# In[57]:


import dash
from dash import dcc, html, Input, Output
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
from plotly.express import data
import dash_bootstrap_components as dbc
import numpy as np
import pickle
import os


# In[58]:


#Initiate the app, define theme, make is mobile responsive
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.PULSE, dbc.icons.BOOTSTRAP, dbc.icons.FONT_AWESOME],
            meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}])

#Read files

#Build components


# In[59]:


#Design layout
app.layout = dbc.Container([

# Top boarder

    dbc.Row([   # Top border 
        dbc.Col([        #1st column
            html.Div([
                html.Div("Overview/Teamwork/Patient",
                        className='text-end'),
            ])
        ], #width={'size': 4, 'order': 1})
            xs=6, sm=6, md=6, lg=2, xl=2         # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
        ),

        dbc.Col([        #2st column
            html.Div([
                html.P("→ Patient profile", 
                        style={"color": "purple"},     # #652d87
                        className='text-start fw-bold')  
            ])
        ], #width={'size': 4, 'order': 1})
            xs=6, sm=6, md=6, lg=2, xl=2         # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
        ),

        dbc.Col([        #3rd column
            dbc.CardImg(
                    src='https://strikersoft.com/media/images/SwipeCare_Heart_1000x213.width-300.png', alt='image',
                    top=True, style={"width": "8rem", "margin": "auto"}, className="d-flex align-items-center"),               # image at the top
        ],  #width={'size': 1, 'offset': 1}
            xs=12, sm=12, md=12, lg=4, xl=4         # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
        ),



        dbc.Col([        #4th column
           html.Div([
                dbc.Label([
                    "Light theme",
                    html.I(className="bi bi-brightness-high-fill fa-fw"),
                ],
                className="d-flex align-items-center",
                ),
           ])
        ], #width={'size': 4, 'order': 1})
            xs=4, sm=4, md=4, lg=2, xl=2         # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
        ),

        dbc.Col([        #5th column
           html.Div([
                dbc.Label([
                    "ENG",
                    html.I(className="fa fa-globe fa-fw"),
                ],
                className="d-flex align-items-center",
                ),
           ])
        ], #width={'size': 4, 'order': 1})
            xs=4, sm=4, md=4, lg=1, xl=1         # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
        ),

        dbc.Col([        #6th column
           html.Div([
                dbc.Label([
                    "John Doe",
                    html.I(className="fa fa-arrow-right-from-bracket fa-fw"),
                ],
                className="d-flex align-items-center",
                ),
           ])
        ], #width={'size': 4, 'order': 1})
            xs=4, sm=4, md=4, lg=1, xl=1         # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
        ),

    ],  className="pt-3",  #Padding top
        justify='start'),  #can also use center, end, between, around. 'start' = everything in the row will be put to the left of the screen


    dbc.Row([   # Thin horozontal line across the screen
        html.Div(html.Hr(style={'borderWidth': "0.8vh", "color": "#808080"}))
    ]),


# Below top boarder, 3 columns om screen

dbc.Row([

# Column left with Patient into   
    dbc.Col([
        dbc.CardImg(
                    src='https://strikersoft.com/media/images/Left_panel_SC_on_PC2.width-1280.png', alt='image',
                    top=True, style={"width": "18rem", "margin": "left"}, className="d-flex align-items-center"),               # image at the top
    ],  #width={'size': 1, 'offset': 1}
            xs=12, sm=12, md=12, lg=4, xl=4         # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
    ),
    

# Column middle with input sections for AI Heart
    dbc.Col([  # Middle column on screen
        
        dbc.Row([
                dbc.Col([        # Hace to define the column first. The first column
                    html.H3("AI Heart Disease Detection",
                        className='text-center', style={"color": "#000000"}),    # Bootstrap specification (see Cheat Sheet)
            ], #width={'size': 4, 'order': 1})
                xs=12, sm=12, md=12, lg=12, xl=12         # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
            )
        ]),

        dbc.Row([   # Thin horozontal line across the screen
            html.Div(html.Hr(style={'borderWidth': "0.8vh", "color": "#808080"}))
        ]),         
                   
        dbc.Row([   # Q1 Age
            dbc.Col([        
                dbc.Label("1. Age:", className='fw-bold'),
                dbc.Input(id="age_var", placeholder="Enter age in years", type="number", min=0, max=120, step=1, style={"border-radius": "7px"}),
            ], #width={'size': 4, 'order': 2})
                xs=12, sm=12, md=12, lg=12, xl=12         # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
            )
        ],  className="pt-1",
            justify='center'),  #can also use center, end, between, around. 'start' = everything in the row will be put to the left of the screen
  
        dbc.Row([   # Q2 Sex
            dbc.Col([        
                dbc.Label("2. Sex:", className='fw-bold'),  # Bold does not work...
                dbc.RadioItems(
                    options=[
                        {"label": "Male", "value": "Male"},
                        {"label": "Female", "value": "Female"},
                    ],
                    value="None",    #Initial value shown labelStyle 
                    id="sex_var",
                    inline=True,
                ),      
            ], #width={'size': 4, 'order': 1})
                xs=12, sm=12, md=12, lg=12, xl=12         # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
            )
        ],  className="pt-4", 
            justify='center'),  #can also use center, end, between, around. 'start' = everything in the row will be put to the left of the screen

        dbc.Row([   # Q3 Chest Pain Type
            dbc.Col([        
                dbc.Label("3. Chest Pain Type:", className='fw-bold'),
                dbc.RadioItems(
                    options=[
                        {"label": "Typical angina", "value": "ChestPainTyp"},
                        {"label": "Non-anginal pain", "value": "ChestPainNon"},
                        {"label": "Atypical angina", "value": "ChestPainAtyp"},
                        {"label": "Asymptomatic", "value": "ChestPainAsym"},
                    ],
                    # value="Q3-1",    #Initial value shown
                    id="cp_var",
                    inline=True,
                ),      
            ], #width={'size': 4, 'order': 1})
                xs=12, sm=12, md=12, lg=12, xl=12         # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
            )
        ],  className="pt-4",
            justify='center'),  #can also use center, end, between, around. 'start' = everything in the row will be put to the left of the screen

        dbc.Row([   # Q4 Resting Blood Pressure
            dbc.Col([        
                dbc.Label("4. Resting Blood Pressure (Systolic):", className='fw-bold'),
                dbc.Input(id="trestbps_var", placeholder="mmHg", type="number", min=40, max=380, step=1, style={"border-radius": "7px"}), 
            ], #width={'size': 4, 'order': 2})
                xs=12, sm=12, md=12, lg=12, xl=12         # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
            )
        ],  className="pt-4",
            justify='center'),  #can also use center, end, between, around. 'start' = everything in the row will be put to the left of the screen

        dbc.Row([   # Q5 Serum Cholesterol
            dbc.Col([        
                dbc.Label("5. Serum Cholesterol:", className='fw-bold'),
                dbc.Input(id="chol_var", placeholder="mg/dL", type="number", min=30, max=999, step=1, style={"border-radius": "7px"}),   #MIN/MAX???????
            ], #width={'size': 4, 'order': 2})
                xs=12, sm=12, md=12, lg=12, xl=12         # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
            )
        ],  className="pt-4",
            justify='center'),  #can also use center, end, between, around. 'start' = everything in the row will be put to the left of the screen

        dbc.Row([   # Q6 Achieved max heart rate
            dbc.Col([        
                dbc.Label("6. Achieved Max. Heart Rate:", className='fw-bold'),
                dbc.Input(id="thalach_var", placeholder="bpm", type="number", min=25, max=500, step=1, style={"border-radius": "7px"}),  
            ], #width={'size': 4, 'order': 2})
                xs=12, sm=12, md=12, lg=12, xl=12         # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
            )
        ],  className="pt-4",
            justify='center'),  #can also use center, end, between, around. 'start' = everything in the row will be put to the left of the screen

        dbc.Row([   # Q7 Exercised-induced angina
            dbc.Col([        
                dbc.Label("7. Exercise-induced Angina", className='fw-bold'),
                dbc.RadioItems(
                    options=[
                        {"label": "Yes", "value": "Angina-Yes"},
                        {"label": "No", "value": "Angina-No"},
                    ],
                    #value="Male",    #Initial value shown
                    id="exang_var",
                    inline=True,
                ),      
            ], #width={'size': 4, 'order': 1})
                xs=12, sm=12, md=12, lg=12, xl=12         # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
            )
        ],  className="pt-4",
            justify='center'),  #can also use center, end, between, around. 'start' = everything in the row will be put to the left of the screen

        dbc.Row([   # Q8 ST depression induced by exercise relative to rest
            dbc.Col([        
                dbc.Label("8. ST Depression Induced by Exercise Relative to Rest:", className='fw-bold'),
                dbc.Input(id="oldpeak_var", placeholder="mm", type="number", min=0, max=50, style={"border-radius": "7px"}),   #MIN/MAX???????
              ], #width={'size': 4, 'order': 2})
                xs=12, sm=12, md=12, lg=12, xl=12         # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
            )
        ],  className="pt-4",
            justify='center'),  #can also use center, end, between, around. 'start' = everything in the row will be put to the left of the screen

        dbc.Row([   # Q9 Peak slope in exercise ST segment
            dbc.Col([        
                dbc.Label("9. Peak Slope in Exercise ST Segment:", className='fw-bold'),
                dbc.RadioItems(
                    options=[
                        {"label": "Up", "value": "STsegmUp"},
                        {"label": "Plain", "value": "STsegmPlain"},
                        {"label": "Down", "value": "STsegmDown"},
                    ],
                    # value="Q3-1",    #Initial value shown
                    id="slope_var",
                    inline=True,
                ),      
            ], #width={'size': 4, 'order': 1})
                xs=12, sm=12, md=12, lg=12, xl=12         # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
            )
        ],  className="pt-4 pb-0",
            justify='center'),  #can also use center, end, between, around. 'start' = everything in the row will be put to the left of the screen

     dbc.Row([   # Button to predict
            dbc.Col([        
                dbc.Button("Calculate", id="predict_button", n_clicks=0, color="primary", size="lg", className="me-2", style={"border-radius": "7px"}),
                dbc.Button("Reset", id="reset_button", outline=True, color="secondary", size="lg", className="me-2", style={"border-radius": "7px"}),             
            ], #width={'size': 4, 'order': 1})
                xs=12, sm=12, md=12, lg=12, xl=12         # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
            )
        ],  className="pt-5 pb-4",
            justify='center'),  #can also use center, end, between, around. 'start' = everything in the row will be put to the left of the screen

     dbc.Row([   # Outcome of prediction (Heart problems or not)
            dbc.Col([  
                dbc.Alert(children="Please enter patient information.", id="output_var", color="light"),
            ], #width={'size': 4, 'order': 1})           
                xs=12, sm=12, md=12, lg=12, xl=12         # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
            )
        ],  className="pt-0",
            justify='center'),  #can also use center, end, between, around. 'start' = everything in the row will be put to the left of the screen


    # End of Middle column
    ], class_name="pt-0", style={'height': '700px', 'overflow': 'scroll'},
    ),


# Right column for history of acitivies
    dbc.Col([
        dbc.Row([
            dbc.CardImg(
                    src='https://strikersoft.com/media/images/Right_panel_SC_on_PC2.width-1280.png', alt='image',
                    top=True, className="d-flex jusitfy-content-end", style={"width": "18rem"}),               # image at the top
            ],  
            className="pt-1",
            justify='end'),  #can also use center, end, between, around. 'start' = everything in the row will be put to the left of the screen
        ],  #width={'size': 1, 'offset': 1}
        xs=12, sm=12, md=12, lg=4, xl=4         # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
    )
])

], fluid=True)   # fluid=True means the whole screen is filled with the 12 columns, it "floats" out to the sies.


# In[60]:


#Run the app

# Q1 Sex
@app.callback(
    Output(component_id="output_var", component_property="children"),
    [State(component_id="sex_var", component_property="value"),
     State(component_id="age_var", component_property="value"),
     State(component_id="cp_var", component_property="value"),
     State(component_id="trestbps_var", component_property="value"),
     State(component_id="chol_var", component_property="value"),
     State(component_id="thalach_var", component_property="value"),
     State(component_id="exang_var", component_property="value"),
     State(component_id="oldpeak_var", component_property="value"),
     State(component_id="slope_var", component_property="value")],
    Input(component_id="predict_button", component_property="n_clicks"),
    prevent_initial_call=False   # When webpage is refreshed, it triggers all recalls, dont want that = True
)



def saved_model(sex, age, cp, trestbps, chol, thalach, exang, oldpeak, slope, n_clicks):
    if n_clicks > 0:
        
        # Mattias code
        tmp_df = pd.DataFrame({"sex": [sex], "age": [age], "cp": [cp], "trestbps": [trestbps], "chol": [chol],
                                  "thalach": [thalach], "exang": [exang], "oldpeak": [oldpeak], "slope": [slope]})

        num_feats = ["age", "trestbps", "chol", "thalach", "oldpeak"]
        cat_feats = ["slope", "sex", "exang", "cp"]

        
        with open(r"saved_model", "rb") as pickle_file:
                clf = pickle.load(pickle_file)
        


        result = clf.predict(tmp_df)
        print(result)

        presence = dbc.Alert("Patient may have presence of heart disease.", color="danger", className='fw-bold color black')
        absence = dbc.Alert("Patient is not suspected to have heart disease.", color="success", className='fw-bold color black')

       
        if result == True:
            return presence
        elif result == False:
            return absence
    

    elif n_clicks == 0:
        nrzero= dbc.Alert("Please enter patient information.", color="light")
        return nrzero
        raise dash.exceptions.PreventUpdate   # Dont update if field filled out but button not clicked
   


@app.callback( #for the reset button, resets all values and resets the predict button to 0 clicks
    [Output(component_id="sex_var", component_property="value"),
     Output(component_id="age_var", component_property="value"),
     Output(component_id="cp_var", component_property="value"),
     Output(component_id="trestbps_var", component_property="value"),
     Output(component_id="chol_var", component_property="value"),
     Output(component_id="thalach_var", component_property="value"),
     Output(component_id="exang_var", component_property="value"),
     Output(component_id="oldpeak_var", component_property="value"),
     Output(component_id="slope_var", component_property="value"),
     Output(component_id="predict_button", component_property="n_clicks")],
    [Input('reset_button','n_clicks')])

def update(reset):
    return 'None', 'Enter value', 'Male', 'Enter value', 'Enter value', 'Enter value', 'Male', 'Enter value', 'Male', 0


if __name__ == '__main__':
    app.run_server(debug=False, port=8043)


# %%

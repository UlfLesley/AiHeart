import pickle
import dash
import pandas as pd
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import os
from sklearn.compose import ColumnTransformer
from sklearn.neural_network import MLPClassifier

script_path = os.getcwd()

app = dash.Dash(__name__)

app.layout = html.Div(
    children=
    [
        html.Div(
            id="input_div",
            children=[
                html.H1("This is the heart attack risk classifier!"),
                html.P("Sex"),
                dcc.RadioItems(
                    options=[
                        {"label": "Male", "value": "0"},
                        {"label": "Female", "value": "1"},
                        {"label": "Other", "value": "2"}
                    ],
                    id="sex_var"
                ),

                html.P("Age"),
                dcc.Input(id="age_var", value=0),

                html.P("Chest pain type"),
                dcc.RadioItems(
                    options=[
                        {"label": "Typical Angina", "value": "1"},
                        {"label": "Atypical Angina", "value": "2"},
                        {"label": "Non-anginal pain", "value": "3"},
                        {"label": "Asymptomatic", "value": "4"}
                    ],
                    id="cp_var"
                ),

                html.P("Resting blood pressure"),
                dcc.Input(id="trestbps_var", value=0),

                html.P("Serum cholesterol"),
                dcc.Input(id="chol_var", value=0),

                html.P("Is the fasting blood sugar above 120 mg/dl?"),
                dcc.RadioItems(
                    options=[
                        {"label": "Yes", "value": True},
                        {"label": "No", "value": False},
                    ],
                    id="fbs_var"
                ),

                html.P("Resting ECG results"),
                dcc.RadioItems(
                    options=[
                        {"label": "Normal", "value": "0"},
                        {"label": "ST-T abnormality", "value": "1"},
                        {"label": "Probable of definite left ventricular hypertrophy", "value": "2"}
                    ],
                    id="restecg_var"
                ),

                html.P("Maximum heart rate achieved"),
                dcc.Input(id="thalach_var", value=0),

                html.P("Presence of exercise induced angina?"),
                dcc.RadioItems(
                    options=[
                        {"label": "Yes", "value": True},
                        {"label": "No", "value": False}
                    ],
                    id="exang_var"
                ),

                html.P("ST depression induced by exercise relative to rest"),
                dcc.Input(id="oldpeak_var", value=0),

                html.P("The slop of the peak exercise ST segment"),
                dcc.RadioItems(
                    options=[
                        {"label": "Upsloping", "value": "1"},
                        {"label": "Flat", "value": "2"},
                        {"label": "Downsloping", "value": "3"}
                    ],
                    id="slope_var"
                ),

                html.Button("Click me!", n_clicks=0, id="action_var")
            ],
        ),

        html.Div(
            id="output_div",
            children=html.P(children="Please enter patient information.", id="output_var")
        )]
)

@app.callback(
    Output(component_id="output_var", component_property="children"),
    [State(component_id="sex_var", component_property="value"),
     State(component_id="age_var", component_property="value"),
     State(component_id="cp_var", component_property="value"),
     State(component_id="trestbps_var", component_property="value"),
     State(component_id="chol_var", component_property="value"),
     State(component_id="fbs_var", component_property="value"),
     State(component_id="restecg_var", component_property="value"),
     State(component_id="thalach_var", component_property="value"),
     State(component_id="exang_var", component_property="value"),
     State(component_id="oldpeak_var", component_property="value"),
     State(component_id="slope_var", component_property="value")],
    Input(component_id="action_var", component_property="n_clicks")
)
def classifier(sex, age, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, n):
    if n > 0:
        tmp_df = pd.DataFrame({"sex": [sex], "age": [age], "cp": [cp], "trestbps": [trestbps], "chol": [chol], "fbs": [fbs],
                                  "restecg": [restecg], "thalach": [thalach], "exang": [exang], "oldpeak": [oldpeak], "slope": [slope]})

        num_feats = ["age", "trestbps", "chol", "thalach", "oldpeak"]
        cat_feats = ["restecg", "slope", "sex", "fbs", "exang", "cp"]

        os.chdir("..")
        debug_var = os.getcwd()
        with open(r"classifier", "rb") as pickle_file:
            mlp_clf = pickle.load(pickle_file)
        with open(r"preprocessor", "rb") as pickle_file:
            preprocessor = pickle.load(pickle_file)
        os.chdir(script_path)

        prepped_data = preprocessor.transform(tmp_df)

        result = mlp_clf.predict(prepped_data)

        if result == True:
            return "something"
        elif result == False:
            return "something else"

    elif n == 0:
        raise dash.exceptions.PreventUpdate


if __name__ == "__main__":
    app.run_server(debug=True)


# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html as _html, dcc
import plotly.express as px
import pandas as pd



def create_figure(dataframe, x_label, y_label, color=None, barmode="group"):
    return px.line(dataframe, x_label, y_label, color)

class Layout:
    
    def __init__(self):
        self.Elements = []
    
    def H1(self, title):
        self.Elements.append(_html.H1(title))
        return self
    
    def Div(self, content):
        self.Elements.append(_html.Div(content)) 
        return self
        
    def Figure(self, id, figure):
        self.Elements.append(dcc.Graph(id=id, figure=figure))
        return self

    def Build(self):
        return _html.Div(children=self.Elements)
import pandas as pd

variables = [
    {'variable': 'Euros', 'type': 'D0', 'description': ''},
    {'variable': 'Oil', 'type': 'D0', 'description': ''}
]

USER = "Lilian S. de Rivera"
PROJECT ="Time Series Analysis Capstone"
list_datasets = ['Euros','Oil']

DATA = { 'dataset': 'Euros' , 'date_type': 'D0'}


def get_variables():
   return variables

def add_variable(varname, vartype, vardesc):
    dict = { 'variable': varname, 'type':vartype, 'description':vardesc }
    variables.append(dict)
    return True


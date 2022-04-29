import pandas as pd
import os


def get_header_values(dataset):
    if dataset == 'Euros':
        xfile = 'euros.csv'
    else:
        xfile = 'oil.csv'

    xpath = 'c:\\RepoVS\\TestPython\\static\\data\\' + xfile

    xdf = pd.read_csv(xpath)

    return xdf.head(10).to_dict(orient="records")
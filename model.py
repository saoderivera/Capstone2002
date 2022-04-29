import pandas as pd
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import pacf,acf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from math import sqrt

last_model = {
    "last_date": '2022-04-24',
    "months": 3,
    "user" : 'Lilian S. de Rivera',
    "order": 7,
    "alpha": 0.00
}

def get_measures(dataset):
    if dataset == 'Euros':
        xfile = 'euros.csv'
    else:
        xfile = 'oil.csv'

    xpath = 'c:\\RepoVS\\TestPython\\static\\data\\' + xfile

    xdf = pd.read_csv(xpath)

    date_ini = min(xdf['date'])
    date_end = max(xdf['date'])
    num_records = len(xdf)
    mean = xdf['value'].mean()
    std = xdf['value'].std()


    results= adfuller(xdf['value'])
    pvalue = results[1]
    measures_data = {
        'date_ini' :  date_ini,
        'date_end' : date_end,
         'num_records': num_records,
        'type' : 'Daily',
        'pvalue' : pvalue,
        'mean' : mean,
        'std' : std
    }


    return measures_data


def get_correlation(var1,var2):

    xfile1= 'c:\\RepoVS\\TestPython\\static\\data\\' + var1 + '.csv'
    xfile2= 'c:\\RepoVS\\TestPython\\static\\data\\' + var2 + '.csv'

    xdf1 = pd.read_csv(xfile1)
    xdf2 = pd.read_csv(xfile2)

def get_correlations_lags(var1, lags):
    xfile1 = 'c:\\RepoVS\\TestPython\\static\\data\\' + var1 + '.csv'
    xdf1 = pd.read_csv(xfile1)

    df_pacf = pacf(xdf1['value'], nlags=lags, alpha=0.05)
    df_acf = acf(xdf1['value'], nlags=lags, alpha= 0.05)

    y1 = df_acf[1]
    y0 = df_acf[0]
    y_lower = [y1[i][0] for i in range(len(y1))] - y0
    y_upper = [y1[i][1] for i in range(len(y1))] - y0

    yp1 = df_pacf[1]
    yp0 = df_pacf[0]
    yp_lower = [yp1[i][0] for i in range(len(yp1))] - yp0
    yp_upper = [yp1[i][1] for i in range(len(yp1))] - yp0

    res = {
        'x0' : range(lags)

    }
from flask import Flask, render_template, request
import pandas as pd
import mysql_data as msql
import model as md
import bigquery_data as bq
from werkzeug.utils import secure_filename

app = Flask(__name__)

USER = msql.USER
PROJECT = msql.PROJECT
list_datasets = msql.list_datasets
DATA = msql.DATA

list_values = bq.get_header_values(DATA['dataset'])
measures_meta_data = md.get_measures(DATA['dataset'])
last_model = md.last_model

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', user_name=USER, title="Home", project_name=PROJECT, dataset=DATA['dataset'])

@app.route('/datastore')
def datastore():
    return render_template('datastore.html', user_name=USER, title="Data Store", project_name=PROJECT,  dataset=DATA['dataset'] , list_d=list_datasets, values=list_values)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', user_name=USER, title="Home", project_name=PROJECT, dataset=DATA['dataset'], measures=measures_meta_data)

@app.route('/model')
def model():
    return render_template('model.html', user_name=USER, title="Model Definition", project_name=PROJECT, dataset=DATA['dataset'], last=last_model)

@app.route('/predict')
def predict():
    return render_template('predict.html', user_name=USER, title="Model Definition", project_name=PROJECT, dataset=DATA['dataset'], img="none.png")

## Actions
@app.route('/select_variable', methods = ['POST','GET'])
def select_variable():
    if request.method == "POST":
        # getting input with name = variable in HTML form
        variable = request.form.get("variable")
        DATA['dataset'] = variable
        list_values = bq.get_header_values(DATA['dataset'])

    return render_template('datastore.html', user_name=USER, title="Data Store", project_name=PROJECT,  dataset=DATA['dataset'] , list_d=list_datasets, values=list_values)

@app.route('/upload_file', methods = ['POST','GET'])
def upload_file():
    if request.method == "POST":
        f = request.files['file']
        xfile = f.filename
        f.save(secure_filename(xfile))
        xdf = pd.read_csv(xfile)
        xdf = xdf.fillna(method='ffill')
    return render_template('datastore.html', user_name=USER, title="Data Store", project_name=PROJECT, dataset=DATA['dataset'] , list_d=list_datasets)

@app.route('/create_variable', methods = ['POST','GET'])
def create_variable():
    '''
    name of variable : dataset
    type of variable (date ) : date_type
          D0- Daily Information
          W0- Weekly End of Week
          M0- Montly End of Month
     return:
    '''

    if request.method == "POST":
        variable = request.form.get("variable")
        variable = request.form.get('date_type')

    return render_template('datastore.html', user_name=USER, title="Data Store", project_name=PROJECT, dataset=DATA['dataset'], list_d=list_datasets,  values=Datadet)


@app.route('/generate_model', methods = ['POST','GET'])
def generate_model():

    return render_template('predict.html', user_name=USER, title="Model Definition", project_name=PROJECT,
                           dataset=DATA['dataset'], img="1.png")


if __name__ == '__main__':
    app.run()

from flask import Flask, request, make_response
import pandas as pd
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Flask World'

def json_str_to_df(json_str:str):
    return pd.DataFrame(json.loads(json_str))

@app.route('/get_shape', methods=['POST'])
def get_shape():
    df = json_str_to_df(request.json['df'])
    return {'shape':df.shape}

def preprocessing(df:pd.DataFrame):
    return df.reset_index()

@app.route('/get_preprocessed_df', methods=['POST'])
def get_preprocessed_df():
    df = json_str_to_df(request.json['df'])
    df = preprocessing(df)
    return df.to_json()

@app.route('/get_preprocessed_df_and_shape', methods=['POST'])
def get_preprocessed_df_and_shape():
    df = json_str_to_df(request.json['df'])
    df = preprocessing(df)
    res = make_response(df.to_json())
    res.headers['shape'] = df.shape
    return res

if __name__ == '__main__':
    app.run()

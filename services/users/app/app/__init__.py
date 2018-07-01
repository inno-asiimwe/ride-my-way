import os
from flask import Flask, jsonify


app = Flask(__name__)

app_settings = os.getenv('APP_SETTINS')
app.config.from_object(app_settings)


@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': "We are home"
    })

from flask import Flask, render_template, request
import numpy as np
import os
import tensorflow as tf
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
import pickle

app = Flask(__name__)

with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)


def init():
    global model, graph
    graph = tf.Graph()


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")


@app.route('/sentiment_prediction', methods=['POST', 'GET'])
def sent_anly_prediction():
    if request.method == 'POST':
        text = request.form['text']

        tw = tokenizer.texts_to_sequences([text])
        tw = sequence.pad_sequences(tw, maxlen=200)

        with graph.as_default():
            # Load the pre-trained Keras model
            model = load_model('sentiment_analysis.h5')

            probability = model.predict(tw)[0][0]
            prediction = int(model.predict(tw).round().item())

        if prediction == 0:
            sentiment = 'Negative'
        else:
            sentiment = 'Positive'

    return render_template('index.html', text=text, sentiment=sentiment, probability=probability)


init()

if __name__ == "__main__":
    app.run(debug=True)

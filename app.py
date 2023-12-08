from flask import Flask,render_template, request, jsonify
from PIL import Image
import numpy as np
import tensorflow as tf

app = Flask(__name__)

#Load our app model
model = tf.keras.models.load_model('keras_model.h5')

#Uintiz our images' size
target_size = (224,224)

def preprocess_image(image_path):
    img = Image.open(image_path)
    img = img.resize(target_size)
    img_array = np.array(img)/255.0
    img_array = np.expand_dims(img_array,axis=0)
    return img_array


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():

    file = request.files['file']

    if 'file' not in request.files:
        return jsonify({'error':'no file'})
    
    if file.filename == '':
        return jsonify({'error':'file name is empty'})
    
    try:
        img_array = preprocess_image(file)

        #Model Prediction
        predection = model.predict(img_array)
        class_index = np.argmax(predection[0])

        if class_index == 0:
            predictionResults = 'Dog'
        elif(class_index == 1):
            predictionResults = 'Cat'
        return jsonify({'result':predictionResults})
    except Exception as e:
        return jsonify({'error':str(e)})

if __name__ == '__main__':
    app.run(debug=True)

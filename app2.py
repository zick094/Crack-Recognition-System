import tensorflow as tf


import numpy as np

from PIL import Image
import requests
from io import BytesIO
import os

from flask import Flask, render_template, request, Response, url_for



app = Flask(__name__)

UPLOAD_FOLDER = '/tmp/'
ALLOWED_EXTENSIONS = set(['jpg','jpeg','png'])



dict_values = {0:'no cracks',1:'yes cracks'}


def load():
    global services 
    services = dict()
    
    services['model'] = tf.keras.models.load_model('resnet_trained.h5')
    
    
    #services['graph'] = tf.compat.v1.get_default_graph()
    
    
@app.route('/', methods =['GET','POST'])
def analyze():
    if request.method == 'POST':
        
        file = request.files['file']
        img = Image.open(BytesIO(file))
        image_resized = img.resize((224,224))

        
        prediction = services['model'].predict(np.expand_dims(np.array(image_resized, dtype='float32'), axis=0))

        
        #URL = request.form.get('url')
        
        
        # preprocess it to the model format
        
        #response = requests.get(URL)
        #img = Image.open(BytesIO(response.content))
        #image_resized = img.resize((224,224))
        
        
        # predict image
        #with services['graph'].as_default():
        #prediction = services['model'].predict(np.expand_dims(np.array(image_resized, dtype='float32'), axis=0))
            
        
        return ('''
                <h1> Crack: '''+dict_values[np.argmax(prediction[0])]+''' </h1>
                <button> <a href='#' onclick='history.go(-1)'>Back</a> </button> <br><br>
                ''')
#<img src='''+URL+'''> <br>
                    

    return ('''<form id="package_form" action="" method="POST">
            <div>
            <p>Upload Packages:</p>
            <p><input id="upload_button" type="file" class="btn btn-default btn-xs" name="file"></p>
            <p><input id="submit_button" type="submit" class="btn btn-success" value="Upload">
            </div>
            </form>
            ''')
            
            
            
def main():
    load()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    main()
        
        
        
        
                
        

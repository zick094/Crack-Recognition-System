

import tensorflow as tf


import numpy as np

from PIL import Image
import requests
from io import BytesIO
import os

from flask import Flask, request

app = Flask(__name__)

dict_values = {0:'no cracks',1:'yes cracks'}


def load():
    global services 
    services = dict()
    
    services['model'] = tf.keras.models.load_model('./resnet_trained.h5')
    
    
    #services['graph'] = tf.compat.v1.get_default_graph()
    
    
@app.route('/', methods =['GET','POST'])
def analyze():
    if request.method == 'POST':
        
        URL = request.form.get('url')
        
        
        # preprocess it to the model format
        response = requests.get(URL)
        img = Image.open(BytesIO(response.content))
        image_resized = img.resize((224,224))
        
        
        # predict image
        #with services['graph'].as_default():
        prediction = services['model'].predict(np.expand_dims(np.array(image_resized, dtype='float32'), axis=0))
            
        
        return ('''
                <h1> Crack: '''+dict_values[np.argmax(prediction[0])]+''' </h1>
                <button> <a href='#' onclick='history.go(-1)'>Back</a> </button> <br><br>
                <img src='''+URL+'''> <br>
                ''')
    
    return ('''
            <form method="post">
            Paste url concrete cracks: <br>
            URL: <input type="text" name="url"> <br> <br>
            <input type="submit" value="Submit"> <br>
            </form>
            <br><br>
            <a href="https://www.google.com/search?q=concrete+crack+images&sxsrf=ALeKk01yyQFqps4vcbwaI8I3z6tIubiaNw:1590330445607&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjUq6TK2szpAhVCzqYKHTMQAEkQ_AUoAXoECAsQAw&biw=2064&bih=1054", target = "_blank">search for cracked concrete images</a>
            <br>
            <a href="https://www.google.com/search?q=plain+concrete&tbm=isch&ved=2ahUKEwiYq4Tf2szpAhVYt6QKHXWmAScQ2-cCegQIABAA&oq=plain+concrete&gs_lcp=CgNpbWcQAzIECCMQJzIECAAQEzIECAAQEzIECAAQEzIECAAQEzIECAAQEzIECAAQEzIECAAQEzIECAAQEzIECAAQE1CnOVipOmDMO2gAcAB4AIABXIgBtgGSAQEymAEAoAEBqgELZ3dzLXdpei1pbWc&sclient=img&ei=eYTKXtiKB9jukgX1zIa4Ag&bih=1054&biw=2064", target = "_blank">search for plain concrete images</a>
            <br>
            <br> 
            <br>           
            <iframe src="https://youtube.com/embed/NafEYsmeBGU" width="853" height="480" frameborder="0" allowfullscreen></iframe>
            ''')
            
            
            
def main():
    load()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    main()
        
        
        
        
                
        

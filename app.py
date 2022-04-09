#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from keras.models import load_model
from PIL import Image #use PIL
import numpy as np


# In[2]:


app = Flask(__name__)


# In[3]:


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(filename)
        file = open(filename,"r")
        model = load_model("CNN")
        img = Image.open(filename) #rose = 3, sunflower = 4, tulip 5
        img = img.resize((100,100))
        img = np.asarray(img, dtype="float32") #need to transfer to np to reshape
        img = img.reshape(1, img.shape[0], img.shape[1], img.shape[2]) #rgb to reshape to 1,100,100,3
        img.shape
        pred=model.predict(img)
        return(render_template("index1.html", result=str(pred)))
    else:
        return(render_template("index1.html", result="2"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:





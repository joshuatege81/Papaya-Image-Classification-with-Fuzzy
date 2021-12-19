from flask import Flask, request , flash,redirect, url_for, render_template,jsonify
from fuzzy import fuzzy
from hemo import penentu
from obj_init import obj_size
from bobot import bobot_proc
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["UPLOAD_FOLDER"] = './uploads/'

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        
        if 'file' not in request.files:
            print("no file!")
            return redirect(request.url)

        file = request.files['file']
      
        if file.filename == '':
            print("no selected file")
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            saved_location = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(saved_location)

            penentu([saved_location])
            values = obj_size(saved_location)

            bobot_result = bobot_proc(values)
            fuzzy_result = fuzzy()
            # return result(fuzzy_result)
            
            json_fuzzy = {"result":fuzzy_result,'result1':bobot_result}
            return jsonify(json_fuzzy)

    return render_template('predict.html')
    
# @app.route("/result", methods=['GET'])
# def result(fuzzy_result):
#     render_html = f"<h1>Hasil Prediksi {fuzzy_result}</h1>"
#     return render_html, a

app.run()
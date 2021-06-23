from flask import Flask, request, render_template 
import pickle
import numpy as np

randomForest = 'rf_model.pkl'
classifier = pickle.load(open(randomForest, 'rb'))

# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
@app.route('/')
def home():
    return render_template ('index.html')

@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        glucose = request.form['glucose']
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        age = request.form['age']
        bmi = weight / (height**2)
        
        user_data = np.array([[glucose,bmi, age]])
        new_prediction = classifier.predict(user_data)

        return render_template('result.html', prediction = new_prediction)

if __name__ == '__main__':

       app.run(threaded=True, port=5500)
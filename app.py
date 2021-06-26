from flask import Flask, request, render_template
import pickle
import numpy as np
import smtplib
from config import key

randomForest = 'rf_model.pkl'
classifier = pickle.load(open(randomForest, 'rb'))

def send_alert_email(subject, text, mail):
    senderEmail = 'healthdiabetesapp@gmail.com'
    message = 'Subject: {}\n\n{}'.format(subject, text)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(senderEmail, key)
    print("Log: Login success to send email")
    server.sendmail(senderEmail, mail, message)
    print("emails have been sent")
    

# create instance of Flask app
app = Flask(__name__)



# create route that renders index.html template
@app.route('/')
def home():
    return render_template ('index.html')
# route for getting prediction results based on form inputs
@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        mail = request.form['email']
        glucose = request.form['glucose']
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        age = request.form['age']
        bmi = weight / (height**2)
        name = request.form['name']
        
        user_data = np.array([[glucose,bmi, age]])
        new_prediction = classifier.predict(user_data)
    if new_prediction == 1:
        text1= 'Hello, {}, we regret to inform you that, according to your information you have a very high risk of having or getting diabetes.'.format(name) 
        
    else:
        text1= 'Hello, {}, we are happy to inform you that according to your information you have a low risk of having or gettin diabetes.'.format(name)

    send_alert_email(subject = "Diabetes Result", text = text1, mail = mail )

    return render_template('result.html', prediction = new_prediction, nameVariable = name)


if __name__ == '__main__':

       app.run(threaded=True, port=5500)
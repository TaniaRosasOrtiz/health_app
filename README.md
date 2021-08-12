# HEALTH APP | Diabetes Risk Identifier

TEAM MEMBERS

* Abigail Guzmán
* Carlos Valverde
* Daniela Marroquín 
* Elena Sánchez 
* Joyce Casiano
* Marco Vinicio Cid
* Rodrigo Cid
* Tania Rosas

# APP DESCRIPTION

Our main objective is to develop an app that helps the user to identify their risk of having or getting diabetes according to their age, their body mass index (BMI) and their glucose level. 

# CONSTRUCTION OF THE APP 

The first step we took was to analyze several factors that we found out that could determine strongly the prediction of having or getting diabetes. Those factors were:

     *Pregnancies

     *Glucose Level
  
     *Blood Pressure
  
     *Insulin Level
  
     *Body Mass Index (BMI)
  
     *Age

After we analyzed those factors we came to the conclusion that age, BMI and glucose level were the most important factors that could determine if a user has a low or high risk of being a diabetic.  

The analysis made can be found in the jupyter notebook data_exploration.ipynb 

The second step was to build the backend of the app where we trained a Random Forest Model with a dataset of 2000 entries in order to be able to get a prediction for our users. The model can be found in the script RandomForest_model.py and the dataset can be obtained from Kaggle in the following link https://www.kaggle.com/vikasukani/diabetes-data-set.

The final step was to build the frontend in HTML with Bootstrap. The frontend consists of a form that should be filled by the user with these data: 
      
      * Name
      
      * Email
      
      * Phone
      
      * Glucose Level
      
      * Weight
      
      * Height 
      
      * Age
      
After the user fills the form the prediction is made and the user is directed to a new page where the results are displayed.

The form code can be found in the index.html file and the results code can be found in the result.html. The app was created with Flask in the app.py file. 

Finally we deployed our app using Heroku, the deployement can be found in the following link: https://health-diabetes-app.herokuapp.com/

The site is best viewed using the current browser version of Firefox, Chrome and Safari or Internet Explorer 10 and higher.


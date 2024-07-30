from flask import Flask, redirect, render_template, request
import pandas as pd
import joblib
import os
import numpy as np
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/Dry_Eyes_Detection"
mongo = PyMongo(app)


def classify(inputs):
    try:
        new_data = np.array(inputs).reshape(1, -1)

        model_folder = r"C:\Users\Lenovo\Desktop\DRY_EYES_STAGE_DETECTION\models"
        model_file = "best_model.pkl"
        model_path = os.path.join(model_folder, model_file)
        model = joblib.load(model_path)

        prediction = model.predict(new_data)
        return prediction
    except Exception as e:
        print(f"Error in classification: {e}")
        return None


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            name=str(request.form.get("name"))
            age = float(request.form.get("Age"))
            gender = int(request.form.get('gender'))
            hours = int(request.form.get('hours'))
            working = int(request.form.get('working'))
            painful = int(request.form.get('painful'))
            gritty = int(request.form.get('gritty'))
            sensitive = int(request.form.get('sensitive'))
            TV = int(request.form.get('TV'))
            ac = int(request.form.get('ac'))
            humidity = int(request.form.get('humidity'))
            windy = int(request.form.get('windy'))
            driving = int(request.form.get('driving'))
            blurred = int(request.form.get('blurred'))
            poor = int(request.form.get('poor'))
            read = int(request.form.get('reading'))

            p = classify([age, gender, hours, sensitive, gritty, painful, blurred,
                          poor, read, driving, working, TV, windy, humidity, ac])
            
            

            if int(p[0]) == 0:
                    pr = "Normal eye condition"
            elif int(p[0]) == 1:
                    pr = "Mild dry eye condition"
            elif int(p[0]) == 2:
                    pr = "Moderate dry eye condition"
            else:
                    pr = "Severe dry eye condition"
            if p is not None:
                mongo.db.New_data.insert_one({
                    'name':name,'age': age, 'gender': gender, 'hours': hours, 'sensitive': sensitive,
                    'gritty': gritty, 'painful': painful, 'blurred': blurred,
                    'poor': poor, 'read': read, 'driving': driving,
                    'working': working, 'TV': TV, 'windy': windy,
                    'humidity': humidity, 'ac': ac,'prediction':pr
                })

            return render_template('result.html', prediction=pr)
        except Exception as e:
            print(f"Error in form submission: {e}")
            return render_template('index.html', prediction="An error occurred. Please try again.")

    return render_template('index.html', prediction=None)


if __name__ == "__main__":
    app.run(debug=True)

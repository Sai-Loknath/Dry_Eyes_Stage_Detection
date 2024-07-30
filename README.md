# Dry_Eyes_Stage_Detection
This project detects dry eye stages using machine learning models. It involves data preprocessing, model training with hyperparameter tuning, and deployment using a Flask web application integrated with MongoDB.

Project Overview
The project uses various machine learning models to classify dry eye conditions based on user input features. The best-performing model is selected and saved as a pickle file for deployment.

Installation
To set up the project, follow these steps
1)Clone the repository
2)Create a virtual environment
3)Install the dependecies

Best Model: SVM
Among the models evaluated (Decision Tree, Random Forest, Gradient Boosting, and SVM), the SVM model achieved the highest accuracy. The SVM model's hyperparameters were tuned using GridSearchCV to optimize its performance. The best model is saved as a pickle file (best_model.pkl), which can be downloaded and used for predictions.

##Flask Web Application
The Flask web application allows users to input their data and get predictions for their dry eye condition. The application workflow is as follows:
1)Form Submission:
Users input their data (age, gender, symptoms, etc.) through a form on the web page.
2)Data Processing and Prediction:
The input data is processed and passed to the trained SVM model, which predicts the dry eye stage.
3)MongoDB Integration:
The user input data and the prediction results are stored in a MongoDB database for future reference.
Feel free to download the best_model.pkl file and integrate it into your applications for dry eye stage detection.

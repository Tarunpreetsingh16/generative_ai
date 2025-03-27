Bank Customer Exit Prediction App
This project is a basic web application that predicts whether a bank customer is likely to exit or not. The app is built using Streamlit and leverages an Artificial Neural Network (ANN) model for predictions. It is designed as a learning exercise to explore the fundamentals of ANN and its application in real-world scenarios.

Features
User Input: Users can input customer details such as credit score, geography, gender, age, tenure, balance, number of products, credit card ownership, active membership status, and estimated salary.
Data Preprocessing: The app preprocesses the input data by encoding categorical variables (e.g., geography and gender) and scaling numerical features.
Prediction: The ANN model predicts whether the customer is likely to exit the bank.
Interactive UI: Built with Streamlit for an easy-to-use and interactive interface.
How to Access the App
The app is hosted online and can be accessed at:

https://generativeai-ryos32mrkvv4ue2rh4ys7u.streamlit.app/

Project Structure
How It Works
Input Data: Users provide customer details through the Streamlit interface.
Data Encoding and Scaling:
Geography is one-hot encoded using a pre-trained encoder.
Gender is label-encoded using a pre-trained encoder.
Numerical features are scaled using a pre-trained scaler.
Prediction: The preprocessed data is passed to the ANN model, which outputs the likelihood of the customer exiting.
Output: The app displays the prediction result to the user.
Installation and Running Locally
To run the app locally, follow these steps:

Clone the repository:

Install the required dependencies:

Run the Streamlit app:

Open the app in your browser at http://localhost:8501.

Learning Objectives
This project was created as a learning exercise to understand:

Data preprocessing techniques (e.g., encoding, scaling).
Building and training an Artificial Neural Network using TensorFlow/Keras.
Saving and loading machine learning models and preprocessing objects.
Deploying a machine learning model as a web application using Streamlit.
Acknowledgments
Streamlit: For providing an easy-to-use framework for building interactive web apps.
Scikit-learn: For preprocessing tools like encoders and scalers.
TensorFlow/Keras: For building and training the ANN model.
Future Improvements
Enhance the ANN model for better accuracy.
Add more features to the app, such as visualizations of predictions and model performance.
Deploy the app on a custom domain.

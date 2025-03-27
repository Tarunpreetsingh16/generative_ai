### Bank Customer Exit Prediction App
This project is a basic web application that predicts whether a bank customer is likely to exit or not. The app is built using Streamlit and leverages an Artificial Neural Network (ANN) model for predictions. It is designed as a learning exercise to explore the fundamentals of ANN and its application in real-world scenarios.

## Features

User Input: Users can input customer details such as credit score, geography, gender, age, tenure, balance, number of products, credit card ownership, active membership status, and estimated salary.
Data Preprocessing: The app preprocesses the input data by encoding categorical variables (e.g., geography and gender) and scaling numerical features.
Prediction: The ANN model predicts whether the customer is likely to exit the bank.
Interactive UI: Built with Streamlit for an easy-to-use and interactive interface.

How to Access the App
The app is hosted online and can be accessed at:

https://generativeai-ryos32mrkvv4ue2rh4ys7u.streamlit.app/

## How It Works

1. Input Data: Users provide customer details through the Streamlit interface.

2. Data Encoding and Scaling:  
   2.1. Geography is one-hot encoded using a pre-trained encoder.  
   2.2. Gender is label-encoded using a pre-trained encoder.  
   2.3. Numerical features are scaled using a pre-trained scaler.  

4. Prediction: The preprocessed data is passed to the ANN model, which outputs the likelihood of the customer exiting.
5. Output: The app displays the prediction result to the user.

## Installation and Running Locally

To run the app locally, follow these steps:

1. Clone the repository:
```
git clone <repository-url>
cd <repository-folder>
```

2. Install the required dependencies:
```
pip install -r requirements.txt
```

3. Run the Streamlit app:
```
streamlit run index.py
```

4. Open the app in your browser at `http://localhost:8501`.

### Learning Objectives

This project was created as a learning exercise to understand:

1. Data preprocessing techniques (e.g., encoding, scaling).
2. Building and training an Artificial Neural Network using TensorFlow/Keras.
3. Saving and loading machine learning models and preprocessing objects.
4. Deploying a machine learning model as a web application using Streamlit.
   
## Acknowledgments

1. Streamlit: For providing an easy-to-use framework for building interactive web apps.
2. Scikit-learn: For preprocessing tools like encoders and scalers.
3. TensorFlow/Keras: For building and training the ANN model.

## Future Improvements

1. Enhance the ANN model for better accuracy.
2. Add more features to the app, such as visualizations of predictions and model performance.

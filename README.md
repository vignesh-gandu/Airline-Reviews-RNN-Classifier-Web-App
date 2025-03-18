# Airline Customer Sentiment Analysis 

Flask Web App to classify customer feedback as postive or negative. 

![Image](https://github.com/user-attachments/assets/ce9b2b99-7c6d-4404-aff2-87cc09e1277a)
![Image](https://github.com/user-attachments/assets/21fee53b-f5b6-4768-a35d-fa0d753b2992)

Utilizing Python, TensorFlow (RNN Model), Flask, Pandas 

# Data Set
Twitter US Airline Sentiment from Kaggle
[Dataset](https://www.kaggle.com/crowdflower/twitter-airline-sentiment)

# Getting Started
Python3 needs to be installed on local machine. 

How to run Flask Web App Locally (Mac): 

1. Copy or download the repository to your local machine.
2. Navigate to the Customer-Feedback-Sentiment-Analysis-using-LSTM folder and use the terminal command to set up a virtual Python environment. Replace `flaskapp` with any name of your choice for the environment:
    ```bash 
     python3 -m venv flaskapp
    ```
3. Use this command to activate the virtual environment:
    ```bash                 
    source flaskapp/bin/activate
    ```
4. Next, execute the command `pip install -r requirements.txt` to install the required dependencies.  
   If you encounter an error on macOS related to permissions, use:
   ```bash
   pip install -r requirements.txt
5. Now, configure the `FLASK_APP` variable to `app.py` and set `FLASK_ENV` to `development` using the following commands:
    ```bash
    export FLASK_APP=app.py
    ```
    ```bash
    export FLASK_ENV=development
    ```
6. Lastly, start the application by running the command:
    ```bash
    python3 -m flask run
    ```
7. The terminal will display the local URL and port where the application is hosted. For instance, it could show `http://127.0.0.1:5000/`. Open this address in a web browser to access the app.

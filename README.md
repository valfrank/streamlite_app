# Airline passenger satisfaction 
This repository provides a project to deploy a machine learning model as a web application using the Streamlit framework.

**It covers various stages**
   - exploratory data analysis, 
   - model development, 
   - building a web service.

**Check out the live [app](https://airline-satisfaction.streamlit.app/) here!**

## Project structure
    .
    ├── EDA & model train.ipynb                   
    ├── data
    │   ├── col_transformer.pkl          # Fit transformer for preprocessing
    │   ├── model.pkl                    # Trained CatBoostClassifier
    │   └── intro.jpg
    ├── app.py                     
    ├── model.py                   
    ├── .streamlit
    │   └── config.toml              
    ├── requirements.txt
    ├── LICENSE
    └── README.md

## Run locally

        $ python -m venv venv
        $ source venv/bin/activate
        $ pip install -r requirements.txt
        $ streamlit run app.py
Open http://localhost:8501 to view the app.

import pandas as pd
import pickle


def load_from_pkl(path='data', file_name='model'):
    """ Load saved model as pickle file"""

    model = pickle.load(open(f'{path}/{file_name}.pkl', 'rb'))
    return model


def predict_on_input(df: pd.DataFrame):
    """ Load model and returns prediction and probability"""

    model = load_from_pkl()
    pred = model.predict(df)
    return pred


def preprocess_data(X: pd.DataFrame, test=True):
    """ Function for scaling and encoding data"""

    col_transformer = load_from_pkl(path='data', file_name='col_transformer')
    X = col_transformer.transform(X)
    return X

import pandas as pd
import streamlit as st
from PIL import Image
from model import preprocess_data, predict_on_input
import time


def process_main_page():
    show_main_page()
    df = process_side_bar_inputs()
    df1 = process_rating_inputs()
    prediction(df, df1)


def show_main_page():
    image = Image.open('data/intro.jpg')
    st.set_page_config(
        layout="wide",
        initial_sidebar_state="auto",
        page_title="Airline customer satisfaction",
        page_icon=":flight_arrival:",

    )
    st.write(
        """
        # Airline customer satisfaction
        Сhecking whether the client liked the flight based on a survey
        """
    )
    st.image(image)


def process_side_bar_inputs():
    """Function process sidebar inputs and return DataFrame"""

    st.sidebar.header('Personal information')
    gender = st.sidebar.radio('Gender', ['Male', 'Female'])
    age = st.sidebar.number_input('Age', 0, 100)
    loyalty = st.sidebar.radio('Do you have loyal card?', ['Loyal Customer', 'disloyal Customer'])
    typefl = st.sidebar.selectbox('Purpose of the trip', ['Business travel', 'Personal Travel'])
    classfl = st.sidebar.selectbox('Class', ['Eco', 'Eco Plus', 'Business'])
    distance = st.sidebar.slider('Flight distance', 0, 5000)
    delayarr = st.sidebar.slider('Departure delay, min', 0, 500)
    delaydep = st.sidebar.slider('Arrival delay, min', 0, 500)

    df = pd.DataFrame({'gender': [gender], 'age': [age], 'customer_type': [loyalty], 'type_of_travel': [typefl],
                       'flight_distance': [distance], 'departure_delay_in_minutes': [delayarr],
                       'arrival_delay_in_minutes': [delaydep], 'class': [classfl]
                       })
    return df


def process_rating_inputs():
    """Function process page inputs and return DataFrame"""

    st.write('## Please rate your flight 📋')
    col1, col2 = st.columns(2)
    df1 = pd.DataFrame({'inflight_wifi_service': [col1.radio('Wi-Fi', [1, 2, 3, 4, 5], horizontal=True)],
                        'departure_arrival_time_convenient': [
                            col1.radio('Arrival time', [1, 2, 3, 4, 5], horizontal=True)],
                        'ease_of_online_booking': [col1.radio('Online booking', [1, 2, 3, 4, 5], horizontal=True)],
                        'gate_location': [col1.radio('Gate location', [1, 2, 3, 4, 5], horizontal=True)],
                        'food_and_drink': [col1.radio('Food & drink', [1, 2, 3, 4, 5], horizontal=True)],
                        'online_boarding': [col1.radio('Online boarding', [1, 2, 3, 4, 5], horizontal=True)],
                        'seat_comfort': [col1.radio('Seat comfort', [1, 2, 3, 4, 5], horizontal=True)],
                        'inflight_entertainment': [
                            col2.radio('Inflight entertainment', [1, 2, 3, 4, 5], horizontal=True)],
                        'on_board_service': [col2.radio('On board service', [1, 2, 3, 4, 5], horizontal=True)],
                        'leg_room_service': [col2.radio('Leg room service', [1, 2, 3, 4, 5], horizontal=True)],
                        'baggage_handling': [col2.radio('Baggage handling', [1, 2, 3, 4, 5], horizontal=True)],
                        'checkin_service': [col2.radio('Checkin service', [1, 2, 3, 4, 5], horizontal=True)],
                        'inflight_service': [col2.radio('Inflight service', [1, 2, 3, 4, 5], horizontal=True)],
                        'cleanliness': [col2.radio('Cleanliness', [1, 2, 3, 4, 5], horizontal=True)], })
    return df1


def prediction(df, df1):
    """Function to preprocess inputs and predict"""

    if st.button('Predict!'):
        with (st.spinner('In progress..')):
            time.sleep(1)
            final = pd.concat([df, df1], axis=1)
            X = preprocess_data(final)
            pred = predict_on_input(X)
            if pred == 1:
                st.success('The customer is happy! 🤗')
            elif pred == 0:
                st.error('The customer is not happy 😞')
            else:
                st.error('Something went wrong...')


if __name__ == "__main__":
    process_main_page()

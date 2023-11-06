import streamlit as st
import requests


def hit_api_gateway(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses

        st.success("API request successful!")
        st.write("Response:")
        st.write(response.json())  # Assumes the response is in JSON format

    except requests.exceptions.RequestException as e:
        st.error(f"Error making API request: {e}")


# Streamlit UI
st.title("API Gateway GET Request Example")

# Input field for API URL
api_url = st.text_input("Enter API Gateway URL")

# Button to trigger the API request
if st.button("Hit API Gateway"):
    if api_url:
        hit_api_gateway(api_url)
    else:
        st.warning("Please enter an API URL.")
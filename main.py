import requests
import streamlit as st

import boto3
from botocore.exceptions import NoCredentialsError

st.set_page_config(
    page_title="AIA Insurance Hackathon",
    page_icon="🧑‍💻",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': 'https://github.com/aia-hackathon/team-27',
        'Get Help': "https://github.com/aia-hackathon/team-27",
        'Report a bug': "https://github.com/aia-hackathon/team-27",
    }

)

st.title("AIA Insurance Hackathon - Team 27")
st.subheader("Please fill this form to start your :blue[insurance journey] :smiley:", divider="rainbow")
form = st.form("user-details")
name = form.text_input("Name")
gender = form.radio("Gender", ["Male", "Female"])
age = form.number_input("Age", format="%d", step=1)
occupation = form.text_input("Occupation")
type_of_policy = form.selectbox("Type of Policy", ["Life", "Health", "Auto"])
duration_of_policy = form.selectbox("Duration of Policy", [1, 3, 5, 10, 15])
no_of_insured_members = form.number_input("No. of Insured Members", format="%d", step=1, max_value=10,  min_value=1)
coverage_amount = form.number_input("Coverage Amount", format="%d", step=1)
policy_holder_type = form.selectbox("Policy Holder Type", ["Individual", "Company"])
salary = form.number_input("Salary", format="%d", step=1)
policy_holder_location = form.text_input("Policy Holder Location")
medical_history = form.checkbox("Medical History")
medical_history_details = form.text_area("Medical History Details")
blood_glucose_level = form.number_input("Blood Glucose Level", format="%d", step=1)
hba1c_level = form.number_input("HbA1c Level",  format="%d", step=1)
ldl_cholesterol_level = form.number_input("LDL Cholesterol Level",  format="%d", step=1)
lifestyle = form.selectbox("Lifestyle", ["smoker", "non-smoker"])
documents = form.file_uploader("Upload Documents", accept_multiple_files=True)
premium_calculation_explanation = form.checkbox("Do you want to explain how the premium was calculated?")
submit_button = form.form_submit_button("Submit")


def upload_to_s3(file_content, bucket_name, object_name):
    try:
        s3_client = boto3.client('s3')
        s3_client.put_object(Body=file_content, Bucket=bucket_name, Key=object_name)
        st.success("File uploaded successfully!")
    except NoCredentialsError:
        st.error("Credentials not found. Please check your credentials and try again.")
    except Exception as e:
        st.error(f"Error uploading file: {e}")


def hit_api_gateway(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses

        st.success("API request successful!")
        st.write("Response:")
        response_body = response.json()["body"]
        st.write("Response:", response_body)
    except requests.exceptions.RequestException as e:
        st.error(f"Error making API request: {e}")


def generate_api_url():
    # generate api url based on form inputs and return it
    base_url = "https://5aqtmakxph.execute-api.us-east-1.amazonaws.com/Testing?foo=200&"
    query_params_dict = {
        "Age": age,
        "CoverageAmt": coverage_amount,
        "CoverageYear": duration_of_policy,
        "Gender": gender,
        "Occupation": occupation,
        "Salary": salary,
        "GlucoseLevel": blood_glucose_level,
        "HbA1cLevel": hba1c_level,
        "LDLLevel": ldl_cholesterol_level,
        "lifestyle": lifestyle
    }
    query_params = "&".join(f"{key}={value}" for key, value in query_params_dict.items())
    return base_url + query_params


if documents:
    st.write("Uploaded Documents:")
    for doc in documents:
        st.write(f"Name: {doc.name}")
        st.write(f"Type: {doc.type}")
        st.write(f"Size: {doc.size} bytes")
        # Specify S3 bucket and object name
        bucket_name = "team27operation"
        if submit_button:
            object_name = doc.name
            file_content = doc.read()
            upload_to_s3(file_content, bucket_name, object_name)
            api_url = generate_api_url()
            st.write(api_url)
            hit_api_gateway(api_url)

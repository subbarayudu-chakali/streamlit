import streamlit as st
# import pandas as p

st.set_page_config(
    page_title="AIA Insurance Hackathon",
    page_icon="🧑‍💻",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items= {
        'About': 'https://github.com/aia-hackathon/team-27',
        'Get Help': "https://github.com/aia-hackathon/team-27",
        'Report a bug': "https://github.com/aia-hackathon/team-27",
    }

)


st.title("AIA Insurance Hackathon - Team 27")
st.header("Predicting the Insurance Premium", divider='rainbow')

st.file_uploader("Upload Claim Documents")

st.markdown("WE ❤️️ A 👁️")

# create a form for the user to enter the data

st.header("Validate the details of the policy holder")
form = st.form("my_form")
name = form.text_input("Name")
gender = form.radio("Gender", ["Male", "Female"])
age = form.number_input("Age")
occupation = form.text_input("Occupation")
type_of_policy = form.selectbox("Type of Policy", ["Life", "Health", "Travel"])
duration_of_policy = form.selectbox("Duration of Policy", [1, 3, 5, 10])
no_of_insured_members = form.number_input("No. of Insured Members")
policy_holder_type = form.selectbox("Policy Holder Type", ["Individual", "Company"])
policy_holder_location = form.text_input("Policy Holder Location")
medical_history = form.checkbox("Medical History")
submit_button = form.form_submit_button("Submit")

st.checkbox("Do you want to explain how the premium was calculated?")
st.button("Predict Premium")

st.info('Please Check below tabs for more details')

tab1, tab2, tab3, tab4, tab5 = st.tabs(["About", "Architecture", "Data Extraction", "Prediction", "Explainability"])

with tab1:
    st.write("This project was created by Team 27 as part of AIA Insurance Hackathon")
    st.write("The project is based on the AI-based insurance premium prediction model")

with tab2:
    st.write("Architecture")

with tab3:
    st.write("Data Extraction")
    st.write("The process begins once the user uploads the documents in the portal")

with tab4:
    st.write("Prediction")

with tab5:
    st.write("Explainability")

code = '''def hello():
    print("Hello, Streamlit!")
    print("Hello, Streamlit!")
    print("Hello, Streamlit!")
    print("Hello, Streamlit!")'''
st.code(code, language='python', line_numbers=True)

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
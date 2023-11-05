import streamlit as st
import pandas as pd

# Set the title of the page
st.title("Full Stack Java Developer Portfolio")

# Add a header section with personal information
st.header("Personal Information")
st.write("Name: John Doe")
st.write("Email: johndoe@email.com")
st.write("Phone: 555-555-5555")

# Add a section for education
st.header("Education")
df_education = pd.DataFrame([
    {"Institution": "University of California, Berkeley", "Degree": "Bachelor of Science in Computer Science", "Graduation Date": "May 2018"},
    {"Institution": "Stanford University", "Degree": "Master of Science in Computer Science", "Graduation Date": "June 2020"}
])
st.dataframe(df_education)

# Add a section for certifications
st.header("Certifications")
df_certifications = pd.DataFrame([
    {"Certification": "Oracle Certified Java Programmer", "Issuing Organization": "Oracle", "Date": "August 2018"},
    {"Certification": " AWS Certified Solutions Architect - Associate", "Issuing Organization": "Amazon Web Services", "Date": "November 2019"}
])
st.dataframe(df_certifications)

# Add a section for experience
st.header("Experience")
df_experience = pd.DataFrame([
    {"Company": "ABC Corporation", "Job Title": "Software Engineer", "Start Date": "January 2019", "End Date": "Present", "Description": "Worked on several projects involving Spring Boot and Android Studio."},
    {"Company": "XYZ Inc.", "Job Title": "Senior Software Engineer", "Start Date": "June 2018", "End Date": "December 2018", "Description": "Led a team of developers in building a web application using Spring MVC and JavaScript."},
    {"Company": "MNO Ltd.", "Job Title": "Full Stack Java Developer", "Start Date": "January 2017", "End Date": "June 2018", "Description": "Developed a RESTful API using Spring Boot and created a frontend using AngularJS."}
])
st.dataframe(df_experience)

# Add a section for tools and technologies
st.header("Tools and Technologies")
df_tools = pd.DataFrame([
    {"Tool/Technology": "Java", "Proficiency Level": "Expert"},
    {"Tool/Technology": "Python", "Proficiency Level": "Intermediate"},
    {"Tool/Technology": "JavaScript", "Proficiency Level": "Beginner"},
    {"Tool/Technology": "Spring Framework", "Proficiency Level": "Expert"},
    {"Tool/Technology": "Android Studio", "Proficiency Level": "Intermediate"},
    {"Tool/Technology": "AWS", "Proficiency Level": "Associate"}
])
st.dataframe(df_tools)

# Add a section for projects
st.header("Projects")
df_projects = pd.DataFrame([
    {"Project Name": "MyFitnessApp", "Description": "A fitness tracking app built using Spring Boot and Android Studio", "Link": "https://github.com/johndoe/myfitnessapp"},
    {"Project Name": "BookStore", "Description": "An e-commerce website built using Spring MVC and JavaScript", "Link": "https://github.com/johndoe/bookstore"},
    {"Project Name": "WeatherApp", "Description": "A weather application built using Spring Boot and ReactJS", "Link": "https://github.com/johndoe/weatherapp"}
])
st.dataframe(df_projects)

# Add a section for social media links

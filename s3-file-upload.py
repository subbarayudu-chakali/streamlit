import streamlit as st
import boto3
from botocore.exceptions import NoCredentialsError
from io import BytesIO


# Function to upload file to S3
def upload_to_s3(file_content, s3_bucket_name, s3_object_name):
    try:
        s3_client = boto3.client('s3')

        # Upload file to S3 bucket
        s3_client.put_object(Bucket=s3_bucket_name, Key=s3_object_name, Body=file_content)
        st.success("File uploaded successfully!")

    except NoCredentialsError:
        st.error("Credentials not found. Please check your credentials and try again.")
    except Exception as e:
        st.error(f"Error uploading file: {e}")

# Streamlit UI
st.title("S3 File Uploader")

# File upload widget
files = st.file_uploader("Choose files", accept_multiple_files=True)

if files:
    st.write("Files Details:")
    for file in files:
        # Display file details
        st.write(f"Name: {file.name}")
        st.write(f"Type: {file.type}")
        st.write(f"Size: {file.size} bytes")

        # Specify S3 bucket and object name
        bucket_name = "ai-insurance-docs"

        # Upload the file to S3 on button click
        if st.button("Upload to S3"):
            for file in files:
                object_name = file.name
                file_content = file.read()
                upload_to_s3(file_content, bucket_name, object_name)


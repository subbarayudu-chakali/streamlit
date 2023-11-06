import streamlit as st

import boto3

st.title('Send Notification to mail')
st.write('This is a simple web app to send notification to mail')
st.text_input('Enter your mail id', key='mail_id')


# st.write('Notification sent to', st.session_state.mail_id)

def send_notification_to_mail(mail_id):
    st.write('Sending notification to', mail_id)
    # code to send notification to the mail id
    sns_client = boto3.client('sns')
    # send notification to the mail id
    # create a topic
    # create a subscription to the topic
    # send notification to the topic
    sns_topic_name = 'mail_notification'
    sns_topic_arn = sns_client.create_topic(Name=sns_topic_name)['TopicArn']
    # subscribe to the topic
    sns_client.subscribe(TopicArn=sns_topic_arn, Protocol='email', Endpoint=mail_id)
    # send notification to the topic
    response = sns_client.publish(TopicArn=sns_topic_arn, Message='Hello, World!')
    return None


if st.button('Send notification') and 'mail_id' in st.session_state and st.session_state.mail_id != '':
    #st.session_state.mail_id = st.session_state.mail_id.strip()
    if st.session_state.mail_id == '':
        st.error('Please enter a valid mail id')
    if '@' not in st.session_state.mail_id:
        st.error('Please enter a valid mail id')
    # send notification to the mail id
    send_notification_to_mail(st.session_state.mail_id)
    st.write('Notification sent to', st.session_state.mail_id)

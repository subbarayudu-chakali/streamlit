import streamlit as st

st.header("Button")
if st.button("Press me") :
    st.write("why hello there")
else:
    st.write("goodbye")
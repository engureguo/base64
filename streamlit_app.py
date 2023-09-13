：

import streamlit as st

# Page title
st.title("Base64 Encoder/Decoder")

# Page header
st.header("Welcome to the Base64 Encoder/Decoder")

# Main page content
input_data = st.text_input("Enter the string to be encoded/decoded")

# Encoding button
if st.button("Encode"):
    encoded_data = input_data.encode('base64', 'strict')
    st.write(encoded_data)

# Decoding button
if st.button("Decode"):
    decoded_data = input_data.decode('base64', 'strict')
    st.write(decoded_data)

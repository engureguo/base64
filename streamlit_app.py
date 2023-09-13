import streamlit as st
import base64


# Page title
st.title("Base64 Encoder/Decoder")

# Page header
st.header("Welcome to the Base64 Encoder/Decoder")

# Main page content
input_data = st.text_input("Enter the string to be encoded/decoded")

# Encoding button
if st.button("Encode"):
    encoded_data = base64.b64encode(bytes(input_data, 'utf-8'))
    #encoded_data = input_data.encode('base64', 'strict')
    st.write(encoded_data)

# Decoding button
if st.button("Decode"):
    decoded_data = base64.b64decode(bytes(input_data, 'utf-8'))
    #decoded_data = input_data.decode('base64', 'strict')
    st.write(decoded_data)

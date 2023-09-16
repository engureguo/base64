import streamlit as st
import base64
import urllib.parse
import clipboard

def base64_encode(text):
    try:
        encoded_text = base64.b64encode(text.encode()).decode()
        return encoded_text
    except Exception as e:
        st.error("Wrong process")

def base64_decode(encoded_text):
    try:
        decoded_text = base64.b64decode(encoded_text).decode()
        return decoded_text
    except Exception as e:
        st.error("Wrong process")

def url_encode(text):
    try:
        encoded_text = urllib.parse.quote(text)
        return encoded_text
    except Exception as e:
        st.error("Wrong process")

def url_decode(encoded_text):
    try:
        decoded_text = urllib.parse.unquote(encoded_text)
        return decoded_text
    except Exception as e:
        st.error("Wrong process")

# Base64 Encoding/Decoding Section
st.header("Base64 Encoding/Decoding")

base64_input = st.text_input("Enter text for Base64 encoding/decoding:")
base64_encode_button = st.button("Encode", key="base64_encode")
base64_decode_button = st.button("Decode", key="base64_decode")

if base64_encode_button:
    encoded_text = base64_encode(base64_input)
    if encoded_text:
        st.success(f"Encoded Text: {encoded_text}")
        copy_button = st.button("Copy Encoded Text", key="copy_encoded_text")
        if copy_button:
            clipboard.copy(encoded_text)
            st.success("Encoded Text copied to clipboard!")

if base64_decode_button:
    decoded_text = base64_decode(base64_input)
    if decoded_text:
        st.success(f"Decoded Text: {decoded_text}")
        copy_button = st.button("Copy Decoded Text", key="copy_decoded_text")
        if copy_button:
            clipboard.copy(decoded_text)
            st.success("Decoded Text copied to clipboard!")


# URL Encoding/Decoding Section
st.header("URL Encoding/Decoding")

url_input = st.text_input("Enter text for URL encoding/decoding:")
url_encode_button = st.button("Encode", key="url_encode")
url_decode_button = st.button("Decode", key="url_decode")

if url_encode_button:
    encoded_text = url_encode(url_input)
    if encoded_text:
        st.success(f"Encoded Text: {encoded_text}")
        copy_button = st.button("Copy Encoded Text", key="copy_encoded_text")
        if copy_button:
            clipboard.copy(encoded_text)
            st.success("Encoded Text copied to clipboard!")

if url_decode_button:
    decoded_text = url_decode(url_input)
    if decoded_text:
        st.success(f"Decoded Text: {decoded_text}")
        copy_button = st.button("Copy Decoded Text", key="copy_decoded_text")
        if copy_button:
            clipboard.copy(decoded_text)
            st.success("Decoded Text copied to clipboard!")

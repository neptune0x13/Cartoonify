import streamlit as st

from lib.cartoonify import Cartoonify

cartoonifier = Cartoonify()

st.set_page_config(page_title="Cartoonifier",
                   page_icon="images/favicon.png")

st.header("Cartoonifier")
st.subheader("Here, you can click an image or upload one to cartoonify it!")

camera = st.button(label="Click Picture")
upload = st.file_uploader(label="Upload Picture", type=['jpg', 'png', 'jpeg'])

a = st.camera_input(label="Click Picture")
if a:
    print(a)
    # a = cartoonifier.cartoonify(a)

if upload:
    pass
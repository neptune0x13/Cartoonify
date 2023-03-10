import cv2
import streamlit as st
from lib.cartoonify import Cartoonify

cartoonifier = Cartoonify()

st.set_page_config(page_title="Cartoonifier",
                   page_icon="images/favicon.png")

st.header("Cartoonifier")
st.write("#### Github : https://github.com/neptune0x13/Cartoonify")
st.write("This is a mini app using which you can Cartoonify your Images using OpenCV library.")
st.write("##### Either:")
st.write("###### - Click a picture ")
st.write("###### - Upload a Picture  ")


def cartooner(pic):
    with open('images/tempFile.jpg', 'wb') as f:
        f.write(pic.getvalue())

    cartoonified = cartoonifier.cartoonify("images/tempFile.jpg")
    cv2.imwrite("images/cartoonified.png", cartoonified)

    col1, col2 = st.columns(2)
    with col1:
        st.image("images/tempFile.jpg", caption="Original Image")
    with col2:
        st.image("images/cartoonified.png", caption="Cartoonified Image")

    st.download_button(label="Download Cartoonified Image",
                       data=open("images/cartoonified.png", "rb").read(),
                       file_name="cartoonified.png")


camera = st.checkbox(label="Click Picture")
if camera:
    picture = st.camera_input("Take a picture")
    if picture:
        cartooner(picture)

upload = st.file_uploader(label="Upload Picture", type=['jpg', 'png', 'jpeg'])
if upload:
    cartooner(upload)

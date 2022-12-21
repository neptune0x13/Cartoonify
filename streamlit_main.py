import streamlit as st

from lib.cartoonify import Cartoonify

cartoonifier = Cartoonify()

st.set_page_config(page_title="Cartoonifier",
                   page_icon="images/favicon.png")

st.header("Cartoonifier")
st.subheader("Here, you can click an image or upload one to cartoonify it!")

camera = st.button(label="Click Picture")
if camera:
    pass
upload = st.file_uploader(label="Upload Picture", type=['jpg', 'png', 'jpeg'])
print(type(upload))
if upload:
    open('images/tempFile.jpg', 'wb').write(upload.getvalue())
    cartoonified = cartoonifier.cartoonify("images/tempFile.jpg")
    st.image(cartoonified)
# a = st.camera_input(label="Click Picture")
# if a:
#     print(a)
    # a = cartoonifier.cartoonify(a)

# if upload:
#     pass
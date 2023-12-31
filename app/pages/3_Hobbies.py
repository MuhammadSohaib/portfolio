import streamlit as st
from PIL import Image
from constant import *

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

def load_and_resize_image(image_path, size=(700, 700)):
    img = Image.open(image_path)
    img = img.resize(size, Image.ANTIALIAS)
    return img
        


local_css("app/style/style.css")

st.sidebar.markdown(info['Photo'],unsafe_allow_html=True)


st.title("🫶 Hobbies")


img_1 = load_and_resize_image("app/images/1.jpeg")
img_2 = load_and_resize_image("app/images/2.jpeg")
img_3 = load_and_resize_image("app/images/3.jpeg")
img_4 = load_and_resize_image("app/images/4.jpeg")


# Create two rows with two columns each
col1, col2 = st.columns(2)  # First row
col3, col4 = st.columns(2)  # Second row

with col1:
    st.image(img_1)
    
with col2:
    st.image(img_2)

with col3:
    st.image(img_3)

with col4:
    st.image(img_4)

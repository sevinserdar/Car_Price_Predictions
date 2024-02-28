# import module
import streamlit as st

# Title
st.title("Car Price Predictions")

# Header
st.header("Learn your car price") 

# Subheader
st.subheader("This is a car predictions app")

# Display Images

# import Image from pillow to open images
from PIL import Image
img = Image.open("slideshow-564.jpg")

# display image using streamlit
# width is used to set the width of an image
st.image(img, width=200)

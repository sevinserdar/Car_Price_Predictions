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


# radio button
# first argument is the title of the radio button
# second argument is the options for the radio button
status = st.radio("Select Color: ", ('White', 'Grey', 'Black', 'Red'))

# conditional statement to print 
# Male if male is selected else print female
# show the result using the success function
if (status == 'White'):
	st.success("White")
elif (status == 'Grey'):
    st.success("Grey")
elif (status == 'Black'):
    st.success("Black")
else:
	st.success("Red")


# Selection box

# first argument takes the titleof the selectionbox
# second argument takes options
hobby = st.selectbox("Year: ",
					['Jeep', 'SUV', 'Sports'])

# print the selected hobby
st.write("Your hobby is: ", hobby)



# Text Input

# save the input text in the variable 'name'
# first argument shows the title of the text input box
# second argument displays a default text inside the text input area
name = st.text_input("Enter Your name", "Type Here ...")

# display the name when the submit button is clicked
# .title() is used to get the input text string
if(st.button('Submit')):
	result = name.title()
	st.success(result)

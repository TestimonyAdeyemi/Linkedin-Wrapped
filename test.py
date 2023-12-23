import streamlit as st
import pandas as pd
from PIL import Image, ImageDraw, ImageFont, ImageOps
import openpyxl as excel
import io
import pyperclip
import streamlit as st
from PIL import Image
from streamlit_cropper import st_cropper

def crop():
    st.title("Square Crop Box App")

    uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        #st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        # Get the image as a PIL Image
        image = Image.open(uploaded_file)

        # Set the aspect_ratio parameter to enforce a square crop box
        cropped_image = st_cropper(image, aspect_ratio=(1, 1))

        # Display the cropped image
        st.image(cropped_image, caption="Cropped Image", use_column_width=True)
        print(cropped_image)


                # Specify the file path for the new cropped image
        new_image_path = "path/to/your/new_cropped_image.jpg"

        # Save the cropped image to the new file path
        cropped_image.save(new_image_path)

        # Optionally, display the cropped image
        cropped_image.show()

        # You can do further processing or save the cropped image here
        # For example, you can save it back to a file using cropped_image.save("cropped_image.jpg")

crop()
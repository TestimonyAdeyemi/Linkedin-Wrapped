import streamlit as st
import pandas as pd
from PIL import Image, ImageDraw, ImageFont, ImageOps
import openpyxl as excel
import io
import pyperclip


def credits():
    st.title("Please credit me in your posts")

    # Text to be displayed in the text box
    text_to_copy = "Thanks @Adeyemi Testimony for creating this tool that helped with generating the wrapped graphics"

    # Display the text in a text box
    st.text_area("Text:", value=text_to_copy, height=100)

    # Add a copy button
    copy_button = st.button("Copy Text")

    # If the copy button is clicked, copy the text to the clipboard
    if copy_button:
        pyperclip.copy(text_to_copy)
        st.success("Text copied to clipboard!")


def format_large_number(number):
    if number >= 1e6:  # If the number is a million or more
        return f"{number / 1e6:.1f}M"
    elif number >= 1e3:  # If the number is a thousand or more
        return f"{number / 1e3:.1f}k"
    else:
        return str(number)


def data_analysis():
    ENGAGEMENT = pd.read_excel(excel_file, sheet_name='ENGAGEMENT')
    TOP_POSTS = pd.read_excel(excel_file,sheet_name='TOP POSTS')
    FOLLOWER = pd.read_excel(excel_file, sheet_name='FOLLOWERS')
    DEMOGRAPHICS = pd.read_excel(excel_file, sheet_name='DEMOGRAPHICS')

    ENGAGEMENT['Date'] = pd.to_datetime(ENGAGEMENT['Date'])
    ENGAGEMENT = ENGAGEMENT[(ENGAGEMENT['Date'] >= '01/01/2023') & (ENGAGEMENT['Date'] <= '11/30/2023')]
    ENGAGEMENT['month'] = ENGAGEMENT['Date'].dt.month
    global Total_Impressions
    Total_Impressions = ENGAGEMENT['Impressions'].sum()
    Total_Impressions = format_large_number(Total_Impressions)
    


    global Total_Engagements
    Total_Engagements = ENGAGEMENT['Engagements'].sum()
    Total_Engagements = format_large_number(Total_Engagements) 

 
    global total_followers
    header = FOLLOWER.columns.tolist()
    total_followers = header[-1]
    total_followers = format_large_number(total_followers)


    # Assign the second row as the header
    FOLLOWER.columns = FOLLOWER.iloc[1]
    # Drop the rows above the second row
    FOLLOWER = FOLLOWER[2:].reset_index(drop=True)
    FOLLOWER = FOLLOWER[(FOLLOWER['Date'] >= '01/01/2023') & (FOLLOWER['Date'] <= '11/30/2023')]
    global Total_New_FOLLOWER
    Total_New_FOLLOWER = FOLLOWER['New followers'].sum() 
    Total_New_FOLLOWER = format_large_number(Total_New_FOLLOWER)
    
    
    
    global Top_Locations
    global Top_Job_Titles
    Top_Job_Titles = ""
    Top_Locations = ""
    Top_Industries = ""

    # Check the value based on the "Top Demographics"
    for index, row in DEMOGRAPHICS.iterrows():
        top_demographics = row['Top Demographics']
        value = row['Value']
        if top_demographics == 'Job titles':
            Top_Job_Titles += f"{value}\n"
        elif top_demographics == 'Locations':
            Top_Locations += f"{value}\n"
        elif top_demographics == 'Industries':
            Top_Industries += f"{value}\n"

    # Display or use the result_string as needed with numbered bullets

    Top_Job_Titles = "\n".join([f"{i+1}. {title}" for i, title in enumerate(Top_Job_Titles.split("\n")[:-1])])

    Top_Locations = "\n".join([f"{i+1}. {location}" for i, location in enumerate(Top_Locations.split("\n")[:-1])])

    Top_Industries = "\n".join([f"{i+1}. {industry}" for i, industry in enumerate(Top_Industries.split("\n")[:-1])])



def page1():
 # Load the base image
    
    base_image = Image.open("page1.png")  # Replace with your actual template path

    # Create a drawing object
    draw = ImageDraw.Draw(base_image)

    font_path = "XP-Vosta.ttf"  # Replace with your actual font file path
    font_size = 34

    # Load the specified font
    font = ImageFont.truetype(font_path, font_size)

    # Choose a position for the text
    text_position = (67, 944.7)  # Replace with your desired position for the text

    # Choose a color for the text
    text_color = (255, 255, 255)  # Replace with your desired color for the text

    # Draw the text on the image
    draw.text(text_position, user_name, font=font, fill=text_color)

    # Load the user's avatar image
    global avatar
    avatar = Image.open(user_avatar_path)  # Replace with the actual path to the user's uploaded image

    # Resize the avatar to fit into a circle
    size = (537, 537)  # Set the desired size for the circular avatar
    avatar = avatar.resize(size, Image.LANCZOS)  # Use Image.ANTIALIAS for antialiasing

    # Create a circular mask
    mask = Image.new("L", size, 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.ellipse((0, 0, size[0], size[1]), fill=255)

    # Apply the circular mask to the avatar
    avatar = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
    avatar.putalpha(mask)

    # Choose a position for the circular avatar
    avatar_position = (271, 237)  # Replace with your desired position for the circular avatar

    # Paste the circular avatar onto the base image
    base_image.paste(avatar, avatar_position, avatar)

    # Save or display the resulting image
    page1Edit = base_image.save("page1Edit.png")  # Replace with your desired output path
    #base_image.show()

    
    image_bytes = io.BytesIO()
    base_image.save(image_bytes, format="PNG")

    st.image(base_image, caption="Page1", use_column_width=True)
    # Add a download button for the image

    st.download_button(label="Download Image", data=image_bytes.getvalue(), key="download_button")
    #st.download_button(label="Download Image", data = base_image, key="download_button")



def page2():
    # Load the base image
    base_image = Image.open("page2.png")  # Replace with your actual template path

    # Create a drawing object
    draw = ImageDraw.Draw(base_image)

    font_path = "XP-Vosta.ttf"  # Replace with your actual font file path
    font_size1 = 77
    font1 = ImageFont.truetype(font_path, font_size1)
    text_position1 = (108, 266.8)  # Replace with your desired position for the text
    text_color1 = (255, 255, 255)  # Replace with your desired color for the text


    font_size1 = 77
    font2 = ImageFont.truetype(font_path, font_size1)
    text_position2 = (108, 530.7)  # Replace with your desired position for the text
    text_color1 = (255, 255, 255)  # Replace with your desired color for the text
    
    # Draw the text on the image
    
    draw.text(text_position1, Total_New_FOLLOWER, font=font1, fill=text_color1)
    draw.text(text_position2, total_followers, font=font2, fill=text_color1)
    

    # Load the user's avatar image
    # Replace with the actual path to the user's uploaded image

    # Resize the avatar to fit into a circle
    size = (496, 496) 
    global avatar # Set the desired size for the circular avatar
    avatar = avatar.resize(size, Image.LANCZOS)  # Use Image.ANTIALIAS for antialiasing

    # Create a circular mask
    mask = Image.new("L", size, 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.ellipse((0, 0, size[0], size[1]), fill=255)

    # Apply the circular mask to the avatar
    avatar = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
    avatar.putalpha(mask)

    # Choose a position for the circular avatar
    avatar_position = (493, 265)  # Replace with your desired position for the circular avatar

    # Paste the circular avatar onto the base image
    base_image.paste(avatar, avatar_position, avatar)

    # Save or display the resulting image
    base_image.save("page2Edit.png")  # Replace with your desired output path

    image_bytes = io.BytesIO()
    base_image.save(image_bytes, format="PNG")

    st.image(base_image, caption="Page2", use_column_width=True)
    # Add a download button for the image

    st.download_button(label="Download Image", data=image_bytes.getvalue(), key="download_button2")


def page3():
    # Load the base image
    base_image = Image.open("page3.png")  # Replace with your actual template path

    # Create a drawing object
    draw = ImageDraw.Draw(base_image)

    font_path = "XP-Vosta.ttf"  # Replace with your actual font file path
    font_size1 = 70
    font1 = ImageFont.truetype(font_path, font_size1)
    text_position1 = (108, 265)  # Replace with your desired position for the text
    text_color1 = (255, 255, 255)  # Replace with your desired color for the text


    font_size1 = 70
    font2 = ImageFont.truetype(font_path, font_size1)
    text_position2 = (108, 493)  # Replace with your desired position for the text
    text_color1 = (255, 255, 255)  # Replace with your desired color for the text
    
    # Draw the text on the image
    
    draw.text(text_position1, Total_Impressions, font=font1, fill=text_color1)
    draw.text(text_position2, Total_Engagements, font=font2, fill=text_color1)
    

   # Load the user's avatar image
    
    avatar = Image.open(user_avatar_path)  # Replace with the actual path to the user's uploaded image

    # Resize the avatar to fit into a circle
    size = (496, 496)  # Set the desired size for the circular avatar
    avatar = avatar.resize(size, Image.LANCZOS)  # Use Image.ANTIALIAS for antialiasing

    # Create a circular mask
    mask = Image.new("L", size, 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.ellipse((0, 0, size[0], size[1]), fill=255)

    # Apply the circular mask to the avatar
    avatar = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
    avatar.putalpha(mask)

    # Choose a position for the circular avatar
    avatar_position = (493, 265)  # Replace with your desired position for the circular avatar

    # Paste the circular avatar onto the base image
    base_image.paste(avatar, avatar_position, avatar)

    # Save or display the resulting image
    base_image.save("page3Edit.png")  # Replace with your desired output path
    image_bytes = io.BytesIO()
    base_image.save(image_bytes, format="PNG")
    st.image(base_image, caption="Page3", use_column_width=True)
    # Add a download button for the image
    st.download_button(label="Download Image", data=image_bytes.getvalue(), key="download_button3")





def page4():
    # Load the base image
    base_image = Image.open("page4.png")  # Replace with your actual template path

    # Create a drawing object
    draw = ImageDraw.Draw(base_image)

    font_path = "XP-Vosta.ttf"  # Replace with your actual font file path
    font_size1 = 36
    font1 = ImageFont.truetype(font_path, font_size1)
    text_position1 = (110, 280)  # Replace with your desired position for the text
    text_color1 = (255, 255, 255)  # Replace with your desired color for the text

    # Draw the text on the image
    
    draw.text(text_position1, Top_Locations, font=font1, fill=text_color1)
    

   # Load the user's avatar image
    avatar = Image.open('test.jpeg')  # Replace with the actual path to the user's uploaded image

    # Resize the avatar to fit into a circle
    size = (496, 496)  # Set the desired size for the circular avatar
    avatar = avatar.resize(size, Image.LANCZOS)  # Use Image.ANTIALIAS for antialiasing

    # Create a circular mask
    mask = Image.new("L", size, 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.ellipse((0, 0, size[0], size[1]), fill=255)

    # Apply the circular mask to the avatar
    avatar = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
    avatar.putalpha(mask)

    # Choose a position for the circular avatar
    avatar_position = (516, 499)  # Replace with your desired position for the circular avatar

    # Paste the circular avatar onto the base image
    base_image.paste(avatar, avatar_position, avatar)

    # Save or display the resulting image
    base_image.save("page4Edit.png")  # Replace with your desired output path

    image_bytes = io.BytesIO()
    base_image.save(image_bytes, format="PNG")
    st.image(base_image, caption="Page4", use_column_width=True)
    # Add a download button for the image
    st.download_button(label="Download Image", data=image_bytes.getvalue(), key="download_button4")





def page5():
    # Load the base image
    base_image = Image.open("page5.png")  # Replace with your actual template path

    # Create a drawing object
    draw = ImageDraw.Draw(base_image)

    font_path = "XP-Vosta.ttf"  # Replace with your actual font file path
    font_size1 = 36
    font1 = ImageFont.truetype(font_path, font_size1)
    text_position1 = (110, 299)  # Replace with your desired position for the text
    text_color1 = (255, 255, 255)  # Replace with your desired color for the text

    # Draw the text on the image
    
    draw.text(text_position1, Top_Job_Titles, font=font1, fill=text_color1)
    

   # Load the user's avatar image
    avatar = Image.open('test.jpeg')  # Replace with the actual path to the user's uploaded image

    # Resize the avatar to fit into a circle
    size = (496, 496)  # Set the desired size for the circular avatar
    avatar = avatar.resize(size, Image.LANCZOS)  # Use Image.ANTIALIAS for antialiasing

    # Create a circular mask
    mask = Image.new("L", size, 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.ellipse((0, 0, size[0], size[1]), fill=255)

    # Apply the circular mask to the avatar
    avatar = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
    avatar.putalpha(mask)

    # Choose a position for the circular avatar
    avatar_position = (516, 499)  # Replace with your desired position for the circular avatar

    # Paste the circular avatar onto the base image
    base_image.paste(avatar, avatar_position, avatar)

    # Save or display the resulting image
    base_image.save("page5Edit.png")  # Replace with your desired output path
    
    image_bytes = io.BytesIO()
    base_image.save(image_bytes, format="PNG")
    st.image(base_image, caption="Page5", use_column_width=True)
    # Add a download button for the image
    st.download_button(label="Download Image", data=image_bytes.getvalue(), key="download_button5")




def page6():
    # Load the base image
    base_image = Image.open("page6.png")  # Replace with your actual template path   

   # Load the user's avatar image
    avatar = Image.open('test.jpeg')  # Replace with the actual path to the user's uploaded image

    # Resize the avatar to fit into a circle
    size = (600, 600)  # Set the desired size for the circular avatar
    avatar = avatar.resize(size, Image.LANCZOS)  # Use Image.ANTIALIAS for antialiasing

    # Create a circular mask
    mask = Image.new("L", size, 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.ellipse((0, 0, size[0], size[1]), fill=255)

    # Apply the circular mask to the avatar
    avatar = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
    avatar.putalpha(mask)

    # Choose a position for the circular avatar
    avatar_position = (240, 235)  # Replace with your desired position for the circular avatar

    # Paste the circular avatar onto the base image
    base_image.paste(avatar, avatar_position, avatar)

    # Save or display the resulting image
    base_image.save("page6Edit.png")  # Replace with your desired output path

    image_bytes = io.BytesIO()
    base_image.save(image_bytes, format="PNG")
    st.image(base_image, caption="Page6", use_column_width=True)
    # Add a download button for the image
    st.download_button(label="Download Image", data=image_bytes.getvalue(), key="download_button6")




# Streamlit app
st.title("Linkedin wrapped Generator")

# User input for name
user_name = st.text_input("Enter your full name:")

# User input for avatar image
user_avatar_path = st.file_uploader("Upload your profile picture:", type=["jpg", "png", "jpeg"])

# User input for Excel file
excel_file = st.file_uploader("Export your analytics and upload here (.xlsx):", type=["xlsx"])

# Display inputs
st.write("Entered Name:", user_name)

if user_avatar_path:
    st.write("Avatar Image Uploaded.")
else:
    st.warning("Please upload an avatar image.")

if excel_file:
    st.write("Excel File Uploaded.")
    data_analysis()
    page1()
    page2()
    page3()
    page4()
    page5()
    page6()
    credits()

else:
    st.warning("Please upload an Excel file.")

# Note: You can add the flyer generation part back as needed.

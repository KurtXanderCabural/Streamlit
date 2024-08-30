import streamlit as st
from base64 import b64encode
import os

def web_portfolio():
    # Page configs
    st.set_page_config(page_title="Kurt Xander Cabural's Portfolio", page_icon="⭐")
    
    # Set the page title
    st.write(f"""
    <div class="title" style="text-align: center;">
    <span style='font-size: 32px;'>Hello! My name is Kurt Xander Cabural</span>👋
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<style>div.block-container{padding-top:3rem;}</style>', unsafe_allow_html=True)

    # Define the path to the image file
    img_path = os.path.join("C:", "Users", "kurt xander cabural", "Downloads", "kx.jpg")

    # Check if the image file exists
    if os.path.exists(img_path):
        # Read and encode the image file
        with open(img_path, "rb") as img_file:
            img = "data:image/jpg;base64," + b64encode(img_file.read()).decode()
        
        # Display the image in the app
        st.write(f"""
        <div style="text-align: center;">
            <img src="{img}" style="border-radius: 50%; width: 200px; height: 200px;">
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error(f"Image file not found at: {img_path}")

    # Reading Profile (assuming you have a Profile.pdf file)
    profile_path = "Profile.pdf"
    if os.path.exists(profile_path):
        with open(profile_path, "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
            st.download_button(label="Download Profile", data=pdf_bytes, file_name="Kurt_Xander_Cabural_Profile.pdf")
    else:
        st.warning("Profile PDF not found.")

# Call the function to run the app
web_portfolio()

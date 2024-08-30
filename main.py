import streamlit as st
from base64 import b64encode

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

    # Get Profile Image
    with open("C:/Users/kurt xander cabural/Downloads/kx.jpg", "rb") as img_file:
        img = "data:image/jpg;base64," + b64encode(img_file.read()).decode()
    
    st.write(f"""
    <div style="text-align: center;">
        <img src="{img}" style="border-radius: 50%; width: 200px; height: 200px;">
    </div>
    """, unsafe_allow_html=True)

    # Reading Profile (assuming you have a Profile.pdf file)
    with open("Profile.pdf", "rb") as pdf_file:
       pdf_bytes = pdf_file.read()

# Call the function to run the app
web_portfolio()

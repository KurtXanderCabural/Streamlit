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
    image_path = r"C:\Users\YourUsername\Downloads\kx.jpg"

    with open(image_path, "rb") as img_file:
        img = "data:image/jpeg;base64," + b64encode(img_file.read()).decode()

    # Display the image in Streamlit
    st.write(f"""
    <img src="{img}" alt="Kurt Xander Cabural" style="width:200px; height:auto;">
    """, unsafe_allow_html=True)

 
 

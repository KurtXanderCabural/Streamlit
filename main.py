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

    # Set the title of the app
    st.title("Kurt Xander Cabural - Autobiography & Portfolio")

    # Autobiography section
    st.header("About Me")
    st.write("""
    Hello! I'm Kurt Xander Cabural, a passionate web designer and front-end developer currently in my 4th year of studying Information Technology at Cebu Institute of Technology University. My expertise lies in creating visually appealing and user-friendly web interfaces using technologies such as HTML, CSS, JavaScript, and React JS. I'm dedicated to continuous learning and always eager to take on new challenges that allow me to grow as a developer and designe

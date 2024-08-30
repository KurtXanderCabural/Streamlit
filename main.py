import streamlit as st

def web_portfolio():
    # Page configs
    st.set_page_config(page_title="Kurt Xander Cabural's Portfolio", page_icon="⭐")
    
    # Set the page title
    st.write(f"""
    <style>
    .waving-hand {{
        display: inline-block;
        animation: wave 1s linear infinite;
    }}
    
    @keyframes wave {{
        0% {{
            transform: rotate(0deg);
        }}
        25% {{
            transform: rotate(15deg);
        }}
        50% {{
            transform: rotate(0deg);
        }}
        75% {{
            transform: rotate(-15deg);
        }}
        100% {{
            transform: rotate(0deg);
        }}
    }}
    
    .center {{
        text-align: center;
    }}
    </style>
    <div class="title" style="text-align: center;">
    <span style='font-size: 32px;'>Hello! My name is Kurt Xander Cabural</span>
    <span class="waving-hand">👋</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<style>div.block-container{padding-top:3rem;}</style>', unsafe_allow_html=True)

    # Use the raw GitHub URL for the profile image
    image_url = "https://raw.githubusercontent.com/KurtXanderCabural/Streamlit/main/kx.jpg"

    # Display the image in Streamlit with center alignment
    st.write(f"""
    <div class="center">
        <img src="{image_url}" alt="Kurt Xander Cabural" style="width:200px; height:auto;">
    </div>
    """, unsafe_allow_html=True)

    # Set the title of the app
    st.title("Kurt Xander Cabural - Autobiography & Portfolio")

    # Autobiography section
    st.header("About Me")
    st.write("""
    Hello! I'm Kurt Xander Cabural, a passionate web designer and front-end developer currently in my 4th year of studying Information Technology at Cebu Institute of Technology University. My expertise lies in creating visually appealing and user-friendly web interfaces using technologies such as HTML, CSS, JavaScript, and React JS. I'm dedicated to continuous learning and always eager to take on new challenges that allow me to grow as a developer and designer.
    """)

    # Portfolio section
    st.header("Portfolio")

    # Project 1: Focusify
    st.subheader("Focusify - Systems Integration and Architecture")
    st.write("""
    **Role:** Web Designer and Front-End Developer  
    **Date:** May 2024  
    **Description:** Designed and developed responsive web interfaces using HTML, CSS, and JavaScript. Utilized Figma to create intuitive designs and collaborated with the team to integrate these designs into the overall system architecture.
    """)

    # Project 2: CampusEats
    st.subheader("CampusEats - Capstone Project")
    st.write("""
    **Role:** Front-End Developer  
    **Date:** August 2024  
    **Description:** Developed and implemented the user interface using React JS and CSS, creating a responsive and user-friendly experience. Designed UI elements with Figma, ensuring a cohesive and attractive design. Collaborated with backend developers to integrate front-end features with the Java-based backend.
    """)

    # Contact Information
    st.header("Contact Me")
    st.write("""
    - **Email:** kurtxander1@gmail.com  
    - **Phone:** 09912233775  
    - **LinkedIn:** [linkedin.com/in/kurtxander](#)
    """)

if __name__ == "__main__":
    web_portfolio()

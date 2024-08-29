import streamlit as st
from base64 import b64encode

def web_portfolio():
    # page configs 
    st.set_page_config(page_title = "Abhisheak Saraswat's Portfolio",page_icon="⭐")
    # Set the page title
    st.write(f"""
    <div class="title" style="text-align: center;">
    <span style='font-size: 32px;'>Hello! My name is Abhisheak Saraswat</span>👋
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<style>div.block-container{padding-top:3rem;}</style>',unsafe_allow_html=True)

    # Get Profile Image
    with open("dp.png", "rb") as img_file:
        img = "data:image/png;base64," + b64encode(img_file.read()).decode()
    
    # Reading Profile
    with open("Profile.pdf", "rb") as pdf_file:
       pdf_bytes = pdf_file.read()

    # st.write(f"""
    # <div style="display: flex; justify-content: center;">
    # <div class="box">
    # <img src="{img}" alt="Abhisheak Saraswat" style="width: 300px; height: 200px;">
    # </div>
    # </div>
    # """, 
    # unsafe_allow_html=True)
    # Add animation on the DP
    st.write(f"""
    <style>
    @keyframes slowTilt {{
    0%, 100% {{
    transform: rotate(0deg);
    }}
    50% {{
    transform: rotate(5deg);
    }}
    }}
    .box img {{
    width: 300px;
    height: 200px;
    border-radius: 50%;
    animation: slowTilt 2s ease-in-out infinite;
    }}
    </style>
    <div style="display: flex; justify-content: center;">
    <div class="box">
    <img src="{img}">
    </div>
    </div>
    """, 
    unsafe_allow_html=True)

# Set the title
    st.write(f"""
             <div class=
             "subtitle" style="text-align: center;">Senior Data Scientist and GenAI Engineer</div>""",
              unsafe_allow_html=True)
# Add Social Icons
    social_icons_data = {
    "Kaggle": ["https://www.kaggle.com/abhisheak", "https://www.kaggle.com/static/images/site-logo.svg"],
    "LinkedIn": ["https://www.linkedin.com/in/abhisheaksaraswat", "https://cdn-icons-png.flaticon.com/128/3536/3536505.png"],
    "GitHub": ["https://github.com/abhisheaksaraswat", "https://cdn-icons-png.flaticon.com/128/5968/5968866.png"],
    "YouTube": ["https://www.youtube.com/@programmingisfunn", "https://cdn-icons-png.flaticon.com/128/1384/1384060.png"],
    "Medium": ["https://medium.com/@programmingisfun", "https://cdn-icons-png.flaticon.com/128/5968/5968906.png"]
    }

    social_icons_html = [
    f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'>"
    f"<img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'"
    f" style='width: 25px; height: 25px;'></a>"
    for platform in social_icons_data
]
    st.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
    {''.join(social_icons_html)}
    </div>""", 
    unsafe_allow_html=True)

    st.write("##")

    # About Me Section
    st.subheader("About Me")

    st.markdown("""
    - 🧑‍💻 I am a **Senior Data Scientist and Gen AI Engineer** at [IBM](https://www.ibm.com/), 
    where I am currently working on a healthcare project for [Elevance Healthcare](https://www.elevancehealth.com/).
    - 🚀 Previously, I served as an Application Development Manager at [MMC](https://www.mmc.com/).
    - ❤️ I am passionate about *Machine Learning/Deep Learning, MLOps, Data Science, Software Engineering, 
    Computer Vision, Data Analytics, Data Engineering, Automation*, and more!
    - 🤖 Additionally, I am a Senior Instructor at [upGrad](https://www.upgrad.com/), where I offer bootcamp sessions 
    on topics such as Data Science, Machine Learning, Natural Language Processing, Automation, and more.
    - 🏂 In my free time, I enjoy practicing sports such as Cricket and Cycling.
    - 🪧 You can reach me at myprogrammingisfun@gmail.com.
    - 🏠 Based in India.
    """)

    st.write("##")

    # Download CV button
    st.download_button(label="📄 Download my CV", data=pdf_bytes, file_name="Abhisheak_linkedin_cv.pdf", mime="application/pdf",)
    st.write("##")
    st.write(f"""<div class="subtitle" style="text-align: center;">🌟 Have A Wonderfull Day!!! 🌟</div>""", unsafe_allow_html=True)


if __name__ == "__main__":
    web_portfolio()

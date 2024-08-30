import streamlit as st

def web_portfolio():
    # Page configurations
    st.set_page_config(page_title="Kurt Xander Cabural", page_icon="⭐")

    # Initialize session state for toggling contact information
    if "show_contact" not in st.session_state:
        st.session_state["show_contact"] = False
    if "sidebar_opened" not in st.session_state:
        st.session_state["sidebar_opened"] = False

    # Sidebar Contact Button
    if st.sidebar.button('Contact'):
        st.session_state["show_contact"] = not st.session_state["show_contact"]
        st.session_state["sidebar_opened"] = True

    # Hide contact information when the sidebar is first opened or the "Contact" button is not clicked
    if st.session_state["show_contact"]:
        st.sidebar.write("""
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <img src="https://cdn-icons-png.flaticon.com/128/6424/6424087.png" 
            style="width: 25px; height: 25px; margin-right: 10px;" alt="Gmail Icon">
            <a href="mailto:kurtxander1@gmail.com" style="text-decoration: none; color: inherit;">kurtxander1@gmail.com</a>
        </div>
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <img src="https://cdn-icons-png.flaticon.com/128/6422/6422202.png" 
            style="width: 25px; height: 25px; margin-right: 10px;" alt="LinkedIn Icon">
            <a href="https://www.linkedin.com/in/kurt-xander-cabural-129132310/" 
            target="_blank" style="text-decoration: none; color: inherit;">Kurt Xander Cabural</a>
        </div>
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <img src="https://cdn-icons-png.flaticon.com/128/6422/6422199.png" 
            style="width: 25px; height: 25px; margin-right: 10px;" alt="Facebook Icon">
            <a href="https://www.facebook.com/Cabural.Kurt.Xander.M" 
            target="_blank" style="text-decoration: none; color: inherit;">Kurt Xander Cabural</a>
        </div>
        """, unsafe_allow_html=True)
    elif not st.session_state["sidebar_opened"]:
        st.sidebar.write("")  # Ensures nothing is shown when the info is hidden

    # Reset sidebar open state
    st.session_state["sidebar_opened"] = False

    # Page title with waving hand emoji animation
    st.write("""
    <style>
    .waving-hand {
        display: inline-block;
        animation: wave 1s linear infinite;
    }
    
    @keyframes wave {
        0% { transform: rotate(0deg); }
        25% { transform: rotate(15deg); }
        50% { transform: rotate(0deg); }
        75% { transform: rotate(-15deg); }
        100% { transform: rotate(0deg); }
    }

    @keyframes slowTilt {
        0%, 100% { transform: rotate(0deg); }
        50% { transform: rotate(5deg); }
    }
    
    .box {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    
    .box img {
        animation: slowTilt 2s ease-in-out infinite;
        max-width: 40%;
        height: auto;
    }
    </style>
    <div class="title" style="text-align: center;">
        <span style='font-size: 32px;'>Hello! My name is Kurt Xander Cabural</span>
        <span class="waving-hand">👋</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<style>div.block-container{padding-top:3rem;}</style>', unsafe_allow_html=True)

    # Display profile image with center alignment and animation
    image_url = "https://raw.githubusercontent.com/KurtXanderCabural/Streamlit/main/kx.png"
    st.write(f"""
    <div class="box">
        <img src="{image_url}" alt="Kurt Xander Cabural">
    </div>
    """, unsafe_allow_html=True)

    # Title and social icons
    st.write("""
    <div class="subtitle" style="text-align: center;">Front-end Developer and Web Designer</div>
    """, unsafe_allow_html=True)

    social_icons_data = {
        "Figma": ["https://www.figma.com/files/team/1239597512271544315/all-projects?fuid=1239597507354790543", "https://cdn-icons-png.flaticon.com/128/6423/6423305.png"],
        "LinkedIn": ["https://www.linkedin.com/in/kurt-xander-cabural-129132310/", "https://cdn-icons-png.flaticon.com/128/6422/6422202.png"],
        "GitHub": ["https://github.com/KurtXanderCabural", "https://cdn-icons-png.flaticon.com/128/5968/5968866.png"],
        "Facebook": ["https://www.facebook.com/Cabural.Kurt.Xander.M", "https://cdn-icons-png.flaticon.com/128/6422/6422199.png"],
        "Discord": ["https://discord.com/channels/@me", "https://cdn-icons-png.flaticon.com/128/6422/6422197.png"]
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
    </div>
    """, unsafe_allow_html=True)

    st.write("##")

    # About Me Section
    st.subheader("About Me")
    st.markdown("""
    I am a 4th-year IT student with a strong passion for technology and collaborative projects. 
    Throughout my academic journey, I have consistently worked with my classmates on various projects, 
    gaining hands-on experience and honing my skills in web development and design. I specialize in HTML, React JS, 
    and React TS, and have a keen eye for design, utilizing Figma to create intuitive and visually appealing user interfaces. 
    My ability to work effectively in a team, combined with my technical expertise and design skills, positions me well to contribute to innovative 
    and impactful projects. I am dedicated to continuous learning and excited to bring my skills and enthusiasm to new challenges in the IT field.
    """)

if __name__ == "__main__":
    web_portfolio()

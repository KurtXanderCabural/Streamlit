import streamlit as st

def web_portfolio():
    # Page configurations
    st.set_page_config(page_title="Kurt Xander Cabural", page_icon="⭐")

   # Custom CSS to replicate the sidebar design
    st.markdown("""
    <style>
    /* Sidebar container */
    .css-18e3th9 {
        background-color: #2E1D43;
        padding-top: 20px;
    }
    
    /* Sidebar title */
    .sidebar-title {
        font-size: 24px;
        color: #A899C0;
        font-weight: bold;
        padding: 10px;
        text-align: left;
        margin-bottom: 30px;
        margin-left: 20px;
    }
    
    /* Sidebar items */
    .sidebar-item {
        display: flex;
        align-items: center;
        padding: 10px 20px;
        font-size: 16px;
        color: #A899C0;
        text-decoration: none;
        margin: 5px 0;
    }
    
    .sidebar-item:hover {
        background-color: #45275E;
        cursor: pointer;
        border-radius: 10px;
    }
    
    /* Sidebar icons */
    .sidebar-icon {
        margin-right: 10px;
    }
    
    /* User section */
    .user-section {
        display: flex;
        align-items: center;
        padding: 20px;
        background-color: #2E1D43;
        margin-top: 40px;
        border-top: 1px solid #A899C0;
    }
    
    .user-section img {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        margin-right: 10px;
    }
    
    .user-info {
        font-size: 14px;
        color: #A899C0;
    }
    
    .user-info strong {
        display: block;
    }
    </style>
    """, unsafe_allow_html=True)

    # Initialize session state
    if "show_contact" not in st.session_state:
        st.session_state["show_contact"] = False
    if "show_skills" not in st.session_state:
        st.session_state["show_skills"] = False
    if "show_resume" not in st.session_state:
        st.session_state["show_resume"] = False

    # Sidebar Items
    st.sidebar.markdown("<div class='sidebar-title'>Reflex</div>", unsafe_allow_html=True)
    
    def toggle_section(section_name):
        if section_name == "contact":
            st.session_state["show_contact"] = not st.session_state["show_contact"]
        elif section_name == "skills":
            st.session_state["show_skills"] = not st.session_state["show_skills"]
        elif section_name == "resume":
            st.session_state["show_resume"] = not st.session_state["show_resume"]


    # Sidebar Layout
    st.sidebar.markdown("<div class='sidebar-title'>Reflex</div>", unsafe_allow_html=True)
    
    # Sidebar Items
    sidebar_items = [
        ("📩", "Contact"),
        ("📝", "Skills"),
        ("📑", "Resume"),
        ("🔔", "Notifications"),
        ("⚙️", "Settings"),
        ("↩️", "Log out")
    ]
    
    for icon, name, section in sidebar_items:
        if section:
            st.sidebar.markdown(f"""
            <div class='sidebar-item' onclick="window.parent.postMessage({{'type':'toggle', 'section':'{section}'}})">
                <span class='sidebar-icon'>{icon}</span>
                <span>{name}</span>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.sidebar.markdown(f"""
            <div class='sidebar-item'>
                <span class='sidebar-icon'>{icon}</span>
                <span>{name}</span>
            </div>
            """, unsafe_allow_html=True)

    # User Section
    st.sidebar.markdown("""
    <div class='user-section'>
        <img src='https://cdn-icons-png.flaticon.com/512/3135/3135715.png' alt='User Icon'>
        <div class='user-info'>
            <strong>My account</strong>
            user@reflex.dev
        </div>
    </div>
    """, unsafe_allow_html=True)

     # Display or hide content based on session state
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

    if st.session_state["show_skills"]:
        st.sidebar.write("""
        <div style="margin-bottom: 20px;">
            <h3>Skills</h3>
            <ul class="skills-list">
                <li><img src="https://cdn-icons-png.flaticon.com/128/732/732212.png" class="moving-icon" alt="HTML Icon">HTML</li>
                <li><img src="https://cdn-icons-png.flaticon.com/128/919/919827.png" class="moving-icon" alt="React JS Icon">React JS</li>
                <li><img src="https://cdn-icons-png.flaticon.com/128/919/919830.png" class="moving-icon" alt="React TS Icon">React TS</li>
                <li><img src="https://cdn-icons-png.flaticon.com/128/871/871210.png" class="moving-icon" alt="Figma Icon">Figma Design</li>
                <li><img src="https://cdn-icons-png.flaticon.com/128/226/226777.png" class="moving-icon" alt="Java Icon">Java Programming</li>
                <li><img src="https://cdn-icons-png.flaticon.com/128/919/919831.png" class="moving-icon" alt="CSS Icon">CSS Web Development</li>
                <li><img src="https://cdn-icons-png.flaticon.com/128/5968/5968242.png" class="moving-icon" alt="JavaScript Icon">JavaScript Web Development</li>
                <li><img src="https://cdn-icons-png.flaticon.com/128/2620/2620675.png" class="moving-icon" alt="MySQL Icon">MySQL Database</li>
                <li><img src="https://cdn-icons-png.flaticon.com/128/2922/2922501.png" class="moving-icon" alt="Team Collaboration Icon">Team Collaboration</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    if st.session_state["show_resume"]:
        st.sidebar.write("""
        <div class="resume-container">
            <a class="resume-link" href="https://drive.google.com/file/d/1gGJ1pB2cqr6bHoNTCtugTwGifrD_cj1e/view?usp=sharing" target="_blank">View Resume</a>
        </div>
        """, unsafe_allow_html=True)

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

    # Use the raw GitHub URL for the profile image
    image_url = "https://raw.githubusercontent.com/KurtXanderCabural/Streamlit/main/kx.png"

    # Display the image with center alignment and animation
    st.write(f"""
    <div class="box">
        <img src="{image_url}" alt="Kurt Xander Cabural">
    </div>
    """, unsafe_allow_html=True)

    # Set the title
    st.write("""
    <div class="subtitle" style="text-align: center;">Front-end Developer and Web Designer</div>
    """, unsafe_allow_html=True)

    # Social Icons
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

    # --- About Me Section ---
    st.write('\n')
    st.subheader("About Me")
    st.write("---")

    st.markdown("""
    I am a 4th-year IT student with a strong passion for technology and collaborative projects. 
    Throughout my academic journey, I have consistently worked with my classmates on various projects, 
    gaining hands-on experience and honing my skills in web development and design. I specialize in HTML, React JS, 
    and React TS, and have a keen eye for design, utilizing Figma to create intuitive and visually appealing user interfaces. 
    My ability to work effectively in a team, combined with my technical expertise and design skills, positions me well to contribute to innovative 
    and impactful projects. I am dedicated to continuous learning and excited to bring my skills and enthusiasm to new challenges in the IT field.
    """)

    # --- Educational Attainment ---
    st.write('\n')
    st.subheader("Educational Attainment")
    st.write("---")

    # --- SCHOOL 1
    st.write("📚", "**Cebu Institute of Technology University**")
    st.write("Bachelor of Science in Information Technology | 2024 -2025")
    st.write(
    """
    - ► Studying Project Management, Data Analytics, and Application Development with Emerging Technologies
    """
    )

    # --- SCHOOL 2
    st.write('\n')
    st.write("📚", "**Cebu Institute of Technology University**")
    st.write("Graduated STEM | 2018 - 2020")
    st.write(
    """
    - ► Thesis involved with Science, Technology and Computational Mathematics
    - ► GPA 4.1
    """
    )

    # --- Projects and Accomplishment ---
    st.write('\n')
    st.subheader("Projects and Accomplishment")
    st.write("---")

    # --- Project 1
    st.write("🗂️", "**CampusEats - Capstone**")
    st.write("August 2024 - Cebu Institute of Techonology University")
    st.write(
    """
    - 💡 Developed and implemented the user interface using React JS and CSS, creating a responsive and user-friendly experience.
    - 💡 Utilized Figma to design intuitive and visually appealing user interfaces, ensuring a cohesive and attractive design.
    - 💡 Collaborated with backend developers to integrate front-end features with the Java-based backend.
    - 💡 Designed and optimized web pages to ensure seamless navigation and fast loading times.
    """
    )


     # --- Project 2
    st.write("🗂️", "**Focusify - Systems Integration and Architecture**")
    st.write("May 2024 - Cebu Institute of Techonology University")
    st.write(
    """
    - 💡 Designed and developed web interfaces using HTML, CSS, and JavaScript.
    - 💡 Utilized Figma for creating intuitive and visually appealing designs.
    - 💡 Collaborated with the team for seamless system integration.
    - 💡 Ensured responsive and optimized performance across devices.
    """
    )

    
if __name__ == "__main__":
    web_portfolio()

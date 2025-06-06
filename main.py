import streamlit as st

def web_portfolio():
    # Page configurations
    st.set_page_config(page_title="Kurt Xander Cabural", page_icon="⭐")

  # Initialize session state for various sections
    if "show_contact_info" not in st.session_state:
        st.session_state.show_contact_info = False
    if "show_skills" not in st.session_state:
        st.session_state.show_skills = False
    if "show_resume" not in st.session_state:
        st.session_state.show_resume = False
    if "show_notifications" not in st.session_state:
        st.session_state.show_notifications = False

    # Custom CSS to replicate the sidebar design and add moving icons
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
    
    /* Moving icons */
    .moving-icon {
        width: 20px;
        height: 20px;
        margin-right: 10px;
        animation: move 1.5s ease-in-out infinite;
    }
    
    @keyframes move {
        0% { transform: translateY(0); }
        50% { transform: translateY(-5px); }
        100% { transform: translateY(0); }
    }
    
    /* Sidebar content */
    .sidebar-content {
        padding-left: 30px;
    }
    
    /* Sidebar links */
    .sidebar-link {
        display: block;
        margin-top: 10px;
        color: #A899C0;
        text-decoration: none;
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

    # Sidebar Layout
    st.sidebar.markdown("<div class='sidebar-title'>Hello! 👋</div>", unsafe_allow_html=True)
    
    # Sidebar Items
    sidebar_items = [
        ("📩", "Contact"),
        ("📝", "Skills"),
        ("📑", "Resume"),
        ("🔔", "Notifications"),
        ("↩️", "Log out")
    ]
    
    for icon, name in sidebar_items:
        if name == "Contact":
            if st.sidebar.button(f"{icon} {name}"):
                st.session_state.show_contact_info = not st.session_state.show_contact_info
            if st.session_state.show_contact_info:
                st.sidebar.markdown("""
                <div style="display: flex; align-items: center; margin-bottom: 20px; padding-left: 30px;">
                    <img src="https://cdn-icons-png.flaticon.com/128/6422/6422202.png" 
                    style="width: 25px; height: 25px; margin-right: 10px;" alt="LinkedIn Icon">
                    <a href="https://www.linkedin.com/in/kurt-xander-cabural-129132310/" 
                    target="_blank" style="text-decoration: none; color: inherit;">Kurt Xander Cabural</a>
                </div>
                """, unsafe_allow_html=True)
        elif name == "Skills":
            if st.sidebar.button(f"{icon} {name}"):
                st.session_state.show_skills = not st.session_state.show_skills
            if st.session_state.show_skills:
                st.sidebar.markdown("""
                <div class='sidebar-content'>
                    <ul>
                        <li><img src="https://cdn-icons-png.flaticon.com/128/732/732212.png" class="moving-icon" alt="HTML Icon">HTML</li>
                        <li><img src="https://cdn-icons-png.flaticon.com/128/919/919827.png" class="moving-icon" alt="React JS Icon">React JS</li>
                        <li><img src="https://cdn-icons-png.flaticon.com/128/919/919830.png" class="moving-icon" alt="React TS Icon">React TS</li>
                        <li><img src="https://cdn-icons-png.flaticon.com/128/871/871210.png" class="moving-icon" alt="Figma Icon">Figma Design</li>
                        <li><img src="https://cdn-icons-png.flaticon.com/128/226/226777.png" class="moving-icon" alt="Java Icon">Java Programming</li>
                        <li><img src="https://cdn-icons-png.flaticon.com/128/919/919831.png" class="moving-icon" alt="CSS Icon">CSS Web Development</li>
                        <li><img src="https://cdn-icons-png.flaticon.com/128/5968/5968242.png" class="moving-icon" alt="JavaScript Icon">JavaScript WebDev</li>
                        <li><img src="https://cdn-icons-png.flaticon.com/128/2620/2620675.png" class="moving-icon" alt="MySQL Icon">MySQL Database</li>
                        <li><img src="https://cdn-icons-png.flaticon.com/128/2922/2922501.png" class="moving-icon" alt="Team Collaboration Icon">Team Collaboration</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
        elif name == "Resume":
            if st.sidebar.button(f"{icon} {name}"):
                st.session_state.show_resume = not st.session_state.show_resume
            if st.session_state.show_resume:
                st.sidebar.markdown("""
                <div class='sidebar-content'>
                    <a href="https://drive.google.com/file/d/1nGTb7YxJgcEMqdfrKykPFwqU-KajT4d3/view?usp=sharing" 
                    target="_blank" class="sidebar-link">View My Resume</a>
                </div>
                """, unsafe_allow_html=True)
        elif name == "Notifications":
            if st.sidebar.button(f"{icon} {name}"):
                st.session_state.show_notifications = not st.session_state.show_notifications
            if st.session_state.show_notifications:
                st.sidebar.markdown("""
                <div class='sidebar-content'>
                    <ul>
                        <li><a href="https://www.linkedin.com/in/person1" target="_blank" class="sidebar-link">Person 1 - New Message</a></li>
                        <li><a href="https://www.linkedin.com/in/person2" target="_blank" class="sidebar-link">Person 2 - Follow-up</a></li>
                        <li><a href="https://www.linkedin.com/in/person3" target="_blank" class="sidebar-link">Person 3 - Job Opportunity</a></li>
                        <!-- Add more notifications as needed -->
                    </ul>
                </div>
                """, unsafe_allow_html=True)
        elif name == "Log out":
            if st.sidebar.button(f"{icon} {name}"):
                st.markdown("""
                <script>
                window.location.href = "https://share.streamlit.io/";
                </script>
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
            kurtxander.cabural@cit.edu
        </div>
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
    I am a passionate and driven IT graduate with practical experience in web development, UI/UX design, and collaborative software projects. 
    Proficient in HTML, React.js, and TypeScript, I have developed responsive, user-centered applications while refining my design skills through Figma, 
    translating ideas into functional and visually engaging interfaces. My background includes successful teamwork on academic and freelance projects, 
    where I’ve demonstrated strong communication, adaptability, and problem-solving abilities. Eager to grow and contribute meaningfully, I am open to any role 
    in the IT field—from front-end development to UI/UX design, QA, or technical support. I bring a proactive mindset, fast learning ability, and a commitment 
    to delivering value in dynamic, tech-driven environments.
    """)

    # --- Educational Attainment ---
    st.write('\n')
    st.subheader("Educational Attainment")
    st.write("---")

    # --- SCHOOL 1
    st.write("📚", "**Cebu Institute of Technology University**")
    st.write("Bachelor of Science in Information Technology | 2025")
    st.write(
    """
    - ► Specialized in Project Management, Data Analytics, and Application Development using Emerging Technologies—developing strong analytical, 
        development, and problem-solving skills aligned with industry demands.
    - ► GPA 4.1
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

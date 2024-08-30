import streamlit as st
import rx  # Ensure you have the rx library installed for this example

def sidebar_item(text: str, icon: str, href: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon, size="24px"),  # Adjust icon size
            rx.text(text, size="4", weight="bold"),
            width="100%",
            padding_x="0.75rem",
            padding_y="0.5rem",
            align="center",
            style={
                "_hover": {
                    "bg": rx.color("blue.500"),
                    "color": rx.color("white"),
                },
                "border-radius": "0.5em",
                "transition": "background-color 0.3s ease, color 0.3s ease",  # Smooth hover transition
            },
        ),
        href=href,
        underline="none",
        weight="medium",
        width="100%",
    )


def sidebar_items() -> rx.Component:
    return rx.vstack(
        sidebar_item("Contact", "phone", "/#"),
        sidebar_item("Skills", "star", "/#"),
        sidebar_item("Resume", "file-text", "/#"),
        spacing="1",
        width="100%",
    )


def sidebar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2.5em",  # Slightly larger logo
                        height="auto",
                        border_radius="50%",  # Circular logo
                    ),
                    rx.heading(
                        "My Portfolio", size="6", weight="bold", color="blue.700"
                    ),
                    align="center",
                    justify="start",
                    padding_x="1rem",  # Increased padding
                    width="100%",
                ),
                sidebar_items(),
                spacing="4",  # Increased spacing between items
                padding_x="1.5em",
                padding_y="2em",
                bg=rx.color("gray.100"),  # Light background color
                align="start",
                height="100vh",  # Full height sidebar
                width="18em",  # Slightly wider sidebar
            ),
        ),
        rx.mobile_and_tablet(
            rx.drawer.root(
                rx.drawer.trigger(
                    rx.icon("menu", size=30, color="blue.500")  # Change menu icon color
                ),
                rx.drawer.overlay(z_index="5"),
                rx.drawer.portal(
                    rx.drawer.content(
                        rx.vstack(
                            rx.box(
                                rx.drawer.close(
                                    rx.icon("close", size=30, color="blue.500")  # Change close icon color
                                ),
                                width="100%",
                            ),
                            sidebar_items(),
                            spacing="4",  # Increased spacing
                            width="100%",
                        ),
                        top="auto",
                        right="auto",
                        height="100%",
                        width="20em",
                        padding="2em",
                        bg=rx.color("gray.100"),  # Light background color
                    ),
                    width="100%",
                ),
                direction="left",
            ),
            padding="1em",
        ),
    )


def web_portfolio():
    # Page configurations
    st.set_page_config(page_title="Kurt Xander Cabural", page_icon="⭐")

    # Initialize session state for toggling contact information, skills, and resume
    if "show_contact" not in st.session_state:
        st.session_state["show_contact"] = False
    if "show_skills" not in st.session_state:
        st.session_state["show_skills"] = False
    if "show_resume" not in st.session_state:
        st.session_state["show_resume"] = False

    # Streamlit sidebar layout with the updated design
    st.sidebar.title("Navigation")
    sidebar_html = """
    <div style="
        background-color: #F0F0F0;
        padding: 1em;
        border-radius: 0.5em;
        width: 100%;
        height: 100vh;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
    ">
        <div style="text-align: center; margin-bottom: 1em;">
            <img src="/logo.jpg" style="width: 80px; height: 80px; border-radius: 50%;" />
            <h2 style="color: #1E3A8A;">My Portfolio</h2>
        </div>
        <a href="#contact" style="
            display: block;
            padding: 0.5em;
            text-decoration: none;
            color: #1E3A8A;
            border-radius: 0.5em;
            transition: background-color 0.3s ease, color 0.3s ease;
            margin-bottom: 0.5em;
        ">Contact</a>
        <a href="#skills" style="
            display: block;
            padding: 0.5em;
            text-decoration: none;
            color: #1E3A8A;
            border-radius: 0.5em;
            transition: background-color 0.3s ease, color 0.3s ease;
            margin-bottom: 0.5em;
        ">Skills</a>
        <a href="#resume" style="
            display: block;
            padding: 0.5em;
            text-decoration: none;
            color: #1E3A8A;
            border-radius: 0.5em;
            transition: background-color 0.3s ease, color 0.3s ease;
            margin-bottom: 0.5em;
        ">Resume</a>
    </div>
    """
    st.sidebar.markdown(sidebar_html, unsafe_allow_html=True)

    # Main content display
    if st.session_state["show_contact"]:
        st.write("""
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
    elif not st.session_state["show_skills"] and not st.session_state["show_resume"]:
        st.sidebar.write("")  # Ensures nothing is shown when the info is hidden

    if st.session_state["show_skills"]:
        st.sidebar.write("""
        <style>
        .moving-icon {
            display: inline-block;
            animation: move 2s ease-in-out infinite;
            width: 25px; /* Set the same size as contact icons */
            height: 25px; /* Set the same size as contact icons */
            margin-right: 10px;
        }

        @keyframes move {
            0% { transform: translateX(0); }
            50% { transform: translateX(10px); }
            100% { transform: translateX(0); }
        }

        .skills-list {
            list-style-type: none;
            padding: 0;
        }

        .skills-list li {
            margin-bottom: 15px; /* Line spacing for skills list items */
        }
        </style>
        <div style="margin-bottom: 20px;">
            <h3>Skills</h3>
            <ul class="skills-list">
                <li><img src="https://cdn-icons-png.flaticon.com/128/732/732212.png" class="moving-icon" alt="HTML Icon">HTML</li>
                <li><img src="https://cdn-icons-png.flaticon.com/128/919/919827.png" class="moving-icon" alt="React JS Icon">React JS</li>
                <li><img src="https://cdn-icons-png.flaticon.com/128/919/919827.png" class="moving-icon" alt="React TS Icon">React TS</li>
                <li><img src="https://cdn-icons-png.flaticon.com/128/190/190411.png" class="moving-icon" alt="Figma Icon">Figma Design</li>
                <li><img src="https://cdn-icons-png.flaticon.com/128/226/226777.png" class="moving-icon" alt="Java Icon">Java Programming</li>
                <li><img src="https://cdn-icons-png.flaticon.com/128/226/226777.png" class="moving-icon" alt="CSS Icon">CSS Web Development</li>
                <li><img src="https://cdn-icons-png.flaticon.com/128/919/919826.png" class="moving-icon" alt="JavaScript Icon">JavaScript Web Development</li>
                <li><img src="https://cdn-icons-png.flaticon.com/128/2111/2111372.png" class="moving-icon" alt="MySQL Icon">MySQL Database</li>
                <li><img src="https://cdn-icons-png.flaticon.com/128/2461/2461701.png" class="moving-icon" alt="Team Collaboration Icon">Team Collaboration</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    if st.session_state["show_resume"]:
        st.sidebar.write("""
        <h3>Resume</h3>
        <a href="https://example.com/resume.pdf" target="_blank">Download Resume</a>
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

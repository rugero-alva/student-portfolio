import streamlit as st

# Set page title and icon
st.set_page_config(page_title="My Digital Footprint", page_icon="🎓")

# --- DATA ---
profile_data = {
    "name": "RUGERO Alva Victor",
    "location": "Musanze, Rwanda",
    "field_of_study": "BSc Computer Science, Year 3",
    "university": "INES-RUHENGERI",
    "about_me": "A passionate and ambitious computer science student with a keen interest in AI and web development. I enjoy tackling challenging problems and creating innovative solutions.",
}

projects = [
    {
        "title": "Student Attendance System using Face Recognition",
        "type": "Group Project",
        "year": "Year 2",
        "description": "Developed a face recognition system for automated student attendance tracking.",
        "link": "https://github.com/your-username/face-recognition-attendance",
    },
    {
        "title": "AI-Powered Chatbot for Customer Support",
        "type": "Individual Project",
        "year": "Year 3",
        "description": "Built a chatbot using natural language processing to answer customer queries.",
        "link": "https://github.com/your-username/ai-chatbot",
    },
    {
        "title": "Analysis of Rwandan GDP Trends",
        "type": "Dissertation",
        "year": "Year 3",
        "description": "Conducted in-depth analysis of Rwandan GDP trends using time series forecasting.",
        "link": "https://your-university-repo.com/dissertation-RUGERO",
    },
]

testimonials = [
    "RUGERO is a brilliant problem solver! His final year project was truly innovative. – Dr. Theodore",
    "Working with RUGERO on the AI chatbot project was a pleasure. He's a dedicated and talented developer. – John Doe (Team Member)",
]

# --- FUNCTIONS ---
def filter_projects(projects, selected_year=None, selected_type=None):
    filtered = []
    for project in projects:
        if (selected_year is None or project["year"] == selected_year) and \
           (selected_type is None or project["type"] == selected_type):
            filtered.append(project)
    return filtered

# --- SIDEBAR ---
st.sidebar.title("📍 Navigation")
page = st.sidebar.radio("Go To:", ["Home", "Projects", "Skills", "Contact"])

# --- HOME ---
if page == "home":
    st.title("🎓 Student Portfolio")

    # Profile Picture (HOME)
    uploaded_image_home = st.file_uploader("Upload Home Profile Picture", type=["jpg", "png"])
    if uploaded_image_home is not None:
        st.image(uploaded_image_home, width=150, caption="Home Profile Picture")
    else:
        st.image("person.jpg", width=150, caption="Home Default Image")

    # Profile Details
    st.write(f"**{profile_data['name']}**")
    st.write(f"📍 {profile_data['location']}")
    st.write(f"📚 {profile_data['field_of_study']}")
    st.write(f"🎓 {profile_data['university']}")

    # About Me
    st.markdown("---")
    st.subheader("About Me")
    st.write(profile_data["about_me"])

    # Resume Download
    try:
        with open("resume.pdf", "rb") as file:
            resume_bytes = file.read()
            st.download_button(label="📄 Download Resume", data=resume_bytes, file_name="Resume.pdf", mime="application/pdf")
    except FileNotFoundError:
        st.write("Resume.pdf not found")

# --- PROJECTS ---
elif page == "Projects":
    st.title("💻 Projects")

    # Project Filters
    selected_year = st.selectbox("Filter by Year:", ["All Years", "Year 1", "Year 2", "Year 3"])
    selected_type = st.selectbox("Filter by Type:", ["All Types", "Individual Project", "Group Project", "Dissertation"])

    # Filter Projects
    filtered_projects = filter_projects(projects, selected_year if selected_year != "All Years" else None,
                                        selected_type if selected_type != "All Types" else None)

    # Display Projects
    for project in filtered_projects:
        with st.expander(f"📊 {project['title']}"):
            st.write(f"**Type:** {project['type']}")
            st.write(f"**Year:** {project['year']}")
            st.write(f"**Description:** {project['description']}")
            if project["link"]:
                st.write(f"**Link:** {project['link']}")

# --- SKILLS ---
elif page == "skills":
    st.title("⚡ Skills and Achievements")

    # Profile picture in skills section.
    uploaded_image_skills = st.file_uploader("Upload Skills Profile Picture", type=["jpg", "png"])
    if uploaded_image_skills is not None:
        st.image(uploaded_image_skills, width=150, caption="Skills Profile Picture")
    else:
        st.image("person.jpg", width=150, caption="Skills Default Image")

    # Programming Skills
    st.subheader("Programming Skills")
    skills_python = st.slider("Python", 0, 100, 90)
    st.progress(skills_python)
    skills_js = st.slider("JavaScript", 0, 100, 70)
    st.progress(skills_js)
    skills_AI = st.slider("Artificial Intelligence", 0, 100, 50)
    st.progress(skills_AI)
    skills_web = st.slider("Web Development", 0, 100, 80)
    st.progress(skills_web)

    # Certifications and Achievements
    st.subheader("Certifications and Achievements")
    st.write("✔ Completed Google Data Analytics Certification")
    st.write("✔ Certified AI in Research and Course")

    # Testimonials
    st.subheader("Testimonials")
    for testimonial in testimonials:
        st.write(f"💬 {testimonial}")

# --- CONTACT ---
elif page == "Contact":
    st.title("📞 Contact Information")
    st.write("Feel free to reach out to me!")

    # Contact Form
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Send")

    # Display Contact Links
    st.write("**Connect with me:**")
    st.write("- LinkedIn: [your-linkedin-profile]")
    st.write("- GitHub: [your-github-profile]")
    st.write("- Portfolio Website: [your-portfolio-website]")
    st.write("- Email: [your-email-address]")

# --- FOOTER ---
st.markdown("---")
st.write("© 2023 RUGERO Alva Victor")
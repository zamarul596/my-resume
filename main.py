import streamlit as st
from PIL import Image

# --- PAGE CONFIG ---
st.set_page_config(page_title="My Resume", page_icon="📄", layout="centered")

# --- CUSTOM CSS FOR STYLE ---
st.markdown("""
    <style>
        .main {
            background-color: #f4f6f8;
        }
        .resume-header {
            display: flex;
            align-items: center;
            gap: 2rem;
            margin-bottom: 2rem;
        }
        .profile-pic {
            border-radius: 16px;
            border: 3px solid #2e8cff;
            width: 160px;
            height: 160px;
            object-fit: cover;
            box-shadow: 0 2px 10px rgba(46,140,255,0.1);
        }
        .section-title {
            color: #2e8cff;
            letter-spacing: 1px;
            font-weight: 700;
            margin-top: 1.5rem;
        }
        .divider {
            border: none;
            border-top: 2px solid #e2e6ea;
            margin: 1.5rem 0;
        }
        .item-title {
            font-weight: 600;
        }
    </style>
""", unsafe_allow_html=True)

# --- PERMANENT PROFILE DATA (EDIT HERE) ---
PERMANENT_INFO = {
    "full_name": "ZAMARUL HISYAM BIN MOHD ZAINI",
    "email": "zamarulhisyam1611@gmail.com",
    "phone": "014-8115198",
    "linkedin": "https://www.linkedin.com/in/zamarul-hisyam-9a1a25366/",
    "github": "https://github.com/zamarul596",
    "profile_img_path": "WhatsApp Image 2025-10-01 at 09.28.10_c1808e1d.jpg",
    "edu_school": "University Malaysia Kelantan",
    "edu_degree": "Bachelor of Information Technology",
    "edu_year": "2022 - 2026",
    "edu_desc": "A Bachelor of Information Technology student at University Malaysia Kelantan, tracking in Artificial Intelligence (AI) with strong skills in software development and data analysis.",
    "skills": ["Python", "Dart", "AI", "Java", "Firebase", "Flutter", "VS Code"],
    "achievements": [
        {"desc": "Top 10, Big Spark 2024"},
        {"desc": "Top 30, The Next Big Thing Start Up Competition 2024/2025"},
        {"desc": "Swiss Innovation Competition (SIC) 2025"},
        {"desc": "Trailblazer Cup 2025 (2nd Runner Up)"},
        {"desc": "Virtual Innovation Competition (VIC) 2024 (Gold Medal)"}
    ],
    "extracurricular_activities": [
        {"tittle": "IoT Sensor Monitoring and Data Logging to Google Sheet Workshop"},
        {"desc": "Learn to create the dashboard using Node-Red"}
    ],
}

# --- HEADER WITH IMAGE ---
st.markdown('<div class="resume-header">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 3])
with col1:
    try:
        image = Image.open(PERMANENT_INFO["profile_img_path"])
        st.image(image, width=160, caption="Profile Photo", output_format="auto")
    except Exception:
        st.warning("Profile image not found. Check 'profile_img_path'.")
with col2:
    st.markdown(f'<h1 style="margin-bottom:0;">{PERMANENT_INFO["full_name"]}</h1>', unsafe_allow_html=True)
    st.write("---")
st.markdown('</div>', unsafe_allow_html=True)

# --- PERSONAL INFO ---
st.markdown('<span class="section-title">Personal Information</span>', unsafe_allow_html=True)
st.write(f"**Email:** {PERMANENT_INFO['email']}  \n**Phone:** {PERMANENT_INFO['phone']}")
st.write(f"[LinkedIn]({PERMANENT_INFO['linkedin']}) | [GitHub]({PERMANENT_INFO['github']})")
st.markdown('<hr class="divider">', unsafe_allow_html=True)

# --- EDUCATION ---
st.markdown('<span class="section-title">Education</span>', unsafe_allow_html=True)
st.write(f"**{PERMANENT_INFO['edu_degree']}**, {PERMANENT_INFO['edu_school']} ({PERMANENT_INFO['edu_year']})")
st.write(PERMANENT_INFO['edu_desc'])
st.markdown('<hr class="divider">', unsafe_allow_html=True)

# --- SKILLS ---
st.markdown('<span class="section-title">Skills</span>', unsafe_allow_html=True)
skills_list = ", ".join(PERMANENT_INFO['skills']) if PERMANENT_INFO.get('skills') else "_No skills listed._"
st.write(skills_list)
st.markdown('<hr class="divider">', unsafe_allow_html=True)

# --- ACHIEVEMENTS ---
st.markdown('<span class="section-title">Achievements</span>', unsafe_allow_html=True)
achievements = PERMANENT_INFO.get("achievements", [])
if achievements:
    for ach in achievements:
        title = ach.get("title")
        desc = ach.get("desc")
        if title:
            st.write(f"**{title}**")
        if desc:
            st.write(desc)
else:
    st.write("_No achievements added yet._")
st.markdown('<hr class="divider">', unsafe_allow_html=True)

# --- EXTRACURRICULAR ACTIVITIES ---
st.markdown('<span class="section-title">Extracurricular Activities</span>', unsafe_allow_html=True)
activities = PERMANENT_INFO.get("extracurricular_activities", [])
if activities:
    for act in activities:
        st.write(f"- {act}")
else:
    st.write("_No extracurricular activities listed._")
st.markdown('<hr class="divider">', unsafe_allow_html=True)

# --- PREVIEW SECTION ---
st.markdown('<span class="section-title">Download or Preview</span>', unsafe_allow_html=True)
if st.button("Preview Resume"):
    st.markdown('<div style="background:white;padding:2rem;border-radius:20px;box-shadow:0 2px 12px rgba(46,140,255,0.05);">', unsafe_allow_html=True)

    # Header
    try:
        st.image(PERMANENT_INFO["profile_img_path"], width=140)
    except Exception:
        pass
    st.markdown(f"## {PERMANENT_INFO['full_name']}")
    st.write(f"**Email:** {PERMANENT_INFO['email']}  \n**Phone:** {PERMANENT_INFO['phone']}")
    st.write(f"[LinkedIn]({PERMANENT_INFO['linkedin']}) | [GitHub]({PERMANENT_INFO['github']})")
    st.markdown('---')

    # Education
    st.markdown("### Education")
    st.write(f"**{PERMANENT_INFO['edu_degree']}**, {PERMANENT_INFO['edu_school']} ({PERMANENT_INFO['edu_year']})")
    st.write(PERMANENT_INFO['edu_desc'])
    st.markdown('---')

    # Skills
    st.markdown("### Skills")
    st.write(skills_list)
    st.markdown('---')

    # Achievements
    st.markdown("### Achievements")
    if achievements:
        for ach in achievements:
            if ach.get("title"):
                st.write(f"**{ach['title']}**")
            if ach.get("desc"):
                st.write(ach["desc"])
    else:
        st.write("_No achievements listed._")
    st.markdown('---')

    # Extracurricular Activities
    st.markdown("### Extracurricular Activities")
    if activities:
        for act in activities:
            if ach.get("title"):
                st.write(f"**{ach['title']}**")
            if ach.get("desc"):
                st.write(ach["desc"])
    else:
        st.write("_No extracurricular activities listed._")
    st.markdown('---')

    st.markdown('</div>', unsafe_allow_html=True)

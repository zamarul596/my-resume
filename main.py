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
        .info-text {
            font-size: 1.1rem;
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
        .skill-badge {
            display: inline-block;
            background: #eaf4fe;
            color: #2e8cff;
            padding: 0.3em 0.8em;
            margin: 0.2em 0.3em 0.2em 0;
            border-radius: 8px;
            font-size: 1em;
        }
    </style>
""", unsafe_allow_html=True)

# --- PERMANENT PROFILE DATA ---
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
    "skills": ["Python", "Dart", "AI", "Java", "Firebase", "Flutter", "VS Code"]
}

# --- HEADER WITH IMAGE ---
st.markdown('<div class="resume-header">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 3])
with col1:
    image = Image.open(PERMANENT_INFO["profile_img_path"])
    st.image(image, width=160, caption="Profile Photo", output_format="auto")
with col2:
    st.markdown(f'<h1 style="margin-bottom:0;">{PERMANENT_INFO["full_name"]}</h1>', unsafe_allow_html=True)
    st.write("Showcase your profile in style")
    st.write("---")
st.markdown('</div>', unsafe_allow_html=True)

# --- BASIC INFO ---
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
st.markdown("".join([f'<span class="skill-badge">{s}</span>' for s in PERMANENT_INFO['skills']]), unsafe_allow_html=True)
st.markdown('<hr class="divider">', unsafe_allow_html=True)

# --- PROJECTS & ACHIEVEMENTS ---
st.markdown('<span class="section-title">Projects & Achievements</span>', unsafe_allow_html=True)
st.info("Add your Achievements & Projects below. They will be appended to your permanent resume but are not editable after refresh.")
achievement_projects = st.session_state.get("achievement_projects", [])

with st.form("achieve_form", clear_on_submit=True):
    title = st.text_input("Achievement/Project Title")
    desc = st.text_area("Description")
    submitted = st.form_submit_button("Add Achievement / Project")
    if submitted and (title or desc):
        achievement_projects.append({"title": title.strip(), "desc": desc.strip()})
        st.session_state["achievement_projects"] = achievement_projects

# Display all achievements
if achievement_projects:
    for item in achievement_projects:
        if item["title"]:
            st.write(f"**{item['title']}**")
        if item["desc"]:
            st.write(item["desc"])
else:
    st.write("No achievements/projects added yet.")

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# --- DOWNLOAD SECTION / PREVIEW ---
st.markdown('<span class="section-title">Download or Preview</span>', unsafe_allow_html=True)
if st.button("Preview Resume"):
    st.markdown('<div style="background:white;padding:2rem;border-radius:20px;box-shadow:0 2px 12px rgba(46,140,255,0.05);">', unsafe_allow_html=True)
    st.image(PERMANENT_INFO["profile_img_path"], width=160)
    
    st.markdown(f"## {PERMANENT_INFO['full_name']}")
    st.write(f"**Email:** {PERMANENT_INFO['email']}  \n**Phone:** {PERMANENT_INFO['phone']}")
    st.write(f"[LinkedIn]({PERMANENT_INFO['linkedin']}) | [GitHub]({PERMANENT_INFO['github']})")
    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    st.markdown("### Education")
    st.write(f"**{PERMANENT_INFO['edu_degree']}**, {PERMANENT_INFO['edu_school']} ({PERMANENT_INFO['edu_year']})")
    st.write(PERMANENT_INFO['edu_desc'])
    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    st.markdown("### Skills")
    st.markdown("".join([f'<span class="skill-badge">{s}</span>' for s in PERMANENT_INFO['skills']]), unsafe_allow_html=True)
    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    st.markdown("### Projects & Achievements")
    if achievement_projects:
        for item in achievement_projects:
            if item["title"]:
                st.write(f"**{item['title']}**")
            if item["desc"]:
                st.write(item["desc"])
    else:
        st.write("_No achievements/projects listed yet._")
    st.markdown('</div>', unsafe_allow_html=True)

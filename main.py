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
        .skill-badge {
            display: inline-block;
            background: #eaf4fe;
            color: #2e8cff;
            padding: 0.3em 0.8em;
            margin: 0.2em 0.3em 0.2em 0;
            border-radius: 8px;
            font-size: 1em;
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
    # Add or edit achievements here
    "achievements": [
        {
            "desc": "Top 10, Big Spark 2024"
        },
        {
            "desc": "Top 30, The Next Big Thing Start Up Competition 2024/2025"
        },
          {
            "desc": "Swiss Innovation Competition (SIC) 2025"
        },
              {
            "desc": "Trailblazer Cup 2025 (2nd Runner Up)"
        },
               {
            "desc": "Virtual Innovation Competition (VIC) 2024 (Gold Medal)"
        }
    ],

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
    st.write("Showcase your profile in style")
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
st.markdown("".join([f'<span class="skill-badge">{s}</span>' for s in PERMANENT_INFO['skills']]), unsafe_allow_html=True)
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

# --- PROJECTS (optional) ---
st.markdown('<span class="section-title">Projects</span>', unsafe_allow_html=True)
projects = PERMANENT_INFO.get("projects", [])
if projects:
    for proj in projects:
        title = proj.get("title")
        desc = proj.get("desc")
        link = proj.get("link")
        if title:
            if link:
                st.write(f"**{title}** – [{link}]({link})")
            else:
                st.write(f"**{title}**")
        if desc:
            st.write(desc)
else:
    st.write("_No projects added yet._")
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
    st.markdown("".join([f'<span class="skill-badge">{s}</span>' for s in PERMANENT_INFO['skills']]), unsafe_allow_html=True)
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

    # Projects
    st.markdown("### Projects")
    if projects:
        for proj in projects:
            if proj.get("title"):
                if proj.get("link"):
                    st.write(f"**{proj['title']}** – [{proj['link']}]({proj['link']})")
                else:
                    st.write(f"**{proj['title']}**")
            if proj.get("desc"):
                st.write(proj["desc"])
    else:
        st.write("_No projects listed._")

    st.markdown('</div>', unsafe_allow_html=True)

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

# --- HEADER WITH IMAGE ---
st.markdown('<div class="resume-header">', unsafe_allow_html=True)

# Profile Picture Upload
col1, col2 = st.columns([1,3])
with col1:
    profile_pic_file = st.file_uploader("Upload Your Photo", type=["png", "jpg", "jpeg"])
    if profile_pic_file:
        image = Image.open(profile_pic_file)
        st.image(image, use_column_width=True, output_format="JPEG", caption="Profile Photo")
    else:
        # Use your local image as the default profile photo
        st.image("WhatsApp Image 2025-10-01 at 09.28.10_c1808e1d.jpg", width=160, caption="Profile Photo")

with col2:
    st.markdown('<h1 style="margin-bottom:0;">My Resume</h1>', unsafe_allow_html=True)
    st.write("Showcase your profile in style 🚀")
    st.write("---")
st.markdown('</div>', unsafe_allow_html=True)

# --- BASIC INFO ---
st.markdown('<span class="section-title">Personal Information</span>', unsafe_allow_html=True)
full_name = st.text_input("Full Name", placeholder="ZAMARUL HISYAM BIN MOHD ZAINI")
email = st.text_input("Email", placeholder="zamarulhisyam1611@gmail.com")
phone = st.text_input("Phone Number", placeholder="014-8115198")
linkedin = st.text_input("LinkedIn", placeholder="https://www.linkedin.com/in/zamarul-hisyam-9a1a25366/")
github = st.text_input("GitHub (optional)", placeholder="https://github.com/zamarul596")

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# --- EDUCATION ---
st.markdown('<span class="section-title">Education</span>', unsafe_allow_html=True)
with st.expander("Education Details", expanded=True):
    edu_school = st.text_input("University", value="University Malaysia Kelantan")
    edu_degree = st.text_input("Degree", value="Bachelor of Information Technology")
    edu_year = st.text_input("Year / Duration", placeholder="2022 - 2026")
    edu_desc = st.text_area("Description (optional)", placeholder="A Bachelor of Information Technology student at University Malaysia Kelantan track in Artificial Intelligent (AI) with strong skills ...")

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# --- SKILLS ---
st.markdown('<span class="section-title">Skills</span>', unsafe_allow_html=True)
skills_input = st.text_area("List your key skills (separated by commas)", placeholder="Python, Dart, AI, Java, Firebase, Flutter, VS code")
skills = [skill.strip() for skill in skills_input.split(',') if skill.strip()]

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# --- PROJECTS & ACHIEVEMENTS ---
st.markdown('<span class="section-title">Projects & Achievements</span>', unsafe_allow_html=True)
achievements = []
with st.expander("Achievements & Projects", expanded=True):
    for i in range(1, 6):
        title = st.text_input(f"Achievement/Project Title {i}", key=f"title_{i}")
        desc = st.text_area(f"Description {i}", key=f"desc_{i}")
        if title or desc:
            achievements.append((title, desc))

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# --- DOWNLOAD SECTION / PREVIEW ---
st.markdown('<span class="section-title">Download or Preview</span>', unsafe_allow_html=True)
if st.button("Preview Resume"):
    st.markdown('<div style="background:white;padding:2rem;border-radius:20px;box-shadow:0 2px 12px rgba(46,140,255,0.05);">', unsafe_allow_html=True)
    # Profile Image
    if profile_pic_file:
        st.image(image, width=160)
    else:
        st.image("WhatsApp Image 2025-10-01 at 09.28.10_c1808e1d.jpg", width=160)

    st.markdown(f"## {full_name}")
    st.write(f"**Email:** {email}  \n**Phone:** {phone}")
    if linkedin:
        st.write(f"[LinkedIn]({linkedin})")
    if github:
        st.write(f"[GitHub]({github})")
    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    st.markdown("### 🎓 Education")
    st.write(f"**{edu_degree}**, {edu_school} ({edu_year})")
    st.write(edu_desc)
    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    st.markdown("### 🛠️ Skills")
    if skills:
        st.markdown("".join([f'<span class="skill-badge">{s}</span>' for s in skills]), unsafe_allow_html=True)
    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    st.markdown("### 🏆 Projects & Achievements")
    for title, desc in achievements:
        if title:
            st.write(f"**{title}**")
        if desc:
            st.write(desc)
    st.markdown('</div>', unsafe_allow_html=True)

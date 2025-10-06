# resume_page.py
import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="My Resume", page_icon="📄", layout="centered")

# --- HEADER ---
st.title("My Resume")
st.write("---")

# --- BASIC INFO ---
st.header("Personal Information")

full_name = st.text_input("Full Name", placeholder="ZAMARUL HISYAM BIN MOHD ZAINI")
email = st.text_input("Email", placeholder="zamarulhisyam1611@gmail.com")
phone = st.text_input("Phone Number", placeholder="014-8115198")
linkedin = st.text_input("LinkedIn", placeholder="https://www.linkedin.com/in/zamarul-hisyam-9a1a25366/")
github = st.text_input("GitHub (optional)", placeholder="https://github.com/zamarul596")

st.write("---")

# --- EDUCATION ---
st.header("Education")

with st.expander("Education Details"):
    edu_school = st.text_input("University Malaysia Kelantan")
    edu_degree = st.text_input("Bachelor of Information Technology")
    edu_year = st.text_input("Year / Duration", placeholder="2022 - 2026")
    edu_desc = st.text_area("Description (optional)", placeholder="A Bachelor of Information Technology student at University Malaysia Kelantan track in Artificial Intelligent (AI) with strong skills in digital technology and programming. Passionate about developing innovative solutions and AI.  Experience in software development, databases, and sustainability-focused systems.  Participated in national innovation competitions, to delivered a real-world tech solutions and strengthened problem-solving and teamwork skills. ")

st.write("---")


# --- SKILLS ---
st.header("Skills")

skills = st.text_area("List your key skills (separated by commas)", placeholder="Python, Dart, AI, Java, Firebase, Flutter, VS code")

st.write("---")

# --- PROJECTS & ACHIEVEMENTS ---
st.header("Projects / Achievements")

with st.expander("Achievement"):
     proj_title = st.text_input("Achievement")
     proj_desc = st.text_area("Description", placeholder="Top 10, Big Spark 2024")
     proj_desc = st.text_area("Description", placeholder="Top 30, The Next Big Thing Start Up Competition 2024/2025")
     proj_desc = st.text_area("Description", placeholder="Particip[ated in Swiss Innovation Competition (SIC) 2025")
     proj_desc = st.text_area("Description", placeholder="Trailblazer Cup 2025 (2nd Runner Up)")
     proj_desc = st.text_area("Description", placeholder="Virtual Innovation Competition (VIC) 2024 (Gold Medal)")


st.write("---")

# --- DOWNLOAD SECTION ---
st.header("Download or Preview")

if st.button("Preview Resume"):
    st.subheader(full_name)
    st.write(f"{email}")
    st.write(f"{phone}")
    st.write(f"[LinkedIn]({linkedin})")
    if github:
        st.write(f"[GitHub]({github})")

    st.write("### Education")
    st.write(f"**{edu_degree}**, {edu_school} ({edu_year})")
    st.write(edu_desc)

    st.write("### Experience")
    st.write(f"{work_company} ({work_duration})")
    st.write(work_desc)

    st.write("### Skills")
    st.write(skills)

    st.write("### Projects / Achievements")
    st.write(f"**{proj_title}** — {proj_link}")
    st.write(proj_desc)

st.write("---")



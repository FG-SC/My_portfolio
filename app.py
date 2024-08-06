from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.docx"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Felipe Gabriel"
PAGE_ICON = ":wave:"
NAME = "Felipe Gabriel"
DESCRIPTION = """
Data Scientist, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "felipegabriel.mecanica@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/@manecoda",
    "LinkedIn": "https://www.linkedin.com/in/felipe-gabriel0/",
    "GitHub": "https://github.com/FG-SC",
    "Medium": "https://medium.com/@felipegabriel.mecanica",
}
PROJECTS = {
    "🏆 Recommendation System Dashboard - Anime recommendation using MAL's users database": "https://youtu.be/Sb0A9i6d320",
    "🏆 Real Estate Tracker - Web app with MongoDB database": "https://real-state-floripa.streamlit.app/",
    "🏆 Stock Portfolio - Stocks selection using MF and analytics to combine Python & Excel": " ",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")



# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
    

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 4 Years experience extracting actionable insights from data and research
- ✔️ Strong hands on experience and knowledge in Python
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL
- 📊 Data Visualization: MS Excel, Plotly
- 📚 Modeling: SKlearn, TF
- 🗄️ Databases: MongoDB
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")


# --- CURRENT JOB
st.write("🚧", "**Head of Research | [Runes Land](runes.land)**")
st.write("01/2024 - now")
st.write(
    """
- ► Led a research team of 3 for market reports for guidance.
- ► Developed dashboards for data visualization and analytics.
"""
)

# --- JOB 1
st.write("🚧", "**Quant Analyst | [Zaros Finance](https://www.linkedin.com/company/zaroslabs/)**")
st.write("05/2023 - 09/2023")
st.write(
    """
- ► Conducted crypto derivatives market research and analysis using machine learning techniques.
- ► Developed dashboards for data visualization and analytics.
- ► Created a development roadmap and KPIs for business areas.
"""
)

# --- JOB 2
st.write("🚧", "**Quant Analyst | [Kassandra Finance](https://www.linkedin.com/company/kassandra-dao/)**")
st.write("03/2022 - 10/2022")
st.write(
    """
- ► Developed portfolio modeling strategies for clients.
- ► Analyzed on-chain data and created reports for asset recommendations.
"""
)

# --- JOB 3
st.write("🚧", "**Quant Analyst Internship | [Wise&Trust](https://www.linkedin.com/company/disrux-startup-builder/)**")
st.write("01/2020 - 12/2021")
st.write(
    """
- ► Conducted portfolio modeling and backtesting for algorithmic trading.
- ► Researched and analyzed the crypto and crypto mining markets using machine learning techniques.
"""
)

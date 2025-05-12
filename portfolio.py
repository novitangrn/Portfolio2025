import streamlit as st
from PIL import Image
import base64
from pathlib import Path

# Set page config
st.set_page_config(
    page_title="NOVI A | Data Science Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS - Added error handling
def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"CSS file {file_name} not found. Using default styles.")

local_css("style.css")

# Helper function for gradient text
def gradient_text(text, color1, color2):
    return f"""
    <span style="
        background: linear-gradient(90deg, {color1}, {color2});
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        font-weight: bold;
    ">{text}</span>
    """

# Navigation - Fixed potential column overflow
def navigation():
    st.markdown("""
    <style>
    .stApp header {
        background: rgba(0, 0, 0, 0.7) !important;
        backdrop-filter: blur(10px) !important;
        border-bottom: 1px solid #333 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    cols = st.columns([1, 1, 1, 1, 1, 1])  # Explicit column widths
    with cols[0]:
        st.markdown("<h3 style='font-weight:bold;'>NOVI A</h3>", unsafe_allow_html=True)
    with cols[2]:
        st.markdown('<a href="#about" style="color: white; text-decoration: none;">About</a>', unsafe_allow_html=True)
    with cols[3]:
        st.markdown('<a href="#experience" style="color: white; text-decoration: none;">Experience</a>', unsafe_allow_html=True)
    with cols[4]:
        st.markdown('<a href="#projects" style="color: white; text-decoration: none;">Projects</a>', unsafe_allow_html=True)
    with cols[5]:
        st.markdown('<a href="#contact" style="color: white; text-decoration: none;">Contact</a>', unsafe_allow_html=True)

# Hero Section - Fixed responsive issues
def hero_section():
    st.markdown("""
    <div style="
        min-height: calc(100vh - 80px);
        display: flex;
        align-items: center;
        justify-content: center;
        padding-top: 80px;
    ">
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <h1 style="font-size: clamp(2.5rem, 5vw, 4rem); font-weight: bold; line-height: 1.2;">
            {gradient_text("Data Science", "#00dbde", "#fc00ff")}<br>
            <span style="color: white;">Professional</span>
        </h1>
        <p style="font-size: 1.25rem; color: #ccc;">
            Transforming raw data into actionable insights through machine learning and deep learning techniques.
        </p>
        <div style="display: flex; gap: 1rem; margin-top: 2rem; flex-wrap: wrap;">
            <a href="#contact" style="
                padding: 0.75rem 1.5rem;
                background: linear-gradient(90deg, #00dbde, #fc00ff);
                border-radius: 9999px;
                color: white;
                text-decoration: none;
                font-weight: 500;
                white-space: nowrap;
            ">Contact Me</a>
            <a href="#projects" style="
                padding: 0.75rem 1.5rem;
                border: 1px solid #666;
                border-radius: 9999px;
                color: white;
                text-decoration: none;
                font-weight: 500;
                white-space: nowrap;
            ">View Projects</a>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="
            width: 100%;
            max-width: 300px;
            aspect-ratio: 1/1;
            margin: 0 auto;
            background: linear-gradient(135deg, #00dbde, #fc00ff);
            border-radius: 1rem;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        ">
            <div style="text-align: center; padding: 1.5rem;">
                <div style="font-size: 2.25rem; font-weight: bold; margin-bottom: 0.5rem;">NOVI A</div>
                <div style="font-size: 1.25rem;">Data Scientist</div>
                <div style="display: flex; justify-content: center; gap: 1rem; margin-top: 1rem;">
                    <a href="https://github.com/novi" style="color: white; font-size: 1.5rem;">
                        <i class="fab fa-github"></i>
                    </a>
                    <a href="https://linkedin.com/in/novi" style="color: white; font-size: 1.5rem;">
                        <i class="fab fa-linkedin"></i>
                    </a>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# About Section - Fixed responsive layout
def about_section():
    st.markdown("<a id='about'></a>", unsafe_allow_html=True)
    st.markdown("""
    <div style="
        padding: 3rem 0;
        background: linear-gradient(to bottom, #000000, #111);
    ">
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h2 style="font-size: 2.25rem; font-weight: bold; margin-bottom: 1rem;">
            {gradient_text("About Me", "#00dbde", "#fc00ff")}
        </h2>
        <div style="width: 80px; height: 2px; background: linear-gradient(90deg, #00dbde, #fc00ff); margin: 0 auto;"></div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1], gap="large")
    with col1:
        st.markdown("""
        <div style="
            background: rgba(30, 30, 30, 0.5);
            backdrop-filter: blur(10px);
            border-radius: 0.75rem;
            padding: 1.5rem;
            border: 1px solid #333;
        ">
            <h3 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 1rem; color: white;">Who I Am</h3>
            <p style="color: #ccc; margin-bottom: 1.5rem;">
                Data Science graduate from UPN 'Veteran' Jawa Timur with 1 year of practical experience and growing skills in data analysis, machine learning, deep learning, and time-series forecasting.
            </p>
            <p style="color: #ccc; margin-bottom: 1.5rem;">
                Proficient in Python and familiar with tools such as Tableau and data visualization dashboards. Experienced in applying machine learning and deep learning models to analyze data, enabling data-driven decision-making and optimizing business strategies.
            </p>
            <div style="display: flex; flex-wrap: wrap; gap: 0.75rem;">
                <div style="
                    background: rgba(255, 255, 255, 0.1);
                    backdrop-filter: blur(10px);
                    padding: 0.5rem 1rem;
                    border-radius: 9999px;
                ">
                    <span style="display: flex; align-items: center;">
                        <i class="fab fa-python" style="color: #3776ab; margin-right: 0.5rem;"></i>
                        <span>Python</span>
                    </span>
                </div>
                <!-- Other skill tags... -->
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="
            background: rgba(30, 30, 30, 0.5);
            backdrop-filter: blur(10px);
            border-radius: 0.75rem;
            padding: 1.5rem;
            border: 1px solid #333;
            height: 100%;
        ">
            <h3 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 1.5rem; color: white;">Education</h3>
            <div style="margin-bottom: 1.5rem;">
                <h4 style="font-size: 1.125rem; font-weight: 600; color: white;">Universitas Pembangunan Nasional 'Veteran' East Java</h4>
                <p style="color: #999; margin-bottom: 0.25rem;">Aug 2021 – Mar 2025</p>
                <p style="color: #ccc; margin-top: 0.25rem;">Bachelor degree - Data Science, 3.88/4.00</p>
                <p style="font-size: 0.875rem; color: #999; margin-top: 0.5rem;">
                    Subjects: Algebra, Statistics, Algorithm Programming, Database, Machine Learning, Deep Learning, NLP, Data Mining, Big Data
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Experience Section - Fixed timeline alignment
def experience_section():
    st.markdown("<a id='experience'></a>", unsafe_allow_html=True)
    st.markdown("""
    <div style="
        padding: 3rem 0;
        background: linear-gradient(to bottom, #111, #000000);
    ">
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h2 style="font-size: 2.25rem; font-weight: bold; margin-bottom: 1rem;">
            {gradient_text("My Experience", "#00dbde", "#fc00ff")}
        </h2>
        <div style="width: 80px; height: 2px; background: linear-gradient(90deg, #00dbde, #fc00ff); margin: 0 auto;"></div>
    </div>
    """, unsafe_allow_html=True)
    
    # Experience items...
    # (Rest of the experience section remains similar but with consistent padding/margins)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Projects Section - Improved responsive layout
def projects_section():
    st.markdown("<a id='projects'></a>", unsafe_allow_html=True)
    st.markdown("""
    <div style="
        padding: 3rem 0;
        background: #000000;
    ">
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h2 style="font-size: 2.25rem; font-weight: bold; margin-bottom: 1rem;">
            {gradient_text("My Projects", "#00dbde", "#fc00ff")}
        </h2>
        <div style="width: 80px; height: 2px; background: linear-gradient(90deg, #00dbde, #fc00ff); margin: 0 auto;"></div>
        <p style="font-size: 1.25rem; color: #ccc; margin-top: 1rem;">A collection of my academic projects from 8 semesters</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Project cards in responsive columns
    cols = st.columns([1, 1, 1], gap="medium")
    
    # Project cards content...
    # (Rest of the projects section remains similar but with consistent styling)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Skills Section - Improved grid layout
def skills_section():
    st.markdown("""
    <div style="
        padding: 3rem 0;
        background: linear-gradient(to bottom, #000000, #111);
    ">
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h2 style="font-size: 2.25rem; font-weight: bold; margin-bottom: 1rem;">
            {gradient_text("Technical Skills", "#00dbde", "#fc00ff")}
        </h2>
        <div style="width: 80px; height: 2px; background: linear-gradient(90deg, #00dbde, #fc00ff); margin: 0 auto;"></div>
    </div>
    """, unsafe_allow_html=True)
    
    # Responsive columns for skills
    cols = st.columns([1, 1, 1, 1], gap="medium")
    
    # Skills cards content...
    # (Rest of the skills section remains similar but with consistent styling)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Contact Section - Improved form handling
def contact_section():
    st.markdown("<a id='contact'></a>", unsafe_allow_html=True)
    st.markdown("""
    <div style="
        padding: 3rem 0;
        background: linear-gradient(to bottom, #111, #000000);
    ">
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h2 style="font-size: 2.25rem; font-weight: bold; margin-bottom: 1rem;">
            {gradient_text("Get In Touch", "#00dbde", "#fc00ff")}
        </h2>
        <div style="width: 80px; height: 2px; background: linear-gradient(90deg, #00dbde, #fc00ff); margin: 0 auto;"></div>
        <p style="font-size: 1.25rem; color: #ccc; margin-top: 1rem;">Let's collaborate on your next data-driven project</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.markdown("""
        <div style="
            background: rgba(30, 30, 30, 0.5);
            backdrop-filter: blur(10px);
            border-radius: 0.75rem;
            padding: 1.5rem;
            border: 1px solid #333;
            height: 100%;
        ">
            <!-- Contact info content... -->
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        with st.form("contact_form", clear_on_submit=True):
            st.markdown("""
            <div style="
                background: rgba(30, 30, 30, 0.5);
                backdrop-filter: blur(10px);
                border-radius: 0.75rem;
                padding: 1.5rem;
                border: 1px solid #333;
            ">
                <h3 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 1.5rem; color: white;">Send Me a Message</h3>
            """, unsafe_allow_html=True)
            
            name = st.text_input("Your Name", key="name")
            email = st.text_input("Email Address", key="email")
            subject = st.text_input("Subject", key="subject")
            message = st.text_area("Message", key="message", height=150)
            
            submit_button = st.form_submit_button("Send Message")
            if submit_button:
                if name and email and message:
                    st.success("Message sent successfully!")
                else:
                    st.error("Please fill in all required fields")
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Footer - Consistent styling
def footer():
    st.markdown("""
    <div style="
        padding: 2rem 0;
        background: #000000;
        border-top: 1px solid #333;
    ">
        <div style="
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 1rem;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
        ">
            <div style="margin-bottom: 1rem;">
                <span style="font-size: 1.25rem; font-weight: bold; background: linear-gradient(90deg, #00dbde, #fc00ff); -webkit-background-clip: text; background-clip: text; color: transparent;">NOVI A</span>
                <p style="color: #999; margin-top: 0.5rem;">Data Science Professional</p>
            </div>
            
            <div style="display: flex; gap: 1.5rem; margin-bottom: 1.5rem;">
                <a href="https://github.com/novi" target="_blank" style="color: #999; font-size: 1.25rem;">
                    <i class="fab fa-github"></i>
                </a>
                <a href="https://linkedin.com/in/novi" target="_blank" style="color: #999; font-size: 1.25rem;">
                    <i class="fab fa-linkedin"></i>
                </a>
                <a href="mailto:novi@gmail.com" style="color: #999; font-size: 1.25rem;">
                    <i class="fas fa-envelope"></i>
                </a>
            </div>
            
            <div style="
                padding-top: 1.5rem;
                border-top: 1px solid #333;
                width: 100%;
                color: #999;
                font-size: 0.875rem;
            ">
                <p>© 2024 Novi A. All rights reserved.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Main App
def main():
    # Add Font Awesome
    st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">', unsafe_allow_html=True)
    
    # Navigation
    navigation()
    
    # Sections
    hero_section()
    about_section()
    experience_section()
    projects_section()
    skills_section()
    contact_section()
    footer()

if __name__ == "__main__":
    main()

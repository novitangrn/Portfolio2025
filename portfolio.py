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

# Custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

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

# Navigation
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
    
    cols = st.columns(6)
    with cols[0]:
        st.markdown("<h3 style='font-weight:bold;'>NOVI A</h3>", unsafe_allow_html=True)
    with cols[2]:
        st.page_link("#about", label="About")
    with cols[3]:
        st.page_link("#experience", label="Experience")
    with cols[4]:
        st.page_link("#projects", label="Projects")
    with cols[5]:
        st.page_link("#contact", label="Contact")

# Hero Section
def hero_section():
    st.markdown("""
    <div style="
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        padding-top: 80px;
    ">
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <h1 style="font-size: 4rem; font-weight: bold; line-height: 1.2;">
            {gradient_text("Data Science", "#00dbde", "#fc00ff")}<br>
            <span style="color: white;">Professional</span>
        </h1>
        <p style="font-size: 1.25rem; color: #ccc;">
            Transforming raw data into actionable insights through machine learning and deep learning techniques.
        </p>
        <div style="display: flex; gap: 1rem; margin-top: 2rem;">
            <a href="#contact" style="
                padding: 0.75rem 2rem;
                background: linear-gradient(90deg, #00dbde, #fc00ff);
                border-radius: 9999px;
                color: white;
                text-decoration: none;
                font-weight: 500;
            ">Contact Me</a>
            <a href="#projects" style="
                padding: 0.75rem 2rem;
                border: 1px solid #666;
                border-radius: 9999px;
                color: white;
                text-decoration: none;
                font-weight: 500;
            ">View Projects</a>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="
            width: 300px;
            height: 300px;
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

# About Section
def about_section():
    st.markdown("<a id='about'></a>", unsafe_allow_html=True)
    st.markdown("""
    <div style="
        padding: 5rem 0;
        background: linear-gradient(to bottom, #000000, #111);
    ">
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 4rem;">
        <h2 style="font-size: 2.25rem; font-weight: bold; margin-bottom: 1rem;">
            {gradient_text("About Me", "#00dbde", "#fc00ff")}
        </h2>
        <div style="width: 80px; height: 2px; background: linear-gradient(90deg, #00dbde, #fc00ff); margin: 0 auto;"></div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div style="
            background: rgba(30, 30, 30, 0.5);
            backdrop-filter: blur(10px);
            border-radius: 0.75rem;
            padding: 2rem;
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
                <div style="
                    background: rgba(255, 255, 255, 0.1);
                    backdrop-filter: blur(10px);
                    padding: 0.5rem 1rem;
                    border-radius: 9999px;
                ">
                    <span style="display: flex; align-items: center;">
                        <i class="fas fa-database" style="color: #f29111; margin-right: 0.5rem;"></i>
                        <span>SQL</span>
                    </span>
                </div>
                <div style="
                    background: rgba(255, 255, 255, 0.1);
                    backdrop-filter: blur(10px);
                    padding: 0.5rem 1rem;
                    border-radius: 9999px;
                ">
                    <span style="display: flex; align-items: center;">
                        <i class="fas fa-brain" style="color: #8a2be2; margin-right: 0.5rem;"></i>
                        <span>Machine Learning</span>
                    </span>
                </div>
                <div style="
                    background: rgba(255, 255, 255, 0.1);
                    backdrop-filter: blur(10px);
                    padding: 0.5rem 1rem;
                    border-radius: 9999px;
                ">
                    <span style="display: flex; align-items: center;">
                        <i class="fas fa-chart-line" style="color: #2ecc71; margin-right: 0.5rem;"></i>
                        <span>Data Analysis</span>
                    </span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="
            background: rgba(30, 30, 30, 0.5);
            backdrop-filter: blur(10px);
            border-radius: 0.75rem;
            padding: 2rem;
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

# Experience Section
def experience_section():
    st.markdown("<a id='experience'></a>", unsafe_allow_html=True)
    st.markdown("""
    <div style="
        padding: 5rem 0;
        background: linear-gradient(to bottom, #111, #000000);
    ">
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 4rem;">
        <h2 style="font-size: 2.25rem; font-weight: bold; margin-bottom: 1rem;">
            {gradient_text("My Experience", "#00dbde", "#fc00ff")}
        </h2>
        <div style="width: 80px; height: 2px; background: linear-gradient(90deg, #00dbde, #fc00ff); margin: 0 auto;"></div>
    </div>
    """, unsafe_allow_html=True)
    
    # Experience 1
    st.markdown("""
    <div style="
        background: rgba(30, 30, 30, 0.5);
        backdrop-filter: blur(10px);
        border-radius: 0.75rem;
        padding: 2rem;
        border: 1px solid #333;
        margin-bottom: 3rem;
        position: relative;
        padding-left: 3rem;
    ">
        <div style="
            position: absolute;
            left: -16px;
            top: 0;
            bottom: -3rem;
            width: 2px;
            background: linear-gradient(to bottom, #00dbde, #fc00ff);
        "></div>
        <div style="
            position: absolute;
            left: -20px;
            top: 0;
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: linear-gradient(90deg, #00dbde, #fc00ff);
        "></div>
        
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
            <h3 style="font-size: 1.25rem; font-weight: bold; color: white;">BPBD of Surabaya – Data Analyst Intern</h3>
            <span style="background: rgba(0, 200, 200, 0.2); color: #00dbde; padding: 0.25rem 0.75rem; border-radius: 9999px; font-size: 0.875rem;">Feb 2024 – Jun 2024</span>
        </div>
        <p style="color: #999; margin-bottom: 1rem;">Surabaya City Regional Disaster Management Agency</p>
        <ul style="color: #ccc; list-style-type: none; padding-left: 0;">
            <li style="margin-bottom: 0.5rem; display: flex;">
                <span style="color: #00dbde; margin-right: 0.5rem;">•</span>
                <span>Designed and developed the agency's website database using SQL.</span>
            </li>
            <li style="margin-bottom: 0.5rem; display: flex;">
                <span style="color: #00dbde; margin-right: 0.5rem;">•</span>
                <span>Added over 5,000 historical data entries into the database.</span>
            </li>
            <li style="margin-bottom: 0.5rem; display: flex;">
                <span style="color: #00dbde; margin-right: 0.5rem;">•</span>
                <span>Organized incident and logistics data archives by implementing an efficient automated input format.</span>
            </li>
            <li style="display: flex;">
                <span style="color: #00dbde; margin-right: 0.5rem;">•</span>
                <span>Applied Natural Language Processing (NLP) to automate data entry from raw reports into the database.</span>
            </li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Experience 2
    st.markdown("""
    <div style="
        background: rgba(30, 30, 30, 0.5);
        backdrop-filter: blur(10px);
        border-radius: 0.75rem;
        padding: 2rem;
        border: 1px solid #333;
        margin-bottom: 3rem;
        position: relative;
        padding-left: 3rem;
    ">
        <div style="
            position: absolute;
            left: -16px;
            top: 0;
            bottom: -3rem;
            width: 2px;
            background: linear-gradient(to bottom, #00dbde, #fc00ff);
        "></div>
        <div style="
            position: absolute;
            left: -20px;
            top: 0;
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: linear-gradient(90deg, #00dbde, #fc00ff);
        "></div>
        
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
            <h3 style="font-size: 1.25rem; font-weight: bold; color: white;">Bangkit Academy 2023 Batch 2 - Machine Learning Cohort</h3>
            <span style="background: rgba(150, 0, 200, 0.2); color: #aa00ff; padding: 0.25rem 0.75rem; border-radius: 9999px; font-size: 0.875rem;">July 2023 – Jan 2024</span>
        </div>
        <p style="color: #999; margin-bottom: 1rem;">Academic program led by Google, GoTo, and Traveloka</p>
        <ul style="color: #ccc; list-style-type: none; padding-left: 0;">
            <li style="margin-bottom: 0.5rem; display: flex;">
                <span style="color: #aa00ff; margin-right: 0.5rem;">•</span>
                <span>Completed the Machine Learning path on Coursera ahead of schedule, gaining hands-on experience in key machine learning/deep learning concepts and techniques.</span>
            </li>
            <li style="margin-bottom: 0.5rem; display: flex;">
                <span style="color: #aa00ff; margin-right: 0.5rem;">•</span>
                <span>Developed a travel recommendation system using collaborative filtering to generate personalized itineraries based on user preferences and ratings data.</span>
            </li>
            <li style="display: flex;">
                <span style="color: #aa00ff; margin-right: 0.5rem;">•</span>
                <span>Implemented geospatial analysis algorithms to optimize travel routes by calculating distances between locations and minimizing travel time.</span>
            </li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Experience 3
    st.markdown("""
    <div style="
        background: rgba(30, 30, 30, 0.5);
        backdrop-filter: blur(10px);
        border-radius: 0.75rem;
        padding: 2rem;
        border: 1px solid #333;
        position: relative;
        padding-left: 3rem;
    ">
        <div style="
            position: absolute;
            left: -16px;
            top: 0;
            bottom: 0;
            width: 2px;
            background: linear-gradient(to bottom, #00dbde, #fc00ff);
        "></div>
        <div style="
            position: absolute;
            left: -20px;
            top: 0;
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: linear-gradient(90deg, #00dbde, #fc00ff);
        "></div>
        
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
            <h3 style="font-size: 1.25rem; font-weight: bold; color: white;">Meteorological Office (BMKG) Juanda - Meteorological Data Analyst Intern</h3>
            <span style="background: rgba(0, 100, 200, 0.2); color: #0077cc; padding: 0.25rem 0.75rem; border-radius: 9999px; font-size: 0.875rem;">Aug 2023 – Dec 2023</span>
        </div>
        <p style="color: #999; margin-bottom: 1rem;">Indonesian non-departmental government agency for meteorology</p>
        <ul style="color: #ccc; list-style-type: none; padding-left: 0;">
            <li style="margin-bottom: 0.5rem; display: flex;">
                <span style="color: #0077cc; margin-right: 0.5rem;">•</span>
                <span>Analyzed upper air and synoptic observation data in the form of time series.</span>
            </li>
            <li style="margin-bottom: 0.5rem; display: flex;">
                <span style="color: #0077cc; margin-right: 0.5rem;">•</span>
                <span>Built an ensemble model combining Random Forest, Gradient Boosting, and MLP Neural Network, achieving 82% accuracy in extreme weather prediction.</span>
            </li>
            <li style="margin-bottom: 0.5rem; display: flex;">
                <span style="color: #0077cc; margin-right: 0.5rem;">•</span>
                <span>Developed a web-based synoptic code validator to detect writing errors in code entries.</span>
            </li>
            <li style="display: flex;">
                <span style="color: #0077cc; margin-right: 0.5rem;">•</span>
                <span>Managed to create a dashboard to visualize observation data in the form of charts.</span>
            </li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Projects Section
def projects_section():
    st.markdown("<a id='projects'></a>", unsafe_allow_html=True)
    st.markdown("""
    <div style="
        padding: 5rem 0;
        background: #000000;
    ">
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 4rem;">
        <h2 style="font-size: 2.25rem; font-weight: bold; margin-bottom: 1rem;">
            {gradient_text("My Projects", "#00dbde", "#fc00ff")}
        </h2>
        <div style="width: 80px; height: 2px; background: linear-gradient(90deg, #00dbde, #fc00ff); margin: 0 auto;"></div>
        <p style="font-size: 1.25rem; color: #ccc; margin-top: 1rem;">A collection of my academic projects from 8 semesters</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Book Shelf (simplified)
    st.markdown("""
    <div style="
        height: 300px;
        margin-bottom: 5rem;
        position: relative;
        display: flex;
        justify-content: center;
        gap: 2rem;
    ">
        <!-- Shelf -->
        <div style="
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 20px;
            background: #333;
            border-radius: 4px;
        "></div>
        
        <!-- Books -->
        <div style="
            width: 80px;
            height: 240px;
            background: linear-gradient(to bottom, #0077cc, #0055aa);
            border-radius: 4px;
            position: relative;
            bottom: 0;
            transform-origin: bottom;
            transition: transform 0.3s ease;
        ">
            <div style="
                position: absolute;
                right: 0;
                top: 0;
                bottom: 0;
                width: 8px;
                background: rgba(0, 0, 0, 0.3);
                transform: rotateY(90deg) translateX(8px);
                transform-origin: left;
            "></div>
            <div style="
                padding: 1rem;
                height: 100%;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                transform: rotate(180deg);
                writing-mode: vertical-rl;
            ">
                <h3 style="font-size: 0.75rem; font-weight: bold; color: white;">QuantiNews</h3>
                <span style="font-size: 0.75rem; color: white;">2025</span>
            </div>
        </div>
        
        <div style="
            width: 90px;
            height: 260px;
            background: linear-gradient(to bottom, #aa00ff, #7700bb);
            border-radius: 4px;
            position: relative;
            bottom: 0;
            transform-origin: bottom;
            transition: transform 0.3s ease;
        ">
            <div style="
                position: absolute;
                right: 0;
                top: 0;
                bottom: 0;
                width: 8px;
                background: rgba(0, 0, 0, 0.3);
                transform: rotateY(90deg) translateX(8px);
                transform-origin: left;
            "></div>
            <div style="
                padding: 1rem;
                height: 100%;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                transform: rotate(180deg);
                writing-mode: vertical-rl;
            ">
                <h3 style="font-size: 0.75rem; font-weight: bold; color: white;">Amazon Prime DW</h3>
                <span style="font-size: 0.75rem; color: white;">2024</span>
            </div>
        </div>
        
        <div style="
            width: 85px;
            height: 250px;
            background: linear-gradient(to bottom, #00aa55, #007744);
            border-radius: 4px;
            position: relative;
            bottom: 0;
            transform-origin: bottom;
            transition: transform 0.3s ease;
        ">
            <div style="
                position: absolute;
                right: 0;
                top: 0;
                bottom: 0;
                width: 8px;
                background: rgba(0, 0, 0, 0.3);
                transform: rotateY(90deg) translateX(8px);
                transform-origin: left;
            "></div>
            <div style="
                padding: 1rem;
                height: 100%;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                transform: rotate(180deg);
                writing-mode: vertical-rl;
            ">
                <h3 style="font-size: 0.75rem; font-weight: bold; color: white;">CodeIgniter DB</h3>
                <span style="font-size: 0.75rem; color: white;">2024</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Project Cards
    cols = st.columns(3)
    
    with cols[0]:
        # Project 1
        st.markdown("""
        <div style="
            background: rgba(30, 30, 30, 0.5);
            backdrop-filter: blur(10px);
            border-radius: 0.75rem;
            padding: 1.5rem;
            border: 1px solid #333;
            margin-bottom: 2rem;
        ">
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <div style="
                    width: 40px;
                    height: 40px;
                    border-radius: 50%;
                    background: linear-gradient(to right, #0077cc, #00aaff);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin-right: 0.75rem;
                ">
                    <i class="fas fa-chart-line" style="color: white;"></i>
                </div>
                <h3 style="font-size: 1.25rem; font-weight: bold; color: white;">QuantiNews: Stock Prediction using STACN</h3>
            </div>
            <p style="color: #999; margin-bottom: 0.5rem;">2025</p>
            <p style="color: #ccc; margin-bottom: 1rem;">
                Developed an STACN model to predict price movements across 11 IDX-IC sectoral indices.
            </p>
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1rem;">
                <span style="padding: 0.25rem 0.5rem; background: rgba(0, 100, 200, 0.3); color: #00aaff; font-size: 0.75rem; border-radius: 9999px;">Python</span>
                <span style="padding: 0.25rem 0.5rem; background: rgba(0, 100, 200, 0.3); color: #00aaff; font-size: 0.75rem; border-radius: 9999px;">TensorFlow</span>
                <span style="padding: 0.25rem 0.5rem; background: rgba(0, 100, 200, 0.3); color: #00aaff; font-size: 0.75rem; border-radius: 9999px;">Streamlit</span>
            </div>
            <p style="font-size: 0.875rem; color: #999;">
                <span style="font-weight: 600; color: #00dbde;">Achievement:</span> Achieved a MAPE accuracy range of 0.69% to 2.3% across different sectors.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Project 4
        st.markdown("""
        <div style="
            background: rgba(30, 30, 30, 0.5);
            backdrop-filter: blur(10px);
            border-radius: 0.75rem;
            padding: 1.5rem;
            border: 1px solid #333;
        ">
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <div style="
                    width: 40px;
                    height: 40px;
                    border-radius: 50%;
                    background: linear-gradient(to right, #ffaa00, #ffcc00);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin-right: 0.75rem;
                ">
                    <i class="fas fa-check-circle" style="color: white;"></i>
                </div>
                <h3 style="font-size: 1.25rem; font-weight: bold; color: white;">Synop Validators</h3>
            </div>
            <p style="color: #999; margin-bottom: 0.5rem;">2023</p>
            <p style="color: #ccc; margin-bottom: 1rem;">
                Developed a logic program based on standard synoptic encoding rules to minimize code-writing errors.
            </p>
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1rem;">
                <span style="padding: 0.25rem 0.5rem; background: rgba(200, 150, 0, 0.3); color: #ffcc00; font-size: 0.75rem; border-radius: 9999px;">Python</span>
                <span style="padding: 0.25rem 0.5rem; background: rgba(200, 150, 0, 0.3); color: #ffcc00; font-size: 0.75rem; border-radius: 9999px;">Streamlit</span>
            </div>
            <p style="font-size: 0.875rem; color: #999;">
                <span style="font-weight: 600; color: #00dbde;">Impact:</span> Built and deployed the program as a website to improve data entry accuracy.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with cols[1]:
        # Project 2
        st.markdown("""
        <div style="
            background: rgba(30, 30, 30, 0.5);
            backdrop-filter: blur(10px);
            border-radius: 0.75rem;
            padding: 1.5rem;
            border: 1px solid #333;
            margin-bottom: 2rem;
        ">
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <div style="
                    width: 40px;
                    height: 40px;
                    border-radius: 50%;
                    background: linear-gradient(to right, #aa00ff, #cc44ff);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin-right: 0.75rem;
                ">
                    <i class="fas fa-database" style="color: white;"></i>
                </div>
                <h3 style="font-size: 1.25rem; font-weight: bold; color: white;">Amazon Prime Data Warehouse</h3>
            </div>
            <p style="color: #999; margin-bottom: 0.5rem;">2024</p>
            <p style="color: #ccc; margin-bottom: 1rem;">
                Designed a star schema data warehouse using Pentaho ETL, integrating, cleaning, and transforming raw data.
            </p>
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1rem;">
                <span style="padding: 0.25rem 0.5rem; background: rgba(150, 0, 200, 0.3); color: #cc44ff; font-size: 0.75rem; border-radius: 9999px;">Pentaho</span>
                <span style="padding: 0.25rem 0.5rem; background: rgba(150, 0, 200, 0.3); color: #cc44ff; font-size: 0.75rem; border-radius: 9999px;">Tableau</span>
                <span style="padding: 0.25rem 0.5rem; background: rgba(150, 0, 200, 0.3); color: #cc44ff; font-size: 0.75rem; border-radius: 9999px;">SQL</span>
            </div>
            <p style="font-size: 0.875rem; color: #999;">
                <span style="font-weight: 600; color: #00dbde;">Outcome:</span> Created dashboards analyzing user trends (churn/retention), device preferences, and revenue patterns.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Project 5
        st.markdown("""
        <div style="
            background: rgba(30, 30, 30, 0.5);
            backdrop-filter: blur(10px);
            border-radius: 0.75rem;
            padding: 1.5rem;
            border: 1px solid #333;
        ">
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <div style="
                    width: 40px;
                    height: 40px;
                    border-radius: 50%;
                    background: linear-gradient(to right, #ff3333, #ff6666);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin-right: 0.75rem;
                ">
                    <i class="fas fa-clock" style="color: white;"></i>
                </div>
                <h3 style="font-size: 1.25rem; font-weight: bold; color: white;">Time Series Analysis</h3>
            </div>
            <p style="color: #999; margin-bottom: 0.5rem;">2023</p>
            <p style="color: #ccc; margin-bottom: 1rem;">
                Analyzed over 10,000 records of data using ARIMA, SARIMA, SARIMAX, and LSTM models.
            </p>
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1rem;">
                <span style="padding: 0.25rem 0.5rem; background: rgba(200, 0, 0, 0.3); color: #ff6666; font-size: 0.75rem; border-radius: 9999px;">Python</span>
                <span style="padding: 0.25rem 0.5rem; background: rgba(200, 0, 0, 0.3); color: #ff6666; font-size: 0.75rem; border-radius: 9999px;">LSTM</span>
                <span style="padding: 0.25rem 0.5rem; background: rgba(200, 0, 0, 0.3); color: #ff6666; font-size: 0.75rem; border-radius: 9999px;">ARIMA</span>
            </div>
            <p style="font-size: 0.875rem; color: #999;">
                <span style="font-weight: 600; color: #00dbde;">Achievement:</span> Studied trends in rainfall data parameters from 1982 to 2022, achieving a loss value of 0.8.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with cols[2]:
        # Project 3
        st.markdown("""
        <div style="
            background: rgba(30, 30, 30, 0.5);
            backdrop-filter: blur(10px);
            border-radius: 0.75rem;
            padding: 1.5rem;
            border: 1px solid #333;
            margin-bottom: 2rem;
        ">
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <div style="
                    width: 40px;
                    height: 40px;
                    border-radius: 50%;
                    background: linear-gradient(to right, #00aa55, #00cc77);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin-right: 0.75rem;
                ">
                    <i class="fas fa-code" style="color: white;"></i>
                </div>
                <h3 style="font-size: 1.25rem; font-weight: bold; color: white;">CodeIgniter Website Database</h3>
            </div>
            <p style="color: #999; margin-bottom: 0.5rem;">2024</p>
            <p style="color: #ccc; margin-bottom: 1rem;">
                Designed and implemented an optimized SQL database schema to support website functionality and data storage.
            </p>
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1rem;">
                <span style="padding: 0.25rem 0.5rem; background: rgba(0, 150, 0, 0.3); color: #00cc77; font-size: 0.75rem; border-radius: 9999px;">MySQL</span>
                <span style="padding: 0.25rem 0.5rem; background: rgba(0, 150, 0, 0.3); color: #00cc77; font-size: 0.75rem; border-radius: 9999px;">CodeIgniter</span>
                <span style="padding: 0.25rem 0.5rem; background: rgba(0, 150, 0, 0.3); color: #00cc77; font-size: 0.75rem; border-radius: 9999px;">PHP</span>
            </div>
            <p style="font-size: 0.875rem; color: #999;">
                <span style="font-weight: 600; color: #00dbde;">Result:</span> Integrated the database with a CodeIgniter backend, ensuring secure and efficient data handling.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Project 6
        st.markdown("""
        <div style="
            background: rgba(30, 30, 30, 0.5);
            backdrop-filter: blur(10px);
            border-radius: 0.75rem;
            padding: 1.5rem;
            border: 1px solid #333;
        ">
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <div style="
                    width: 40px;
                    height: 40px;
                    border-radius: 50%;
                    background: linear-gradient(to right, #ff33aa, #ff66cc);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin-right: 0.75rem;
                ">
                    <i class="fas fa-newspaper" style="color: white;"></i>
                </div>
                <h3 style="font-size: 1.25rem; font-weight: bold; color: white;">NLP News Topic Detection</h3>
            </div>
            <p style="color: #999; margin-bottom: 0.5rem;">2022</p>
            <p style="color: #ccc; margin-bottom: 1rem;">
                Collected and pre-processed news data using scraping techniques for text classification.
            </p>
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1rem;">
                <span style="padding: 0.25rem 0.5rem; background: rgba(200, 0, 100, 0.3); color: #ff66cc; font-size: 0.75rem; border-radius: 9999px;">Python</span>
                <span style="padding: 0.25rem 0.5rem; background: rgba(200, 0, 100, 0.3); color: #ff66cc; font-size: 0.75rem; border-radius: 9999px;">NLP</span>
                <span style="padding: 0.25rem 0.5rem; background: rgba(200, 0, 100, 0.3); color: #ff66cc; font-size: 0.75rem; border-radius: 9999px;">LDA</span>
            </div>
            <p style="font-size: 0.875rem; color: #999;">
                <span style="font-weight: 600; color: #00dbde;">Result:</span> Applied Latent Dirichlet Allocation (LDA) for topic modeling, achieving 89% accuracy.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Skills Section
def skills_section():
    st.markdown("""
    <div style="
        padding: 5rem 0;
        background: linear-gradient(to bottom, #000000, #111);
    ">
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 4rem;">
        <h2 style="font-size: 2.25rem; font-weight: bold; margin-bottom: 1rem;">
            {gradient_text("Technical Skills", "#00dbde", "#fc00ff")}
        </h2>
        <div style="width: 80px; height: 2px; background: linear-gradient(90deg, #00dbde, #fc00ff); margin: 0 auto;"></div>
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(4)
    
    with cols[0]:
        st.markdown("""
        <div style="
            background: rgba(30, 30, 30, 0.5);
            backdrop-filter: blur(10px);
            border-radius: 0.75rem;
            padding: 1.5rem;
            border: 1px solid #333;
            height: 100%;
        ">
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <div style="
                    width: 40px;
                    height: 40px;
                    border-radius: 50%;
                    background: linear-gradient(to right, #0077cc, #00aaff);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin-right: 0.75rem;
                ">
                    <i class="fas fa-code" style="color: white;"></i>
                </div>
                <h3 style="font-size: 1.25rem; font-weight: bold; color: white;">Programming</h3>
            </div>
            <div style="color: #ccc;">
                <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                    <i class="fab fa-python" style="color: #3776ab; margin-right: 0.5rem;"></i>
                    <span>Python</span>
                </div>
                <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                    <i class="fas fa-database" style="color: #f29111; margin-right: 0.5rem;"></i>
                    <span>SQL</span>
                </div>
                <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                    <i class="fab fa-php" style="color: #777bb3; margin-right: 0.5rem;"></i>
                    <span>PHP</span>
                </div>
                <div style="display: flex; align-items: center;">
                    <i class="fab fa-html5" style="color: #e34c26; margin-right: 0.5rem;"></i>
                    <span>HTML/CSS</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with cols[1]:
        st.markdown("""
        <div style="
            background: rgba(30, 30, 30, 0.5);
            backdrop-filter: blur(10px);
            border-radius: 0.75rem;
            padding: 1.5rem;
            border: 1px solid #333;
            height: 100%;
        ">
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <div style="
                    width: 40px;
                    height: 40px;
                    border-radius: 50%;
                    background: linear-gradient(to right, #aa00ff, #cc44ff);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin-right: 0.75rem;
                ">
                    <i class="fas fa-cubes" style="color: white;"></i>
                </div>
                <h3 style="font-size: 1.25rem; font-weight: bold; color: white;">Libraries & Frameworks</h3>
            </div>
            <div style="color: #ccc;">
                <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                    <i class="fas fa-brain" style="color: #8a2be2; margin-right: 0.5rem;"></i>
                    <span>TensorFlow/PyTorch</span>
                </div>
                <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                    <i class="fas fa-chart-bar" style="color: #2ecc71; margin-right: 0.5rem;"></i>
                    <span>Pandas/Scikit-learn</span>
                </div>
                <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                    <i class="fas fa-globe" style="color: #0077cc; margin-right: 0.5rem;"></i>
                    <span>Flask/CodeIgniter</span>
                </div>
                <div style="display: flex; align-items: center;">
                    <i class="fas fa-robot" style="color: #ffcc00; margin-right: 0.5rem;"></i>
                    <span>Hugging Face</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with cols[2]:
        st.markdown("""
        <div style="
            background: rgba(30, 30, 30, 0.5);
            backdrop-filter: blur(10px);
            border-radius: 0.75rem;
            padding: 1.5rem;
            border: 1px solid #333;
            height: 100%;
        ">
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <div style="
                    width: 40px;
                    height: 40px;
                    border-radius: 50%;
                    background: linear-gradient(to right, #00aa55, #00cc77);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin-right: 0.75rem;
                ">
                    <i class="fas fa-database" style="color: white;"></i>
                </div>
                <h3 style="font-size: 1.25rem; font-weight: bold; color: white;">Databases & ETL</h3>
            </div>
            <div style="color: #ccc;">
                <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                    <i class="fas fa-server" style="color: #0077cc; margin-right: 0.5rem;"></i>
                    <span>MySQL/MongoDB</span>
                </div>
                <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                    <i class="fas fa-cloud" style="color: #ffcc00; margin-right: 0.5rem;"></i>
                    <span>Google BigQuery</span>
                </div>
                <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                    <i class="fas fa-random" style="color: #aa00ff; margin-right: 0.5rem;"></i>
                    <span>Pentaho ETL</span>
                </div>
                <div style="display: flex; align-items: center;">
                    <i class="fas fa-bolt" style="color: #ff3333; margin-right: 0.5rem;"></i>
                    <span>PySpark</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with cols[3]:
        st.markdown("""
        <div style="
            background: rgba(30, 30, 30, 0.5);
            backdrop-filter: blur(10px);
            border-radius: 0.75rem;
            padding: 1.5rem;
            border: 1px solid #333;
            height: 100%;
        ">
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <div style="
                    width: 40px;
                    height: 40px;
                    border-radius: 50%;
                    background: linear-gradient(to right, #ff3333, #ff6666);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin-right: 0.75rem;
                ">
                    <i class="fas fa-tools" style="color: white;"></i>
                </div>
                <h3 style="font-size: 1.25rem; font-weight: bold; color: white;">Tools & Platforms</h3>
            </div>
            <div style="color: #ccc;">
                <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                    <i class="fas fa-chart-pie" style="color: #0077cc; margin-right: 0.5rem;"></i>
                    <span>Tableau/PowerBI</span>
                </div>
                <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                    <i class="fas fa-file-excel" style="color: #2ecc71; margin-right: 0.5rem;"></i>
                    <span>Microsoft Excel</span>
                </div>
                <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                    <i class="fab fa-github" style="color: #ccc; margin-right: 0.5rem;"></i>
                    <span>GitHub</span>
                </div>
                <div style="display: flex; align-items: center;">
                    <i class="fas fa-code-branch" style="color: #aa00ff; margin-right: 0.5rem;"></i>
                    <span>VS Code/PyCharm</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Contact Section
def contact_section():
    st.markdown("<a id='contact'></a>", unsafe_allow_html=True)
    st.markdown("""
    <div style="
        padding: 5rem 0;
        background: linear-gradient(to bottom, #111, #000000);
    ">
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 4rem;">
        <h2 style="font-size: 2.25rem; font-weight: bold; margin-bottom: 1rem;">
            {gradient_text("Get In Touch", "#00dbde", "#fc00ff")}
        </h2>
        <div style="width: 80px; height: 2px; background: linear-gradient(90deg, #00dbde, #fc00ff); margin: 0 auto;"></div>
        <p style="font-size: 1.25rem; color: #ccc; margin-top: 1rem;">Let's collaborate on your next data-driven project</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="
            background: rgba(30, 30, 30, 0.5);
            backdrop-filter: blur(10px);
            border-radius: 0.75rem;
            padding: 2rem;
            border: 1px solid #333;
            height: 100%;
        ">
            <h3 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 1.5rem; color: white;">Contact Information</h3>
            
            <div style="color: #ccc;">
                <div style="display: flex; align-items: flex-start; margin-bottom: 1.5rem;">
                    <div style="
                        width: 40px;
                        height: 40px;
                        border-radius: 50%;
                        background: linear-gradient(to right, #00dbde, #00aaff);
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        margin-right: 1rem;
                    ">
                        <i class="fas fa-envelope" style="color: white;"></i>
                    </div>
                    <div>
                        <h4 style="font-size: 1.125rem; font-weight: 600; color: white;">Email</h4>
                        <a href="mailto:novi@gmail.com" style="color: #00aaff; text-decoration: none;">novi@gmail.com</a>
                    </div>
                </div>
                
                <div style="display: flex; align-items: flex-start; margin-bottom: 1.5rem;">
                    <div style="
                        width: 40px;
                        height: 40px;
                        border-radius: 50%;
                        background: linear-gradient(to right, #0077bb, #0055aa);
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        margin-right: 1rem;
                    ">
                        <i class="fab fa-linkedin" style="color: white;"></i>
                    </div>
                    <div>
                        <h4 style="font-size: 1.125rem; font-weight: 600; color: white;">LinkedIn</h4>
                        <a href="https://linkedin.com/in/novi" target="_blank" style="color: #00aaff; text-decoration: none;">linkedin.com/in/novi</a>
                    </div>
                </div>
                
                <div style="display: flex; align-items: flex-start; margin-bottom: 1.5rem;">
                    <div style="
                        width: 40px;
                        height: 40px;
                        border-radius: 50%;
                        background: linear-gradient(to right, #333, #555);
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        margin-right: 1rem;
                    ">
                        <i class="fab fa-github" style="color: white;"></i>
                    </div>
                    <div>
                        <h4 style="font-size: 1.125rem; font-weight: 600; color: white;">GitHub</h4>
                        <a href="https://github.com/novi" target="_blank" style="color: #00aaff; text-decoration: none;">github.com/novi</a>
                    </div>
                </div>
                
                <div style="display: flex; align-items: flex-start;">
                    <div style="
                        width: 40px;
                        height: 40px;
                        border-radius: 50%;
                        background: linear-gradient(to right, #ff3333, #ff5555);
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        margin-right: 1rem;
                    ">
                        <i class="fas fa-map-marker-alt" style="color: white;"></i>
                    </div>
                    <div>
                        <h4 style="font-size: 1.125rem; font-weight: 600; color: white;">Location</h4>
                        <p style="color: #ccc;">Surabaya, East Java</p>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        with st.form("contact_form"):
            st.markdown("""
            <div style="
                background: rgba(30, 30, 30, 0.5);
                backdrop-filter: blur(10px);
                border-radius: 0.75rem;
                padding: 2rem;
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
                st.success("Message sent successfully!")
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
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
            
            <div style="display: flex; gap: 1.5rem; margin-bottom: 2rem;">
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
                padding-top: 2rem;
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

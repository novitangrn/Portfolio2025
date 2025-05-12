import streamlit as st
import pandas as pd
import plotly.express as px
import json
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components
from PIL import Image
import base64
import time

# Page configuration
st.set_page_config(
    page_title="Novi Aini | Data Science Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern and futuristic design
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# Load Lottie animations
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Load assets
try:
    lottie_coding = load_lottiefile("animation.json")  # Replace with your animation file
except:
    lottie_coding = None

# Background with particles.js
def particles_background():
    particles_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Particles.js</title>
        <style>
            body {
                margin: 0;
                overflow: hidden;
            }
            canvas {
                display: block;
                vertical-align: bottom;
            }
            #particles-js {
                position: absolute;
                width: 100%;
                height: 100%;
                z-index: -1;
            }
        </style>
    </head>
    <body>
        <div id="particles-js"></div>
        <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
        <script>
            particlesJS("particles-js", {
                "particles": {
                    "number": {
                        "value": 80,
                        "density": {
                            "enable": true,
                            "value_area": 800
                        }
                    },
                    "color": {
                        "value": "#ffffff"
                    },
                    "shape": {
                        "type": "circle",
                        "stroke": {
                            "width": 0,
                            "color": "#000000"
                        },
                        "polygon": {
                            "nb_sides": 5
                        }
                    },
                    "opacity": {
                        "value": 0.5,
                        "random": false,
                        "anim": {
                            "enable": false,
                            "speed": 1,
                            "opacity_min": 0.1,
                            "sync": false
                        }
                    },
                    "size": {
                        "value": 3,
                        "random": true,
                        "anim": {
                            "enable": false,
                            "speed": 40,
                            "size_min": 0.1,
                            "sync": false
                        }
                    },
                    "line_linked": {
                        "enable": true,
                        "distance": 150,
                        "color": "#ffffff",
                        "opacity": 0.4,
                        "width": 1
                    },
                    "move": {
                        "enable": true,
                        "speed": 6,
                        "direction": "none",
                        "random": false,
                        "straight": false,
                        "out_mode": "out",
                        "bounce": false,
                        "attract": {
                            "enable": false,
                            "rotateX": 600,
                            "rotateY": 1200
                        }
                    }
                },
                "interactivity": {
                    "detect_on": "canvas",
                    "events": {
                        "onhover": {
                            "enable": true,
                            "mode": "grab"
                        },
                        "onclick": {
                            "enable": true,
                            "mode": "push"
                        },
                        "resize": true
                    },
                    "modes": {
                        "grab": {
                            "distance": 140,
                            "line_linked": {
                                "opacity": 1
                            }
                        },
                        "bubble": {
                            "distance": 400,
                            "size": 40,
                            "duration": 2,
                            "opacity": 8,
                            "speed": 3
                        },
                        "repulse": {
                            "distance": 200,
                            "duration": 0.4
                        },
                        "push": {
                            "particles_nb": 4
                        },
                        "remove": {
                            "particles_nb": 2
                        }
                    }
                },
                "retina_detect": true
            });
        </script>
    </body>
    </html>
    """
    components.html(particles_html, height=0)

# 3D Book Shelf
def book_shelf():
    shelf_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>3D Book Shelf</title>
        <style>
            .book-shelf {
                perspective: 1000px;
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 20px;
                padding: 20px;
            }
            .book {
                width: 120px;
                height: 180px;
                position: relative;
                transform-style: preserve-3d;
                transition: transform 0.5s ease;
                cursor: pointer;
            }
            .book:hover {
                transform: rotateY(30deg) translateY(-10px);
            }
            .book-cover {
                position: absolute;
                width: 100%;
                height: 100%;
                background: linear-gradient(45deg, #6a11cb 0%, #2575fc 100%);
                border-radius: 5px 10px 10px 5px;
                box-shadow: 5px 5px 10px rgba(0,0,0,0.3);
                backface-visibility: hidden;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                color: white;
                font-weight: bold;
                text-align: center;
                padding: 10px;
                transform: translateZ(10px);
            }
            .book-spine {
                position: absolute;
                width: 15px;
                height: 100%;
                background: linear-gradient(45deg, #4a00e0 0%, #1a5df1 100%);
                transform: rotateY(90deg) translateX(-7.5px) translateZ(7.5px);
                border-radius: 5px 0 0 5px;
            }
            .book-title {
                font-size: 12px;
                margin-bottom: 5px;
            }
            .book-year {
                font-size: 10px;
                opacity: 0.8;
            }
        </style>
    </head>
    <body>
        <div class="book-shelf">
            <div class="book" onclick="location.href='#quantinews'">
                <div class="book-cover">
                    <div class="book-title">QuantiNews</div>
                    <div class="book-year">2025</div>
                </div>
                <div class="book-spine"></div>
            </div>
            <div class="book" onclick="location.href='#data-warehouse'">
                <div class="book-cover" style="background: linear-gradient(45deg, #11998e 0%, #38ef7d 100%);">
                    <div class="book-title">Data Warehouse</div>
                    <div class="book-year">2024</div>
                </div>
                <div class="book-spine" style="background: linear-gradient(45deg, #0b8778 0%, #2bd96b 100%);"></div>
            </div>
            <div class="book" onclick="location.href='#database-dev'">
                <div class="book-cover" style="background: linear-gradient(45deg, #f12711 0%, #f5af19 100%);">
                    <div class="book-title">Database Dev</div>
                    <div class="book-year">2024</div>
                </div>
                <div class="book-spine" style="background: linear-gradient(45deg, #d1210f 0%, #e09c15 100%);"></div>
            </div>
            <div class="book" onclick="location.href='#synop-validator'">
                <div class="book-cover" style="background: linear-gradient(45deg, #8e2de2 0%, #4a00e0 100%);">
                    <div class="book-title">Synop Validator</div>
                    <div class="book-year">2023</div>
                </div>
                <div class="book-spine" style="background: linear-gradient(45deg, #7d26d6 0%, #3a00b3 100%);"></div>
            </div>
            <div class="book" onclick="location.href='#time-series'">
                <div class="book-cover" style="background: linear-gradient(45deg, #00c6ff 0%, #0072ff 100%);">
                    <div class="book-title">Time Series</div>
                    <div class="book-year">2023</div>
                </div>
                <div class="book-spine" style="background: linear-gradient(45deg, #00b4e6 0%, #0062d6 100%);"></div>
            </div>
            <div class="book" onclick="location.href='#text-classification'">
                <div class="book-cover" style="background: linear-gradient(45deg, #f46b45 0%, #eea849 100%);">
                    <div class="book-title">Text Classification</div>
                    <div class="book-year">2022</div>
                </div>
                <div class="book-spine" style="background: linear-gradient(45deg, #e05b35 0%, #e09839 100%);"></div>
            </div>
        </div>
    </body>
    </html>
    """
    components.html(shelf_html, height=250)

# Navigation
def navigation():
    st.sidebar.title("Navigation")
    st.sidebar.markdown("""
    <div class="nav-item" onclick="window.location.href='#home'">🏠 Home</div>
    <div class="nav-item" onclick="window.location.href='#about'">👤 About</div>
    <div class="nav-item" onclick="window.location.href='#education'">🎓 Education</div>
    <div class="nav-item" onclick="window.location.href='#experience'">💼 Experience</div>
    <div class="nav-item" onclick="window.location.href='#projects'">📚 Projects</div>
    <div class="nav-item" onclick="window.location.href='#skills'">🛠️ Skills</div>
    """, unsafe_allow_html=True)

# Header Section
def header_section():
    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("<h1 id='home'>NOVI AINI</h1>", unsafe_allow_html=True)
        st.markdown("""
        <div class="subtitle">
            Data Scientist | Machine Learning Engineer | AI Enthusiast
        </div>
        <div class="contact-info">
            <i class="fas fa-envelope"></i> novi@gmail.com | 
            <i class="fab fa-linkedin"></i> linkedin.com/in/novi | 
            <i class="fab fa-github"></i> github.com/novi<br>
            <i class="fas fa-map-marker-alt"></i> Surabaya, East Java
        </div>
        """, unsafe_allow_html=True)
        
        # Social badges
        st.markdown("""
        <div class="social-badges">
            <a href="https://linkedin.com/in/novi" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a>
            <a href="https://github.com/novi" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>
            <a href="mailto:novi@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"></a>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        if lottie_coding:
            st_lottie(
                lottie_coding,
                speed=1,
                reverse=False,
                loop=True,
                quality="medium",
                height=300,
                width=300,
                key="coding",
            )
        else:
            st.image("profile.png", width=300)

# About Section
def about_section():
    st.markdown("<h2 id='about'>ABOUT ME</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="about-content">
        Data Science graduate from UPN 'Veteran' Jawa Timur with 1 year of practical experience and growing skills in data analysis, 
        machine learning, deep learning, and time-series forecasting. Proficient in Python and familiar with tools such as Tableau 
        and data visualization dashboards. Experienced in applying machine learning and deep learning models to analyze data, 
        enabling data-driven decision-making and optimizing business strategies.
    </div>
    """, unsafe_allow_html=True)

# Education Section
def education_section():
    st.markdown("<h2 id='education'>EDUCATION</h2>", unsafe_allow_html=True)
    
    with st.expander("Universitas Pembangunan Nasional 'Veteran' East Java - Surabaya (Aug 2021 – Mar 2025)"):
        st.markdown("""
        <div class="education-details">
            <strong>Bachelor degree - Data Science, 3.88/4.00</strong><br>
            Subjects: Algebra, Statistics, Algorithm Programming, Database, 
            Machine Learning, Deep Learning, NLP, Data Mining, Big Data
        </div>
        """, unsafe_allow_html=True)

# Experience Section
def experience_section():
    st.markdown("<h2 id='experience'>EXPERIENCE</h2>", unsafe_allow_html=True)
    
    with st.expander("BPBD of Surabaya – Surabaya, Indonesia (Feb 2024 – Jun 2024)"):
        st.markdown("""
        <div class="job-title">Data Analyst Intern</div>
        <div class="company">Surabaya City Regional Disaster Management Agency</div>
        <ul class="job-description">
            <li>Designed and developed the agency's website database using SQL.</li>
            <li>Added over 5,000 historical data entries into the database.</li>
            <li>Organized incident and logistics data archives by implementing an efficient automated input format.</li>
            <li>Applied Natural Language Processing (NLP) to automate data entry from raw reports into the database.</li>
        </ul>
        """, unsafe_allow_html=True)
    
    with st.expander("Bangkit Academy 2023 Batch 2 - Indonesia (July 2023 – Jan 2024)"):
        st.markdown("""
        <div class="job-title">Machine Learning Cohort</div>
        <div class="company">Academic program led by Google, GoTo, and Traveloka</div>
        <ul class="job-description">
            <li>Completed the Machine Learning path on Coursera ahead of schedule, gaining hands-on experience 
            in key machine learning/deep learning concepts and techniques.</li>
            <li>Developed a travel recommendation system using collaborative filtering to generate personalized 
            itineraries based on user preferences and ratings data.</li>
            <li>Implemented geospatial analysis algorithms to optimize travel routes by calculating distances between 
            locations and minimizing travel time.</li>
        </ul>
        """, unsafe_allow_html=True)
    
    with st.expander("Meteorological Office (BMKG) Juanda - Sidoarjo, Indonesia (Aug 2023 – Dec 2023)"):
        st.markdown("""
        <div class="job-title">Meteorological Data Analyst Intern</div>
        <div class="company">Indonesian non-departmental government agency for meteorology</div>
        <ul class="job-description">
            <li>Analyzed upper air and synoptic observation data in the form of time series.</li>
            <li>Built an ensemble model combining Random Forest, Gradient Boosting, and MLP Neural Network, 
            achieving 82% accuracy in extreme weather prediction.</li>
            <li>Developed a web-based synoptic code validator to detect writing errors in code entries.</li>
            <li>Managed to create a dashboard to visualize observation data in the form of charts.</li>
        </ul>
        """, unsafe_allow_html=True)
    
    with st.expander("LSP of Informatics, Graphics, and Data Science - Surabaya, Indonesia (Sep 2022 – Dec 2022)"):
        st.markdown("""
        <div class="job-title">Administration Intern</div>
        <div class="company">A certification body specializing in informatics, graphics, and data science.</div>
        <ul class="job-description">
            <li>Created and prepared administrative documents for the establishment of LSP IGS, a result of the Kedaireka Matching Fund program at UPN "Veteran" Jawa Timur.</li>
            <li>Organized and compiled administrative reports for the LSP IGS establishment process.</li>
        </ul>
        """, unsafe_allow_html=True)

# Projects Section
def projects_section():
    st.markdown("<h2 id='projects'>PROJECTS</h2>", unsafe_allow_html=True)
    st.markdown("<h3 class='project-shelf-title'>My Project Library</h3>", unsafe_allow_html=True)
    book_shelf()
    
    st.markdown("<h3 class='project-details-title'>Project Details</h3>", unsafe_allow_html=True)
    
    with st.expander("QuantiNews: Stock Prediction using Spatial-Temporal Attention-Based Convolutional Network (2025)", id="quantinews"):
        st.markdown("""
        <div class="project-details">
            <ul>
                <li>Developed an STACN model to predict price movements across 11 IDX-IC sectoral indices.</li>
                <li>Achieved a MAPE accuracy range of 0.69% to 2.3% across different sectors.</li>
                <li>Deployed the optimized model in an interactive Streamlit dashboard enabling real-time sectoral index predictions.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with st.expander("Implementation of Data Warehouse on Amazon Prime Userbase Dataset Using Pentaho & Tableau (2024)", id="data-warehouse"):
        st.markdown("""
        <div class="project-details">
            <ul>
                <li>Designed a star schema data warehouse using Pentaho ETL, integrating, cleaning, and transforming raw data.</li>
                <li>Created Tableau dashboards analyzing user trends (churn/retention), device preferences, and revenue patterns to support data-driven decisions.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with st.expander("Database Development for CodeIgniter-Based Website (2024)", id="database-dev"):
        st.markdown("""
        <div class="project-details">
            <ul>
                <li>Designed and implemented an optimized SQL database schema to support website functionality and data storage.</li>
                <li>Integrated the database with a CodeIgniter backend, ensuring secure and efficient data handling for dynamic web operations.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with st.expander("Synop Validators to Minimize Code-Writing Errors (2023)", id="synop-validator"):
        st.markdown("""
        <div class="project-details">
            <ul>
                <li>Developed a logic program based on standard synoptic encoding rules.</li>
                <li>Built and deployed the program as a website using Python and Streamlit.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with st.expander("Time Series Analysis and Forecasting for Upper Air and Synoptic Observation Data (2023)", id="time-series"):
        st.markdown("""
        <div class="project-details">
            <ul>
                <li>Analyzed over 10,000 records of data using ARIMA, SARIMA, SARIMAX, and LSTM models.</li>
                <li>Studied trends in rainfall data parameters from 1982 to 2022, achieving a loss value of 0.8.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with st.expander("Text Classification in NLP for Text-Based News Topic Detection (2022)", id="text-classification"):
        st.markdown("""
        <div class="project-details">
            <ul>
                <li>Collected and pre-processed news data using scraping techniques.</li>
                <li>Applied Latent Dirichlet Allocation (LDA) for topic modeling, achieving 89% accuracy.</li>
                <li>Developed a GUI using Tkinter for user interaction.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Skills Section
def skills_section():
    st.markdown("<h2 id='skills'>SKILLS</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="skills-category">
            <h4>Programming</h4>
            <div class="skill-tag">Python</div>
            <div class="skill-tag">PHP</div>
            <div class="skill-tag">SQL</div>
            <div class="skill-tag">HTML/CSS</div>
        </div>
        
        <div class="skills-category">
            <h4>Databases & ETL</h4>
            <div class="skill-tag">MySQL</div>
            <div class="skill-tag">MongoDB</div>
            <div class="skill-tag">Google BigQuery</div>
            <div class="skill-tag">Pentaho</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="skills-category">
            <h4>Libraries & Frameworks</h4>
            <div class="skill-tag">TensorFlow</div>
            <div class="skill-tag">PyTorch</div>
            <div class="skill-tag">Keras</div>
            <div class="skill-tag">Pandas</div>
            <div class="skill-tag">Scikit-learn</div>
            <div class="skill-tag">Flask</div>
            <div class="skill-tag">CodeIgniter</div>
            <div class="skill-tag">Streamlit</div>
            <div class="skill-tag">Hugging Face</div>
            <div class="skill-tag">PySpark</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="skills-category">
            <h4>Data Viz Tools</h4>
            <div class="skill-tag">Tableau</div>
            <div class="skill-tag">PowerBI</div>
            <div class="skill-tag">Microsoft Excel</div>
        </div>
        
        <div class="skills-category">
            <h4>Tools & Platforms</h4>
            <div class="skill-tag">Jupyter Notebook</div>
            <div class="skill-tag">Google Colab</div>
            <div class="skill-tag">Kaggle</div>
            <div class="skill-tag">VS Code</div>
            <div class="skill-tag">PyCharm</div>
            <div class="skill-tag">GitHub</div>
        </div>
        
        <div class="skills-category">
            <h4>Soft Skills</h4>
            <div class="skill-tag">Adaptability</div>
            <div class="skill-tag">Problem Solving</div>
            <div class="skill-tag">Communication</div>
            <div class="skill-tag">Teamwork</div>
            <div class="skill-tag">Attention to Detail</div>
        </div>
        """, unsafe_allow_html=True)

# Main App
def main():
    # Background effect
    particles_background()
    
    # Navigation sidebar
    navigation()
    
    # Header section
    header_section()
    
    # About section
    about_section()
    
    # Education section
    education_section()
    
    # Experience section
    experience_section()
    
    # Projects section
    projects_section()
    
    # Skills section
    skills_section()
    
    # Footer
    st.markdown("""
    <div class="footer">
        © 2024 Novi Aini | Built with Streamlit
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

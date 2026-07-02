# portfolio_streamlit.py
# Professional Portfolio with Modern UI - ENHANCED

import streamlit as st
import datetime
import time
import re

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Musa Faisal · Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# SESSION STATE
# ============================================================

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ''
if 'show_register' not in st.session_state:
    st.session_state.show_register = False
if 'show_settings' not in st.session_state:
    st.session_state.show_settings = False
if 'page' not in st.session_state:
    st.session_state.page = 'Home'
if 'users' not in st.session_state:
    st.session_state.users = {
        'musa': 'password123',
        'admin': 'admin123'
    }
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'copy_success' not in st.session_state:
    st.session_state.copy_success = False
if 'copy_text' not in st.session_state:
    st.session_state.copy_text = ''

# ============================================================
# PORTFOLIO DATA
# ============================================================

portfolio_data = {
    'name': 'Musa Faisal',
    'title': 'Student · Developer · Problem Solver',
    'school': 'Sheikh Zayed Public School',
    'grade': 'Class 8',
    'email': 'musafaisalryk12@gmail.com',
    'phone': '+92 333 7444700',
    'location': 'Pakistan',
    'bio': '🎓 Passionate student with a love for technology, programming, and creative problem-solving. Always eager to learn new things and build amazing projects! I believe in continuous learning and using technology to make a positive impact.',
    'github': 'https://github.com/musafaisal',
    'linkedin': 'https://www.linkedin.com/in/musa-faisal-12345/',  # Replace with your actual LinkedIn
    'twitter': 'https://twitter.com/musafaisal',
    'instagram': 'https://instagram.com/musafaisal',
    'tiktok': 'https://tiktok.com/@musafaisal',
    'youtube': 'https://youtube.com/@musafaisal'
}

skills_data = [
    {'name': 'Python', 'level': 90, 'icon': '🐍'},
    {'name': 'Streamlit', 'level': 85, 'icon': '📊'},
    {'name': 'HTML & CSS', 'level': 80, 'icon': '🌐'},
    {'name': 'JavaScript', 'level': 65, 'icon': '⚡'},
    {'name': 'Flask', 'level': 70, 'icon': '🔮'},
    {'name': 'SQL', 'level': 60, 'icon': '🗄️'},
    {'name': 'Git & GitHub', 'level': 75, 'icon': '📚'},
    {'name': 'Problem Solving', 'level': 85, 'icon': '🧩'},
    {'name': 'Communication', 'level': 80, 'icon': '💬'},
    {'name': 'Team Work', 'level': 75, 'icon': '🤝'}
]

projects_data = [
    {
        'title': 'AI Chatbot Assistant',
        'description': 'Intelligent chatbot using NLP and deep learning for natural conversations.',
        'tech': ['Python', 'NLP', 'TensorFlow'],
        'icon': '🤖',
        'link': 'https://ai-chatbot-app.streamlit.app'
    },
    {
        'title': 'Weather Forecast Pro',
        'description': 'Real-time weather app with 7-day forecasts and interactive maps.',
        'tech': ['Python', 'Flask', 'API'],
        'icon': '🌤️',
        'link': 'https://weather-app.streamlit.app'
    },
    {
        'title': 'Portfolio Pro',
        'description': 'Modern portfolio with dark theme, animations, and responsive design.',
        'tech': ['Python', 'Streamlit', 'CSS'],
        'icon': '🚀',
        'link': 'https://portfolio-app.streamlit.app'
    },
    {
        'title': 'Task Manager API',
        'description': 'RESTful API for task management with JWT authentication.',
        'tech': ['Python', 'Flask', 'SQLite'],
        'icon': '📋',
        'link': 'https://task-manager-api.streamlit.app'
    },
    {
        'title': 'Data Dashboard',
        'description': 'Interactive dashboard with real-time data visualization.',
        'tech': ['Python', 'Plotly', 'Pandas'],
        'icon': '📊',
        'link': 'https://data-dashboard.streamlit.app'
    },
    {
        'title': '2D Game Engine',
        'description': 'Simple game engine built with Pygame for 2D game development.',
        'tech': ['Python', 'Pygame', 'OOP'],
        'icon': '🎮',
        'link': 'https://game-engine.streamlit.app'
    }
]

education_data = [
    {
        'institution': 'Sheikh Zayed Public School',
        'degree': 'Primary & Secondary Education',
        'field': 'General Science & Computer Studies',
        'year': '2018 - Present',
        'description': 'Currently in Class 8 with a focus on science, mathematics, and computer studies. Maintaining excellent academic record with consistent top grades.',
        'grade': 'A+'
    },
    {
        'institution': 'Online Learning Platforms',
        'degree': 'Self-Study Program',
        'field': 'Computer Science & Programming',
        'year': '2022 - Present',
        'description': 'Completed multiple online courses in Python, Web Development, Artificial Intelligence, and Data Science.',
        'grade': 'Certified'
    }
]

experience_data = [
    {
        'company': 'Student Developer',
        'position': 'Self-Taught Programmer',
        'duration': '2022 - Present',
        'description': 'Learning programming through online courses, building 10+ projects including web apps, chatbots, and data analysis tools. Participated in coding competitions.'
    },
    {
        'company': 'School Tech Club',
        'position': 'Active Member & Mentor',
        'duration': '2023 - Present',
        'description': 'Helping classmates with computer skills, organizing coding workshops for junior students, and leading technology-related activities.'
    }
]

certifications_data = [
    {'name': 'Python for Beginners', 'issuer': 'Coursera', 'year': '2024', 'icon': '🏅'},
    {'name': 'Web Development Fundamentals', 'issuer': 'FreeCodeCamp', 'year': '2024', 'icon': '📜'},
    {'name': 'Introduction to AI', 'issuer': 'Google', 'year': '2023', 'icon': '🤖'},
    {'name': 'Data Science with Python', 'issuer': 'Kaggle', 'year': '2024', 'icon': '📊'}
]

testimonials_data = [
    {
        'name': 'Wajahat Shah',
        'role': 'Online Mentor',
        'text': "One of the most dedicated young programmers I've mentored. Musa's passion for learning and building projects is truly inspiring. He has a bright future ahead in the field of technology.",
        'avatar': '😎'
    },
    {
        'name': 'Ms. Sidra Sana',
        'role': 'Teacher - Sheikh Zayed Public School',
        'text': 'Musa is an exceptional student with great curiosity for technology. He consistently demonstrates problem-solving skills and helps his peers with computer studies. His dedication to learning is truly commendable.',
        'avatar': '👩‍🏫'
    },
    {
        'name': 'Saad Ahmed',
        'role': 'Classmate & Coding Partner',
        'text': 'Always helpful and knowledgeable about computers. Musa explains complex programming concepts in simple ways and makes learning fun. He is a great team player and always ready to help others.',
        'avatar': '👨‍🎓'
    }
]

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>
    /* Main background */
    .stApp {
        background: #0a0a0f;
    }
    
    /* Glass morphism cards */
    .glass-card {
        background: rgba(20, 20, 30, 0.7);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 24px;
        padding: 2rem;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
        margin: 1rem 0;
    }
    
    .glass-card:hover {
        transform: translateY(-5px);
        border-color: rgba(250, 204, 21, 0.3);
        box-shadow: 0 30px 80px rgba(0, 0, 0, 0.6);
    }
    
    /* Gradient text */
    .gradient-text {
        background: linear-gradient(135deg, #facc15 0%, #f59e0b 50%, #f97316 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 800;
    }
    
    /* Typography */
    .main-title {
        font-size: 4rem !important;
        font-weight: 900 !important;
        letter-spacing: -0.03em;
        line-height: 1.1;
        margin: 0;
    }
    
    .subtitle {
        color: #94a3b8;
        font-size: 1.2rem;
        font-weight: 400;
        margin-top: 0.5rem;
    }
    
    .bio-text {
        color: #cbd5e1;
        font-size: 1.1rem;
        line-height: 1.8;
        font-weight: 300;
    }
    
    /* Stats cards */
    .stat-card {
        background: rgba(20, 20, 30, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: default;
    }
    
    .stat-card:hover {
        border-color: rgba(250, 204, 21, 0.3);
        transform: scale(1.02);
        box-shadow: 0 10px 30px rgba(250, 204, 21, 0.05);
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 800;
        color: #facc15;
    }
    
    .stat-label {
        color: #94a3b8;
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-top: 0.3rem;
    }
    
    /* Login container */
    .login-container {
        background: rgba(20, 20, 30, 0.8);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 32px;
        padding: 3rem;
        max-width: 440px;
        margin: 2rem auto;
        box-shadow: 0 40px 80px rgba(0, 0, 0, 0.6);
    }
    
    .login-title {
        font-size: 2.5rem;
        font-weight: 800;
        text-align: center;
        color: #fff;
    }
    
    .login-title span {
        color: #facc15;
    }
    
    .login-subtitle {
        text-align: center;
        color: #94a3b8;
        font-size: 1rem;
        margin-bottom: 2rem;
    }
    
    /* Skills */
    .skill-container {
        margin: 1.2rem 0;
    }
    
    .skill-label {
        display: flex;
        justify-content: space-between;
        color: #e2e8f0;
        font-weight: 500;
        margin-bottom: 0.3rem;
    }
    
    .skill-bar-bg {
        width: 100%;
        height: 8px;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        overflow: hidden;
    }
    
    .skill-bar-fill {
        height: 100%;
        background: linear-gradient(90deg, #facc15, #f59e0b);
        border-radius: 10px;
        transition: width 1.5s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    /* Timeline */
    .timeline-item {
        border-left: 2px solid #facc15;
        padding-left: 2rem;
        margin-bottom: 2rem;
        position: relative;
    }
    
    .timeline-item::before {
        content: '';
        position: absolute;
        left: -7px;
        top: 4px;
        width: 12px;
        height: 12px;
        background: #facc15;
        border-radius: 50%;
        border: 2px solid #0a0a0f;
    }
    
    .timeline-title {
        color: #fff;
        font-size: 1.2rem;
        font-weight: 700;
    }
    
    .timeline-sub {
        color: #94a3b8;
        font-size: 0.95rem;
    }
    
    .timeline-desc {
        color: #cbd5e1;
        margin-top: 0.5rem;
        line-height: 1.6;
    }
    
    /* Project cards */
    .project-card {
        background: rgba(20, 20, 30, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 1.5rem;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        height: 100%;
        margin: 0.5rem 0;
        cursor: pointer;
        position: relative;
        overflow: hidden;
    }
    
    .project-card::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(135deg, rgba(250, 204, 21, 0.05), transparent);
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    
    .project-card:hover::after {
        opacity: 1;
    }
    
    .project-card:hover {
        border-color: rgba(250, 204, 21, 0.3);
        transform: translateY(-8px);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
    }
    
    .project-icon {
        font-size: 3.5rem;
        margin-bottom: 0.5rem;
        display: block;
    }
    
    .project-title {
        color: #fff;
        font-size: 1.2rem;
        font-weight: 700;
        margin: 0.5rem 0;
    }
    
    .project-desc {
        color: #94a3b8;
        font-size: 0.9rem;
        line-height: 1.6;
    }
    
    .project-link-btn {
        display: inline-block;
        background: linear-gradient(135deg, #facc15, #f59e0b);
        color: #0a0a0f !important;
        padding: 0.4rem 1.2rem;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 700;
        font-size: 0.8rem;
        transition: all 0.3s ease;
        margin-top: 0.5rem;
    }
    
    .project-link-btn:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 20px rgba(250, 204, 21, 0.3);
    }
    
    .tech-tag {
        display: inline-block;
        background: rgba(250, 204, 21, 0.1);
        color: #facc15;
        padding: 0.2rem 0.8rem;
        border-radius: 20px;
        font-size: 0.7rem;
        font-weight: 600;
        border: 1px solid rgba(250, 204, 21, 0.1);
        margin: 0.2rem;
    }
    
    /* Testimonials */
    .testimonial-card {
        background: rgba(20, 20, 30, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 1.5rem;
        text-align: center;
        height: 100%;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        margin: 0.5rem 0;
    }
    
    .testimonial-card:hover {
        border-color: rgba(250, 204, 21, 0.3);
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3);
    }
    
    .testimonial-avatar {
        font-size: 4rem;
        margin-bottom: 0.5rem;
        display: block;
    }
    
    .testimonial-name {
        color: #fff;
        font-size: 1.1rem;
        font-weight: 700;
    }
    
    .testimonial-role {
        color: #facc15;
        font-size: 0.85rem;
        font-weight: 500;
    }
    
    .testimonial-text {
        color: #94a3b8;
        font-size: 0.95rem;
        line-height: 1.6;
        margin-top: 0.5rem;
        font-style: italic;
    }
    
    /* Profile image */
    .profile-image {
        width: 280px;
        height: 280px;
        border-radius: 50%;
        background: linear-gradient(135deg, #facc15, #f59e0b);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 7rem;
        border: 4px solid rgba(250, 204, 21, 0.2);
        box-shadow: 0 20px 60px rgba(250, 204, 21, 0.1);
        margin: 0 auto;
        transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        user-select: none;
    }
    
    .profile-image:hover {
        transform: scale(1.02) rotate(-2deg);
        box-shadow: 0 30px 80px rgba(250, 204, 21, 0.2);
    }
    
    /* Divider */
    .divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(250, 204, 21, 0.2), transparent);
        margin: 2rem 0;
    }
    
    /* Status bar */
    .status-bar {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: rgba(10, 10, 15, 0.9);
        backdrop-filter: blur(10px);
        border-top: 1px solid rgba(255, 255, 255, 0.03);
        padding: 0.5rem 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        z-index: 999;
        color: #64748b;
        font-size: 0.8rem;
    }
    
    .status-item {
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* Streamlit overrides */
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.05) !important;
        color: #fff !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
        border-radius: 12px !important;
        padding: 0.8rem 1rem !important;
        font-size: 1rem !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #facc15 !important;
        box-shadow: 0 0 0 3px rgba(250, 204, 21, 0.1) !important;
    }
    
    .stTextArea > div > div > textarea {
        background: rgba(255, 255, 255, 0.05) !important;
        color: #fff !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
        border-radius: 12px !important;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #facc15 !important;
        box-shadow: 0 0 0 3px rgba(250, 204, 21, 0.1) !important;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #facc15, #f59e0b) !important;
        color: #0a0a0f !important;
        font-weight: 700 !important;
        border: none !important;
        border-radius: 50px !important;
        padding: 0.75rem 2rem !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        width: 100% !important;
    }
    
    .stButton > button:hover {
        transform: scale(1.02) !important;
        box-shadow: 0 10px 30px rgba(250, 204, 21, 0.3) !important;
    }
    
    .css-1d391kg {
        background: rgba(10, 10, 15, 0.95) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.03) !important;
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 6px;
    }
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.02);
    }
    ::-webkit-scrollbar-thumb {
        background: #facc15;
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #f59e0b;
    }
    
    /* Social icons container */
    .social-icons {
        display: flex;
        justify-content: center;
        gap: 1.5rem;
        flex-wrap: wrap;
        margin: 1rem 0;
    }
    
    .social-icon {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.05);
        color: #94a3b8;
        font-size: 1.5rem;
        text-decoration: none;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .social-icon:hover {
        background: rgba(250, 204, 21, 0.1);
        border-color: #facc15;
        color: #facc15;
        transform: translateY(-3px) scale(1.1);
        box-shadow: 0 10px 30px rgba(250, 204, 21, 0.1);
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2.8rem !important;
        }
        .profile-image {
            width: 200px;
            height: 200px;
            font-size: 5rem;
        }
        .login-container {
            padding: 2rem;
            margin: 1rem;
        }
        .status-bar {
            padding: 0.3rem 1rem;
            font-size: 0.7rem;
            flex-wrap: wrap;
        }
        .social-icons {
            gap: 0.8rem;
        }
        .social-icon {
            width: 40px;
            height: 40px;
            font-size: 1.2rem;
        }
    }
    
    /* Animations */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes pulse {
        0%, 100% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.05);
        }
    }
    
    .fade-in-up {
        animation: fadeInUp 0.8s cubic-bezier(0.4, 0, 0.2, 1) forwards;
    }
    
    .pulse {
        animation: pulse 2s ease-in-out infinite;
    }
    
    /* Toast notification */
    .copy-toast {
        position: fixed;
        top: 20px;
        left: 50%;
        transform: translateX(-50%);
        background: rgba(20, 20, 30, 0.95);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(250, 204, 21, 0.2);
        border-radius: 16px;
        padding: 1rem 2rem;
        z-index: 10000;
        display: flex;
        align-items: center;
        gap: 0.8rem;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.6);
        animation: fadeInUp 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .copy-toast-success {
        border-color: rgba(34, 197, 94, 0.3);
    }
    
    .copy-toast-error {
        border-color: rgba(239, 68, 68, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def copy_to_clipboard(text):
    """Copy text to clipboard using JavaScript"""
    st.session_state.copy_success = True
    st.session_state.copy_text = text
    # Use JavaScript to copy to clipboard
    st.components.v1.html(f"""
        <script>
            function copyText() {{
                const text = `{text}`;
                navigator.clipboard.writeText(text).then(() => {{
                    // Show success
                    const toast = document.createElement('div');
                    toast.className = 'copy-toast copy-toast-success';
                    toast.innerHTML = '✅ Copied to clipboard!';
                    document.body.appendChild(toast);
                    setTimeout(() => {{
                        toast.remove();
                    }}, 2000);
                }}).catch(() => {{
                    // Fallback
                    const textArea = document.createElement('textarea');
                    textArea.value = text;
                    document.body.appendChild(textArea);
                    textArea.select();
                    document.execCommand('copy');
                    textArea.remove();
                    const toast = document.createElement('div');
                    toast.className = 'copy-toast copy-toast-success';
                    toast.innerHTML = '✅ Copied to clipboard!';
                    document.body.appendChild(toast);
                    setTimeout(() => {{
                        toast.remove();
                    }}, 2000);
                }});
            }}
            copyText();
        </script>
    """, height=0)

def copy_button(text, label):
    """Display a copy button with the given text"""
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(f"""
        <div style="display: flex; align-items: center; background: rgba(20, 20, 30, 0.5); padding: 0.8rem 1.5rem; border-radius: 16px; border: 1px solid rgba(255,255,255,0.05); margin: 0.5rem 0;">
            <span style="color: #94a3b8; min-width: 60px; font-weight: 500;">{label}</span>
            <span style="color: #fff; flex: 1; font-weight: 400; word-break: break-all; font-size: 0.9rem;">{text}</span>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        if st.button("📋 Copy", key=f"copy_{text[:10]}"):
            copy_to_clipboard(text)
            st.rerun()

def display_skill(name, level, icon=''):
    """Display a skill bar"""
    st.markdown(f"""
    <div class="skill-container">
        <div class="skill-label">
            <span>{icon} {name}</span>
            <span style="color: #facc15; font-weight: 700;">{level}%</span>
        </div>
        <div class="skill-bar-bg">
            <div class="skill-bar-fill" style="width: {level}%;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def display_testimonial(testimonial):
    """Display a testimonial card"""
    st.markdown(f"""
    <div class="testimonial-card">
        <span class="testimonial-avatar">{testimonial['avatar']}</span>
        <div class="testimonial-name">{testimonial['name']}</div>
        <div class="testimonial-role">{testimonial['role']}</div>
        <div class="testimonial-text">"{testimonial['text']}"</div>
    </div>
    """, unsafe_allow_html=True)

def open_link(url):
    """Open a link in a new tab"""
    st.markdown(f'<a href="{url}" target="_blank" style="text-decoration: none;">', unsafe_allow_html=True)

# ============================================================
# LOGIN PAGE
# ============================================================

def login_page():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class="login-container">
            <div style="text-align: center; font-size: 4rem; margin-bottom: 0.5rem;">🚀</div>
            <h1 class="login-title">Welcome <span>Back</span></h1>
            <p class="login-subtitle">Sign in to access your portfolio</p>
        """)
        
        with st.form("login_form"):
            username = st.text_input("👤 Username", placeholder="Enter your username")
            password = st.text_input("🔒 Password", placeholder="Enter your password", type="password")
            
            if st.form_submit_button("🔑 Login", use_container_width=True):
                if username in st.session_state.users and st.session_state.users[username] == password:
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.success(f"✅ Welcome back, {username}!")
                    time.sleep(0.5)
                    st.rerun()
                else:
                    st.error("❌ Invalid username or password!")
        
        st.markdown("<div style='text-align: center; color: #94a3b8; margin: 1rem 0;'>Don't have an account?</div>", unsafe_allow_html=True)
        
        if st.button("📝 Create Account", use_container_width=True):
            st.session_state.show_register = True
            st.rerun()
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="status-bar">
        <span class="status-item">🔍 Type here to search</span>
        <span class="status-item">🌡️ 39°C Sunny</span>
        <span class="status-item">🕐 {datetime.datetime.now().strftime('%I:%M %p')}</span>
        <span class="status-item">📅 {datetime.datetime.now().strftime('%m/%d/%Y')}</span>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# REGISTER PAGE
# ============================================================

def register_page():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class="login-container">
            <div style="text-align: center; font-size: 4rem; margin-bottom: 0.5rem;">📝</div>
            <h1 class="login-title">Create <span>Account</span></h1>
            <p class="login-subtitle">Join the community</p>
        """)
        
        with st.form("register_form"):
            new_username = st.text_input("👤 Username", placeholder="Choose a username")
            new_password = st.text_input("🔒 Password", placeholder="Create a password", type="password")
            confirm_password = st.text_input("🔒 Confirm Password", placeholder="Confirm your password", type="password")
            email = st.text_input("📧 Email", placeholder="Enter your email")
            
            if st.form_submit_button("📝 Register", use_container_width=True):
                if not new_username or not new_password:
                    st.error("❌ Please fill in all required fields!")
                elif new_password != confirm_password:
                    st.error("❌ Passwords do not match!")
                elif new_username in st.session_state.users:
                    st.error("❌ Username already exists!")
                else:
                    st.session_state.users[new_username] = new_password
                    st.success("✅ Account created successfully! Please login.")
                    time.sleep(0.5)
                    st.session_state.show_register = False
                    st.rerun()
        
        st.markdown("<div style='text-align: center; color: #94a3b8; margin: 1rem 0;'>Already have an account?</div>", unsafe_allow_html=True)
        
        if st.button("🔑 Back to Login", use_container_width=True):
            st.session_state.show_register = False
            st.rerun()
        
        st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# SETTINGS PAGE
# ============================================================

def settings_page():
    st.markdown("""
    <div class="fade-in-up">
        <h1 style="font-size: 2.5rem; font-weight: 800; margin-bottom: 0.5rem;">
            ⚙️ <span class="gradient-text">Settings</span>
        </h1>
        <div class="divider"></div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("✕ Close Settings", use_container_width=False):
        st.session_state.show_settings = False
        st.rerun()
    
    tab1, tab2, tab3 = st.tabs(["🎨 Appearance", "🔔 Notifications", "🌐 Language"])
    
    with tab1:
        st.markdown('<div class="glass-card"><h3 style="color: #facc15;">🎨 Appearance</h3>', unsafe_allow_html=True)
        st.selectbox("Theme", ["Dark", "Light", "System Default"])
        st.select_slider("Font Size", options=["Small", "Medium", "Large", "Extra Large"])
        st.toggle("Enable Animations", value=True)
        st.color_picker("Accent Color", "#facc15")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown('<div class="glass-card"><h3 style="color: #facc15;">🔔 Notifications</h3>', unsafe_allow_html=True)
        st.toggle("Email Notifications", value=True)
        st.toggle("Push Notifications", value=True)
        st.toggle("Project Updates", value=True)
        st.toggle("Message Notifications", value=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab3:
        st.markdown('<div class="glass-card"><h3 style="color: #facc15;">🌐 Language</h3>', unsafe_allow_html=True)
        st.selectbox("Interface Language", ["English", "Urdu", "Arabic", "Spanish", "French"])
        st.selectbox("Time Zone", ["UTC+5 (Pakistan)", "UTC+0 (GMT)", "UTC-5 (EST)"])
        st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("💾 Save Settings", use_container_width=True):
        st.success("✅ Settings saved successfully!")

# ============================================================
# MAIN PAGES
# ============================================================

def home_page():
    if not st.session_state.logged_in:
        login_page()
        return
    
    st.markdown('<div class="fade-in-up">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div style="margin-top: 1rem;">
            <div style="font-size: 1rem; color: #facc15; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 0.3rem;">
                👋 Welcome to my portfolio
            </div>
            <h1 class="main-title">
                I'm <span class="gradient-text">Musa Faisal</span>
            </h1>
            <p class="subtitle">🎓 Student · Developer · Problem Solver</p>
            <p class="subtitle" style="font-size: 0.95rem; color: #64748b;">
                Sheikh Zayed Public School · Class 8
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <p class="bio-text" style="margin-top: 1.5rem;">
            {portfolio_data['bio']}
        </p>
        """, unsafe_allow_html=True)
        
        copy_button(portfolio_data['email'], "📧 Email")
        copy_button(portfolio_data['phone'], "📱 Phone")
        
        # Social Media Links with icons
        st.markdown("""
        <div style="margin: 1.5rem 0;">
            <p style="color: #94a3b8; font-size: 0.9rem; margin-bottom: 0.8rem;">🔗 Connect with me:</p>
            <div class="social-icons">
                <a href="https://github.com/musafaisal" target="_blank" class="social-icon" title="GitHub">🐙</a>
                <a href="https://www.linkedin.com/in/musa-faisal-12345/" target="_blank" class="social-icon" title="LinkedIn">💼</a>
                <a href="https://twitter.com/musafaisal" target="_blank" class="social-icon" title="Twitter">🐦</a>
                <a href="https://instagram.com/musafaisal" target="_blank" class="social-icon" title="Instagram">📷</a>
                <a href="https://tiktok.com/@musafaisal" target="_blank" class="social-icon" title="TikTok">🎵</a>
                <a href="https://youtube.com/@musafaisal" target="_blank" class="social-icon" title="YouTube">▶️</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin: 1.5rem 0;">
            <div class="stat-card">
                <div class="stat-number">8</div>
                <div class="stat-label">📚 Grade</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">6+</div>
                <div class="stat-label">💻 Projects</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">4+</div>
                <div class="stat-label">🏆 Certificates</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center; margin-top: 2rem;">
            <div class="profile-image pulse">
                👨‍💻
            </div>
            <div style="margin-top: 1rem;">
                <div style="display: flex; justify-content: center; gap: 1rem; font-size: 2rem;">
                    <a href="https://github.com/musafaisal" target="_blank" style="color: #facc15; text-decoration: none; transition: all 0.3s;">🐙</a>
                    <a href="https://www.linkedin.com/in/musa-faisal-12345/" target="_blank" style="color: #facc15; text-decoration: none; transition: all 0.3s;">💼</a>
                    <a href="https://twitter.com/musafaisal" target="_blank" style="color: #facc15; text-decoration: none; transition: all 0.3s;">🐦</a>
                    <a href="https://instagram.com/musafaisal" target="_blank" style="color: #facc15; text-decoration: none; transition: all 0.3s;">📷</a>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def about_page():
    if not st.session_state.logged_in:
        login_page()
        return
    
    st.markdown("""
    <div class="fade-in-up">
        <h1 style="font-size: 2.5rem; font-weight: 800; margin-bottom: 0.5rem;">
            📖 <span class="gradient-text">About Me</span>
        </h1>
        <div class="divider"></div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"""
        <div class="glass-card">
            <h3 style="color: #facc15;">Who am I?</h3>
            <p style="color: #cbd5e1; font-size: 1.05rem; line-height: 1.8;">
                {portfolio_data['bio']}
            </p>
            <br>
            <h4 style="color: #facc15;">🎯 Quick Facts</h4>
            <ul style="color: #cbd5e1; list-style: none; padding: 0;">
                <li style="padding: 0.5rem 0; border-bottom: 1px solid rgba(255,255,255,0.05);">📍 <strong>Location:</strong> {portfolio_data['location']}</li>
                <li style="padding: 0.5rem 0; border-bottom: 1px solid rgba(255,255,255,0.05);">🏫 <strong>School:</strong> {portfolio_data['school']}</li>
                <li style="padding: 0.5rem 0; border-bottom: 1px solid rgba(255,255,255,0.05);">📚 <strong>Grade:</strong> {portfolio_data['grade']}</li>
                <li style="padding: 0.5rem 0; border-bottom: 1px solid rgba(255,255,255,0.05);">💻 <strong>Interests:</strong> Programming, Web Development, AI, Robotics</li>
                <li style="padding: 0.5rem 0;">🌟 <strong>Goal:</strong> To become a software engineer</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="glass-card">
            <h4 style="color: #facc15; text-align: center;">🌟 Achievements</h4>
        """, unsafe_allow_html=True)
        for cert in certifications_data:
            st.markdown(f"""
            <div style="text-align: center; padding: 0.8rem 0; border-bottom: 1px solid rgba(255,255,255,0.05);">
                <div style="font-size: 2.5rem;">{cert['icon']}</div>
                <p style="color: #fff; font-weight: 600; margin: 0.2rem 0;">{cert['name']}</p>
                <p style="color: #94a3b8; font-size: 0.8rem;">{cert['issuer']} · {cert['year']}</p>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

def skills_page():
    if not st.session_state.logged_in:
        login_page()
        return
    
    st.markdown("""
    <div class="fade-in-up">
        <h1 style="font-size: 2.5rem; font-weight: 800; margin-bottom: 0.5rem;">
            ⚡ <span class="gradient-text">Skills</span>
        </h1>
        <div class="divider"></div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    for idx, skill in enumerate(skills_data):
        with col1 if idx % 2 == 0 else col2:
            display_skill(skill['name'], skill['level'], skill['icon'])

def projects_page():
    if not st.session_state.logged_in:
        login_page()
        return
    
    st.markdown("""
    <div class="fade-in-up">
        <h1 style="font-size: 2.5rem; font-weight: 800; margin-bottom: 0.5rem;">
            🚀 <span class="gradient-text">Projects</span>
        </h1>
        <div class="divider"></div>
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(3)
    for idx, project in enumerate(projects_data):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="project-card">
                <span class="project-icon">{project['icon']}</span>
                <div class="project-title">{project['title']}</div>
                <div class="project-desc">{project['description']}</div>
                <div style="margin: 0.5rem 0;">
            """, unsafe_allow_html=True)
            for tech in project['tech']:
                st.markdown(f'<span class="tech-tag">{tech}</span>', unsafe_allow_html=True)
            st.markdown(f"""
                </div>
                <a href="{project['link']}" target="_blank" class="project-link-btn">
                    🔗 View Project
                </a>
            </div>
            """, unsafe_allow_html=True)

def education_page():
    if not st.session_state.logged_in:
        login_page()
        return
    
    st.markdown("""
    <div class="fade-in-up">
        <h1 style="font-size: 2.5rem; font-weight: 800; margin-bottom: 0.5rem;">
            🎓 <span class="gradient-text">Education</span>
        </h1>
        <div class="divider"></div>
    </div>
    """, unsafe_allow_html=True)
    
    for edu in education_data:
        st.markdown(f"""
        <div class="timeline-item">
            <div class="timeline-title">{edu['institution']}</div>
            <div class="timeline-sub">{edu['degree']} · {edu['field']}</div>
            <div style="color: #64748b; font-size: 0.9rem;">📅 {edu['year']} | Grade: <span style="color: #facc15; font-weight: 700;">{edu['grade']}</span></div>
            <div class="timeline-desc">{edu['description']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <h2 style="color: #facc15; margin-top: 2rem;">📜 Certifications</h2>
    <div class="divider"></div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(2)
    for idx, cert in enumerate(certifications_data):
        with cols[idx % 2]:
            st.markdown(f"""
            <div style="background: rgba(20, 20, 30, 0.5); border: 1px solid rgba(255,255,255,0.05); border-radius: 16px; padding: 1.2rem; margin: 0.5rem 0; border-left: 3px solid #facc15; transition: all 0.3s;">
                <div style="display: flex; align-items: center; gap: 1rem;">
                    <span style="font-size: 2rem;">{cert['icon']}</span>
                    <div>
                        <h4 style="color: #fff; margin: 0;">{cert['name']}</h4>
                        <p style="color: #94a3b8; margin: 0; font-size: 0.9rem;">{cert['issuer']} · {cert['year']}</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

def experience_page():
    if not st.session_state.logged_in:
        login_page()
        return
    
    st.markdown("""
    <div class="fade-in-up">
        <h1 style="font-size: 2.5rem; font-weight: 800; margin-bottom: 0.5rem;">
            💼 <span class="gradient-text">Experience</span>
        </h1>
        <div class="divider"></div>
    </div>
    """, unsafe_allow_html=True)
    
    for exp in experience_data:
        st.markdown(f"""
        <div class="timeline-item">
            <div class="timeline-title">{exp['position']}</div>
            <div class="timeline-sub">🏢 {exp['company']}</div>
            <div style="color: #64748b; font-size: 0.9rem;">📅 {exp['duration']}</div>
            <div class="timeline-desc">{exp['description']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <h2 style="color: #facc15; margin-top: 2rem;">💬 Testimonials</h2>
    <div class="divider"></div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(3)
    for idx, testimonial in enumerate(testimonials_data):
        with cols[idx]:
            display_testimonial(testimonial)

def contact_page():
    if not st.session_state.logged_in:
        login_page()
        return
    
    st.markdown("""
    <div class="fade-in-up">
        <h1 style="font-size: 2.5rem; font-weight: 800; margin-bottom: 0.5rem;">
            📧 <span class="gradient-text">Contact Me</span>
        </h1>
        <div class="divider"></div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="glass-card">
            <h3 style="color: #facc15;">Get in Touch</h3>
            <p style="color: #94a3b8;">Feel free to reach out for collaborations or just a friendly chat!</p>
            <div style="margin: 1.5rem 0;">
                <div style="display: flex; align-items: center; gap: 1rem; padding: 0.8rem 0; border-bottom: 1px solid rgba(255,255,255,0.05);">
                    <span style="font-size: 1.5rem;">📧</span>
                    <div>
                        <div style="color: #94a3b8; font-size: 0.8rem;">Email</div>
                        <div style="color: #fff;">{portfolio_data['email']}</div>
                    </div>
                </div>
                <div style="display: flex; align-items: center; gap: 1rem; padding: 0.8rem 0; border-bottom: 1px solid rgba(255,255,255,0.05);">
                    <span style="font-size: 1.5rem;">📱</span>
                    <div>
                        <div style="color: #94a3b8; font-size: 0.8rem;">Phone</div>
                        <div style="color: #fff;">{portfolio_data['phone']}</div>
                    </div>
                </div>
                <div style="display: flex; align-items: center; gap: 1rem; padding: 0.8rem 0; border-bottom: 1px solid rgba(255,255,255,0.05);">
                    <span style="font-size: 1.5rem;">🏫</span>
                    <div>
                        <div style="color: #94a3b8; font-size: 0.8rem;">School</div>
                        <div style="color: #fff;">{portfolio_data['school']}</div>
                    </div>
                </div>
                <div style="display: flex; align-items: center; gap: 1rem; padding: 0.8rem 0;">
                    <span style="font-size: 1.5rem;">📍</span>
                    <div>
                        <div style="color: #94a3b8; font-size: 0.8rem;">Location</div>
                        <div style="color: #fff;">{portfolio_data['location']}</div>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="glass-card">
            <h3 style="color: #facc15;">📨 Send a Message</h3>
            <p style="color: #94a3b8;">I'll get back to you as soon as possible!</p>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("contact_form"):
            name = st.text_input("👤 Your Name", placeholder="Enter your full name")
            email = st.text_input("📧 Your Email", placeholder="Enter your email address")
            subject = st.text_input("📝 Subject", placeholder="What is this about?")
            message = st.text_area("💬 Message", placeholder="Write your message here...", height=150)
            
            if st.form_submit_button("📤 Send Message", use_container_width=True):
                if name and email and message:
                    st.success("✅ Message sent successfully!")
                    st.balloons()
                    st.session_state.messages.append({
                        'name': name,
                        'email': email,
                        'subject': subject,
                        'message': message,
                        'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
                    })
                else:
                    st.error("⚠️ Please fill in all required fields!")

def gallery_page():
    if not st.session_state.logged_in:
        login_page()
        return
    
    st.markdown("""
    <div class="fade-in-up">
        <h1 style="font-size: 2.5rem; font-weight: 800; margin-bottom: 0.5rem;">
            🖼️ <span class="gradient-text">Gallery</span>
        </h1>
        <div class="divider"></div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="border: 2px dashed rgba(255,255,255,0.05); border-radius: 20px; padding: 2rem; text-align: center; background: rgba(20,20,30,0.3); transition: all 0.3s; cursor: pointer;">
        <div style="font-size: 4rem;">📸</div>
        <h3 style="color: #fff;">Upload Your Images</h3>
        <p style="color: #94a3b8;">Drag and drop or click to upload</p>
    </div>
    """, unsafe_allow_html=True)
    
    uploaded_images = st.file_uploader(
        "Choose images",
        type=['jpg', 'jpeg', 'png', 'gif', 'webp'],
        accept_multiple_files=True,
        key="gallery_upload"
    )
    
    if uploaded_images:
        st.markdown(f'<p style="color: #facc15; font-weight: 600;">📸 {len(uploaded_images)} images uploaded</p>', unsafe_allow_html=True)
        cols = st.columns(3)
        for idx, img in enumerate(uploaded_images[:9]):
            with cols[idx % 3]:
                try:
                    st.image(img, use_container_width=True)
                    st.caption(f"📸 Image {idx+1}")
                except:
                    pass
    else:
        st.info("📷 Upload some images to display them here!")

# ============================================================
# SIDEBAR
# ============================================================

def sidebar():
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; padding: 1rem 0;">
            <div style="font-size: 3.5rem;">🚀</div>
            <h2 style="color: #facc15; margin: 0; font-size: 1.3rem;">Musa Faisal</h2>
            <p style="color: #94a3b8; font-size: 0.8rem;">Student · Developer</p>
            <div style="width: 40px; height: 3px; background: linear-gradient(90deg, #facc15, transparent); margin: 0.5rem auto;"></div>
        </div>
        """, unsafe_allow_html=True)
        
        nav_options = {
            '🏠 Home': 'Home',
            '👤 About': 'About',
            '⚡ Skills': 'Skills',
            '🚀 Projects': 'Projects',
            '🎓 Education': 'Education',
            '💼 Experience': 'Experience',
            '📧 Contact': 'Contact',
            '🖼️ Gallery': 'Gallery'
        }
        
        for label, page in nav_options.items():
            if st.button(label, use_container_width=True, key=f"nav_{page}"):
                st.session_state.page = page
                st.rerun()
        
        st.markdown("---")
        
        st.markdown("""
        <div style="text-align: center; padding: 0.5rem 0;">
            <p style="color: #94a3b8; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.1em;">Connect</p>
            <div class="social-icons" style="gap: 0.5rem;">
                <a href="https://github.com/musafaisal" target="_blank" class="social-icon" style="width: 35px; height: 35px; font-size: 1rem;">🐙</a>
                <a href="https://www.linkedin.com/in/musa-faisal-12345/" target="_blank" class="social-icon" style="width: 35px; height: 35px; font-size: 1rem;">💼</a>
                <a href="https://twitter.com/musafaisal" target="_blank" class="social-icon" style="width: 35px; height: 35px; font-size: 1rem;">🐦</a>
                <a href="https://instagram.com/musafaisal" target="_blank" class="social-icon" style="width: 35px; height: 35px; font-size: 1rem;">📷</a>
                <a href="https://tiktok.com/@musafaisal" target="_blank" class="social-icon" style="width: 35px; height: 35px; font-size: 1rem;">🎵</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        if st.button("⚙️ Settings", use_container_width=True):
            st.session_state.show_settings = True
            st.rerun()
        
        if st.session_state.logged_in:
            if st.button("🚪 Logout", use_container_width=True):
                st.session_state.logged_in = False
                st.session_state.username = ''
                st.rerun()
        
        st.markdown(f"""
        <div style="padding: 0.5rem 0; color: #64748b; font-size: 0.7rem; border-top: 1px solid rgba(255,255,255,0.03); margin-top: 0.5rem;">
            <div>🌡️ 39°C Sunny</div>
            <div>🕐 {datetime.datetime.now().strftime('%I:%M %p')}</div>
            <div>📅 {datetime.datetime.now().strftime('%m/%d/%Y')}</div>
            <div style="margin-top: 0.3rem; color: #94a3b8; font-size: 0.6rem;">Mentor: Wajahat Shah</div>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# MAIN
# ============================================================

def main():
    if st.session_state.show_settings:
        settings_page()
        return
    
    if st.session_state.show_register:
        register_page()
        return
    
    sidebar()
    
    page = st.session_state.page
    
    if page == 'Home':
        home_page()
    elif page == 'About':
        about_page()
    elif page == 'Skills':
        skills_page()
    elif page == 'Projects':
        projects_page()
    elif page == 'Education':
        education_page()
    elif page == 'Experience':
        experience_page()
    elif page == 'Contact':
        contact_page()
    elif page == 'Gallery':
        gallery_page()
    else:
        home_page()
    
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0; margin-top: 2rem; border-top: 1px solid rgba(255,255,255,0.03);">
        <p style="color: #64748b; font-size: 0.8rem;">
            🚀 Made with <span style="color: #facc15;">❤️</span> by Musa Faisal · 
            Mentored by <span style="color: #facc15;">Wajahat Shah</span> · 
            © 2024 All Rights Reserved
        </p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":
    main()

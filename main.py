import streamlit as st
from pathlib import Path
import base64

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Mujakkir Ahmad — Data Analyst Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Load CSS with better error handling
# -----------------------------
def load_css(file_path):
    try:
        with open(file_path, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        # Fallback to embedded CSS if file not found
        st.markdown("""
        <style>
            :root {
                --brand: #f5b00f;
                --text: #1841a1;
                --muted: #475569;
                --bg: #519673;
            }
            html, body { background: var(--bg); }
            h1,h2,h3,h4 { color: var(--brand) !important; font-weight: 700; }
            .subtitle { color: var(--muted); margin-top: -8px; margin-bottom: 8px; }
            .stContainer { border-radius: 16px; border: 1px solid #e2e8f0; }
            .stButton>button, .stLinkButton>button, .stDownloadButton>button {
                background: var(--brand) !important;
                color: #fff !important;
                border-radius: 12px !important;
                padding: 8px 14px !important;
                border: none !important;
            }
            [data-testid="stMetricValue"] { color: var(--brand) !important; }
            [data-testid="stMetricLabel"] { color: var(--muted) !important; }
            .social-icon { font-size: 1.5rem; margin-right: 10px; }
        </style>
        """, unsafe_allow_html=True)

css_path = Path("styles.css")
load_css(css_path)

# -----------------------------
# Assets
# -----------------------------

PROFILE_IMG_1 = "mujakkir_profile.png"
PROFILE_IMG_2 = "profile.png"
RESUME_PDF = "resume.pdf"

# Helper function to display images with fallback
def display_image(image_path, caption, width=300):
    try:
        return st.image(str(image_path), caption=caption, use_container_width=True)
    except FileNotFoundError:
        st.info(f"Add your {caption} image at {image_path}")
        return None

# Helper function for PDF download with fallback
def display_resume_download(pdf_path):
    if pdf_path.exists():
        with open(pdf_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600px" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)
            
            st.download_button(
                label="📄 Download Resume",
                data=open(pdf_path, "rb").read(),
                file_name="Mujakkir_Ahmad_Resume.pdf",
                mime="application/pdf",
                use_container_width=True
            )
    else:
        st.warning(f"Add your resume at {pdf_path} to enable download and preview.")

# -----------------------------
# Helper — Card component
# -----------------------------
def card(title: str, subtitle: str = "", body: str = "", link_text: str = "", link_url: str = "", icon: str = ""):
    with st.container(border=True):
        if icon:
            st.markdown(f"### {icon} {title}")
        else:
            st.markdown(f"### {title}")
        if subtitle:
            st.markdown(f"<div class='subtitle'>{subtitle}</div>", unsafe_allow_html=True)
        if body:
            st.markdown(body)
        if link_url and link_text:
            st.link_button(link_text, link_url, use_container_width=True)

# -----------------------------
# Sidebar (Navigation)
# -----------------------------
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home", 
     "Projects", 
     "Services", 
     "Skills", 
     "Experience", 
     "Education", 
     "Testimonials", 
     "Contact"],
)

# Quick contacts in sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("""
<div style="background-color: #0fa8f5; padding: 15px; border-radius: 10px; margin-bottom: 20px;">
    <h3 style="margin-top: 0; color: #4b0082;">Contact Info</h3>
    <p style="margin-bottom: 8px;">
        <span style="font-size: 18px; margin-right: 8px;">👤</span> 
        <strong>Mujakkir Ahmad</strong>
    </p>
    <p style="margin-bottom: 8px;">
        <span style="font-size: 18px; margin-right: 8px;">🏠</span> 
        Sher-E-Bangla Nagar
    </p>
    <p style="margin-bottom: 8px;">
        <span style="font-size: 18px; margin-right: 8px;">📧</span> 
        <a href="mailto:mujakkir.dv@gmail.com" style="color: #4b0082; text-decoration: none;">mujakkir.dv@gmail.com</a>
    </p>
    <p style="margin-bottom: 8px;">
        <span style="font-size: 18px; margin-right: 8px;">📱</span> 
        +8801787933422
    </p>
</div>
""", unsafe_allow_html=True)

# Social links with better icons
st.sidebar.markdown("""
<div style="background-color: #0fa8f5; padding: 15px; border-radius: 10px;">
    <h4 style="margin-top: 0; color: #4b0082;">Connect With Me</h4>
    <div style="display: flex; justify-content: space-between;">
        <a href="https://linkedin.com/in/mujakkir-dv" target="_blank" style="text-decoration: none; color: #0077b5; font-size: 24px; margin-right: 15px;" title="LinkedIn">
            <span style="font-size: 28px;">🔗</span>
        </a>
        <a href="https://github.com/mujakkirdv" target="_blank" style="text-decoration: none; color: #333; font-size: 24px; margin-right: 15px;" title="GitHub">
            <span style="font-size: 28px;">💻</span>
        </a>
        <a href="mailto:mujakkir.dv@gmail.com" style="text-decoration: none; color: #ea4335; font-size: 24px;" title="Email">
            <span style="font-size: 28px;">📧</span>
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# HOME
# -----------------------------
if page == "Home":
    left, right = st.columns([1, 2], gap="large")
    with left:
        display_image(PROFILE_IMG_1, "Mujakkir Ahmad")
        display_resume_download(RESUME_PDF)
        display_image(PROFILE_IMG_2, "Mujakkir Ahmad")

    with right:
        st.markdown("# 👋 Hi, I'm **Mujakkir Ahmad**")
        st.markdown(
    """
    👋 Hi, I’m **Mujakkir Ahmad** — a **Data Analyst & Accountant** who turned curiosity for numbers into a passion for solving business problems.  

    📊 My journey started in **accounts and finance**, where I learned how numbers tell the true story of a business. Over time, I mastered tools like **Excel, QuickBooks, and Python (Pandas, Streamlit, Matplotlib. etc)** to manage reports and financial data.  

    🚀 That curiosity pushed me deeper into the world of **data science and analytics**. Today, I build interactive dashboards with **Python, Pandas, Streamlit, and Plotly**, helping organizations uncover insights, optimize processes, and make smarter, data-driven decisions.  

    🌟 Achievements I’m proud of:  
    - Automated daily financial reports, saving hours of manual work.  
    - Designed dashboards that improved management visibility on sales & expenses.  
    - Supported strategic decisions through clear and actionable insights.  

    💡 For me, data isn’t just numbers — it’s the story behind growth, challenges, and opportunities. And my mission is to translate that story into decisions that move businesses forward.  
    """
)


        # Value Proposition / Why Choose Me

        st.markdown("## 🚀 Why Choose Me")

        st.markdown(
            """
            ✅ **Finance × Data Hybrid**  
            From **cashbooks & ledgers** to **dashboards & forecasting**, I bridge the gap between *accounting* and *analytics*.  

            📊 **Real Business Impact**  
            - Improved financial reporting accuracy by implementing **Intuit QuickBooks**.  
            - Automated reporting tools that saved **hours of manual work** every week.  

            🖥️ **Production-ready Dashboards**  
            I build **Streamlit apps** that leadership teams actually use — for **sales analysis, deposit tracking, and financial forecasting**.  

            🏥 **Domain Knowledge You Can Trust**  
            Hands-on industry experience across **pharma, healthcare, and retail** ensures I understand your business challenges.  

           🧑‍💻 **Clean & Reproducible Work**  
            Pythonic code, version control, and a simple, user-friendly interface — so you get insights that are **clear, reliable, and ready to scale**.  
          """
     )

     
        # Quick KPI counters
        c1, c2, c3 = st.columns(3)
        c1.metric("Years Experience", "5+", help="Combined across accounting, sales, and data roles")
        c2.metric("Deployed Dashboards", "8+", help="Public + internal apps")
        c3.metric("Industries", "4", help="Manufactur, Healthcare, Retail, Sales, Finance, Operations")

# -----------------------------
# PROJECTS
# -----------------------------
elif page == "Projects":
    st.markdown("# 📊 Featured Projects")

    col1, col2 = st.columns(2)
    with col1:
        card(
            title="Portfolio Website",
            subtitle="Streamlit | Clean UI | Live",
            body="A personal site showcasing skills, projects, and contact info.",
            link_text="Open App",
            link_url="https://webmujakkir.streamlit.app",
            icon="🌐"
        )

    with col2:
        card(
            title="Sales & Deposit Analysis Dashboard",
            subtitle="Pandas • Plotly • Streamlit",
            body="Interactive dashboard to analyze sales, deposits, and executive performance.",
            link_text="Open App",
            link_url="https://welburgmetalpvtltd.streamlit.app",
            icon="📈"
        )
    
    col3, col4 = st.columns(2)
    with col3:
        card(
            title="Financial & Expense Forecasting System",
            subtitle="Python • Pandas • Forecasting",
            body="End‑to‑end tooling for statements, bank reports, and expense forecasting.",
            link_text="Open App",
            link_url="https://accountwb.streamlit.app/",
            icon="💰"
        )
    
    with col4:
        card(
            title="Sales and Finance Management System",
            subtitle="Python • Pandas • Streamlit",
            body="Web application for managing sles managment, sales, sales tracking with a user-friendly interface.",
            link_text="Open App",
            link_url="https://hellofinance.streamlit.app/",
            icon="📦"
        )

    # More projects can be added similarly


# -----------------------------
# SERVICES
# -----------------------------
elif page == "Services":
    st.markdown("# 🛠️ Services")

    s1, s2, s3 = st.columns(3)

    with s1:
        card(
            title="Data Dashboards",
            subtitle="Streamlit • Plotly • Excel",
            body="""
            📊 Turn raw data into **interactive dashboards**.  
            From **sales performance** to **financial KPIs**, get insights at a glance with automated updates.  
            """,
            icon="📊"
        )

    with s2:
        card(
            title="Financial Analytics",
            subtitle="QuickBooks • Forecasting",
            body="""
            📉 Go beyond bookkeeping.  
            I deliver **cashflow visibility, expense insights, and deposit analysis**, along with **forecasting tools** to guide better business decisions.  
            """,
            icon="📉"
        )

    with s3:
        card(
            title="Process Automation",
            subtitle="Python • Pandas",
            body="""
            ⚙️ Eliminate repetitive tasks.  
            From **data cleaning** to **reconciliation & reporting**, I build **Python automations** that save hours and reduce errors.  
            """,
            icon="⚙️"
        )

    st.markdown("## 🌟 Additional Services")
    a1, a2, a3 = st.columns(3)

    with a1:
        card(
            title="Data Analysis",
            subtitle="Python • Excel • Pandas",
            body="Exploratory analysis, trend detection, and actionable insights for business growth.",
            icon="🔎"
        )

    with a2:
        card(
            title="Accounting Solutions",
            subtitle="QuickBooks • Excel",
            body="General ledger, expense tracking, reconciliations, and financial statements with accuracy.",
            icon="💰"
        )

    with a3:
        card(
            title="Machine Learning",
            subtitle="scikit-learn • TensorFlow",
            body="Predictive modeling and classification to help businesses make smarter, future-ready decisions.",
            icon="🤖"
        )

    b1, b2 = st.columns(2)

    with b1:
        card(
            title="Data Science",
            subtitle="Python • Pandas • NumPy",
            body="From raw data to insights — feature engineering, visualization, and statistical modeling.",
            icon="🧪"
        )

    with b2:
        card(
            title="Sales & Business Intelligence",
            subtitle="Matpotlib • Streamlit • Excel",
            body="Streamlit interactive dashboards and reporting that reveal sales performance, customer trends, and executive KPIs.",
            icon="📈"
        )

# -----------------------------
# SKILLS
# -----------------------------
elif page == "Skills":
    st.markdown("# ⚡ Technical Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("## 🐍 Programming & Analytics")
        st.markdown("""
        - Python (Pandas, NumPy, Streamlit, Plotly, Matplotlib, Seaborn, Scikit-learn, TensorFlow)
        - Data Analysis & Visualization
        - Statistical Analysis
        - Database Management
        """)
        
        st.markdown("## 📈 Data Management")
        st.markdown("""
        - Google Sheets
        - Microsoft Excel (Advanced formulas, Pivot Tables, Dashboards)
        - SQL
        - Data Cleaning & Preprocessing
        """)
    
    with col2:
        st.markdown("## 💰 Accounting Software")
        st.markdown("""
        - Intuit QuickBooks
        - Tally ERP
        - xero
        - Pharmacy Management Software
        - Financial Reporting
        - Bookkeeping
        """)
        
        st.markdown("## 🎯 Other Skills")
        st.markdown("""
        - Procurement
        - Inventory & Sales Management
        - Data Entry
        - Admin Panel Control
        - Process Optimization
        """)

# -----------------------------
# EXPERIENCE
# -----------------------------
elif page == "Experience":
    st.markdown("# 💼 Professional Experience")

    with st.expander("Welburg Metal Pvt. Ltd. — Accountant & Data Control Officer", expanded=True):
        st.caption("June 2024 – Present")
        st.markdown("""
        - Managing general ledger, cashbook, bankbook, vouchers, and expense reports
        - Preparing sales reports, deposit analysis, and executive performance reports
        - Designed dashboards for sales forecasting & transaction analysis using **Python, Pandas, Streamlit, Plotly**
        - Introduced **Intuit QuickBooks** to improve financial reporting and accuracy
        """)
    
    
    
    with st.expander("Popular Diagnostic Center — Sales Executive (Inventory & Sales)"):
        st.caption("2022 – 2024")
        st.markdown(
    "Handled **inventory management**, **sales tracking**, and end-to-end **medicine shop operations** — ensuring accurate stock control and smooth pharmacy management."
    )

        
    
    with st.expander("Libra Pharmaceutical Ltd. — Operator / Section In‑Charge"):
        st.caption("2020 – 2022")
        st.markdown("Operated production machines (incl. blister packs); supervised lines ensuring quality & compliance.")
    
    
    
    with st.expander("Gel Well Ltd. — Assistant Operator (Blister)"):
        st.caption("2018 – 2020")
        st.markdown("Operated blister pack machines ensuring efficiency and accuracy.")

# -----------------------------
# EDUCATION
# -----------------------------
elif page == "Education":
    st.markdown("# 🎓 Education")

    with st.container(border=True):
        st.subheader("SKILL BASED PGD Program (Data Analytics)")
        st.caption("National University, Gazipr - Dhaka")
        st.write("Session: 2025-2026 · Ongoing")
        

    with st.container(border=True):
        st.subheader("Bachelor of Business Studies (B.B.S)")
        st.caption("Brindaban Government College, Habiganj")
        st.write("Result: GPA 2.83 / 4.00 · Exam Year: 2022")
    
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.subheader("Higher Secondary Certificate (HSC)")
            st.caption("Shaistagonj Degree College, Habiganj · Science · 2018 · Board: Sylhet")
            st.write("Result: GPA 2.83")
    with col2:
        with st.container(border=True):
            st.subheader("Secondary School Certificate (SSC)")
            st.caption("Masud Chaudhary High School and College · Science · 2016 · Board: Sylhet")
            st.write("Result: GPA 4.11")

# -----------------------------
# TESTIMONIALS
# -----------------------------
elif page == "Testimonials":
    st.markdown("# ⭐ Testimonials & Certifications")
    
    # Testimonials section
    st.markdown("## 🗣️ What People Say")
    t1, t2 = st.columns(2)
    with t1:
        with st.container(border=True, height=200):
            st.markdown("""
            > "Mujakkir transformed our financial reporting process with his QuickBooks expertise and custom dashboards. His work has significantly improved our decision-making capabilities."
            
            **— Manager, Welburg Metal**
            """)
    with t2:
        with st.container(border=True, height=200):
            st.markdown("""
            > "Rare combination of financial acumen and technical skills. Delivers clean, production-ready solutions that actually get used by the team."
            
            **— Colleague, Get Well Pharmaceuticals**
            """)
    
    t3, t4 = st.columns(2)
    with t3:
        with st.container(border=True, height=200):
            st.markdown("""
            > "Excellent at turning complex data into actionable insights. His sales dashboards helped us identify key opportunities for growth."
            
            **— Sales Director, Popular Diagnostic**
            """)
    with t4:
        with st.container(border=True, height=200):
            st.markdown("""
            > "Understands both the numbers and the business context behind them. A valuable asset to any data-driven organization."
            
            **— Operations Manager, Libra Pharma**
            """)
    
    # Certifications section
    st.markdown("## 📜 Certifications")
    
    cert1, cert2 = st.columns(2)
    with cert1:
        with st.container(border=True):
            st.markdown("### 🐍 Python for Data Analysis")
            st.caption("FreeCodeCamp • 2024")
            st.markdown("""
            - Data manipulation with Pandas
            - Data visualization with Matplotlib & Seaborn
            - Statistical analysis with NumPy
            """)
            # st.link_button("View Certificate", "https://coursera.org/verify/example123", use_container_width=True)
    
    with cert2:
        with st.container(border=True):
            st.markdown("### 📊 Data Visualization with Python")
            st.caption("DataCamp • 2023")
            st.markdown("""
            - Interactive visualizations with Plotly
            - Dashboard creation
            - Storytelling with data
            """)
            # st.link_button("View Certificate", "https://www.datacamp.com/certificate/example456", use_container_width=True)
    
    cert3, cert4 = st.columns(2)
    with cert3:
        with st.container(border=True):
            st.markdown("### 💼 QuickBooks Online Certification")
            st.caption("Intuit • 2023")
            st.markdown("""
            - Financial reporting
            - Accounts management
            - Advanced bookkeeping
            """)
            # st.link_button("View Certificate", "https://quickbooks.intuit.com/learn-support/en-us/certification/example789", use_container_width=True)
    
    with cert4:
        with st.container(border=True):
            st.markdown("### 📈 Excel Advanced Analytics")
            st.caption("Self • 2022")
            st.markdown("""
            - Advanced formulas & functions
            - PivotTables & Power Query
            - Data modeling & analysis
            """)
            # st.link_button("View Certificate", "https://learn.microsoft.com/en-us/users/example101/certification", use_container_width=True)
# -----------------------------
# CONTACT
# -----------------------------
elif page == "Contact":
    st.markdown("# 📬 Get in Touch")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write("I'm always interested in new opportunities and collaborations. Feel free to reach out!")
        
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Your Name*", placeholder="Enter your full name")
            email = st.text_input("Your Email*", placeholder="Enter your email address")
            subject = st.text_input("Subject", placeholder="What is this regarding?")
            message = st.text_area("Message*", placeholder="Your message here...", height=150)
            submitted = st.form_submit_button("Send Message", type="primary")
            
            if submitted:
                if not name or not email or not message:
                    st.error("Please fill in all required fields (*)")
                else:
                    # In a real application, you would connect this to an email service
                    st.success("Thanks for your message! I'll get back to you soon.")
                    st.balloons()
    
    with col2:
        st.markdown("### Contact Details")
        st.markdown("""
        🏠︎ **Address**:  
        Sher_E Bangla Nagar, Dhaka, Bangladesh
        
        📞 **Phone**:  
        +8801787933422 (Primary)  
        +8801601933422 (Secondary)
        
        ✉️ **Email**:  
        [mujakkir.dv@gmail.com](mailto:mujakkir.dv@gmail.com)
        
        🔗 **LinkedIn**:  
        [linkedin.com/in/mujakkir-dv](https://linkedin.com/in/mujakkir-dv)
        
        💻 **GitHub**:  
        [github.com/mujakkirdv](https://github.com/mujakkirdv)
        """)
        
        # Social media links with icons
        st.markdown("### Follow Me")
        st.markdown("""
        <div>
            <a href="https://linkedin.com/in/mujakkir-dv" target="_blank" style="text-decoration: none; margin-right: 15px;">
                <span style="font-size: 1.5rem;">🔗</span> LinkedIn
            </a>
            <a href="https://github.com/mujakkirah" target="_blank" style="text-decoration: none;">
                <span style="font-size: 1.5rem;">💻</span> GitHub
            </a>
        </div>
        """, unsafe_allow_html=True)


# Add a footer fixed at the bottom
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #0fa8f5;
        color: #e4e4ed;
        text-align: center;
        padding: 10px 0;
        font-size: 16px;
        box-shadow: 0 -1px 5px rgba(0,0,0,0.1);
    }
    </style>
    <div class="footer">
        © 2025 Mujakkir Ahmad | mujakkir.dv@gmail.com | All Rights Reserved
    </div>
    """,
    unsafe_allow_html=True

)


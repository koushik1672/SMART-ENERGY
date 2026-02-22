import streamlit as st
import base64

def set_dashboard_config():
    """Configure professional dashboard settings"""
    st.set_page_config(
        page_title="Smart Energy Analytics Platform",
        page_icon="⚡",
        layout="wide",
        initial_sidebar_state="expanded"
    )

def load_custom_css():
    """Load professional dashboard CSS"""
    css = """
    <style>
    /* Main Dashboard Styles */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    
    .metric-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid #667eea;
        margin: 0.5rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    }
    
    .section-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1rem 1.5rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .data-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #e1e8ed;
        margin: 1rem 0;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    }
    
    .sidebar-section {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        border-left: 3px solid #667eea;
    }
    
    .kpi-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin: 1rem 0;
    }
    
    .alert-info {
        background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
        border-left: 4px solid #667eea;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    .chart-container {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #e1e8ed;
        margin: 1rem 0;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    }
    
    .navigation-tabs {
        background: #f8f9fa;
        padding: 0.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    /* Hide streamlit elements */
    .stDeployButton {
        display: none;
    }
    
    #MainMenu {
        visibility: hidden;
    }
    
    footer {
        visibility: hidden;
    }
    
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Professional color scheme */
    .primary-color { color: #667eea; }
    .secondary-color { color: #764ba2; }
    .accent-color { color: #f093fb; }
    
    /* Data table styling */
    .dataframe {
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    }
    
    /* Input field styling */
    .stSelectbox > div > div {
        background: white;
        border-radius: 8px;
    }
    
    .stNumberInput > div > div {
        background: white;
        border-radius: 8px;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    /* Progress bar styling */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    }
    
    /* Professional typography */
    h1, h2, h3 {
        font-weight: 600;
        color: #2c3e50;
    }
    
    .subtitle {
        color: #7f8c8d;
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def create_sidebar_navigation():
    """Create professional sidebar navigation"""
    with st.sidebar:
        st.markdown("## ⚡ Energy Analytics")
        st.markdown("---")
        
        # Navigation sections
        st.markdown("### 📊 Dashboard Sections")
        
        sections = {
            "🏠 Overview": "overview",
            "🎯 Prediction Engine": "prediction", 
            "📈 Model Analytics": "analytics",
            "🔍 Data Insights": "insights",
            "⚙️ Configuration": "config"
        }
        
        selected_section = st.selectbox(
            "Navigate to:",
            list(sections.keys()),
            key="navigation"
        )
        
        st.markdown("---")
        
        # Quick stats
        st.markdown("### 📊 Quick Stats")
        st.markdown("""
        <div class="sidebar-section">
            <strong>Model Status:</strong> Active<br>
            <strong>Data Points:</strong> 2.07M<br>
            <strong>Accuracy:</strong> 95.2%<br>
            <strong>Last Updated:</strong> Today
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # System info
        st.markdown("### ℹ️ System Info")
        st.markdown("""
        <div class="sidebar-section">
            <strong>Version:</strong> 2.0.1<br>
            <strong>Framework:</strong> Streamlit<br>
            <strong>ML Model:</strong> Gradient Boosting<br>
            <strong>Dataset:</strong> Household Power
        </div>
        """, unsafe_allow_html=True)
        
        return sections[selected_section]

def create_header(title, subtitle=""):
    """Create professional header"""
    st.markdown(f"""
    <div class="main-header">
        <h1 style="margin: 0; font-size: 2.5rem;">{title}</h1>
        <p style="margin: 0.5rem 0 0 0; opacity: 0.9; font-size: 1.1rem;">{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)

def create_metric_card(title, value, delta="", help_text=""):
    """Create professional metric card"""
    st.markdown(f"""
    <div class="metric-card">
        <h4 style="margin: 0; color: #2c3e50;">{title}</h4>
        <p style="margin: 0.5rem 0; font-size: 1.8rem; font-weight: bold; color: #667eea;">{value}</p>
        {f'<p style="margin: 0; color: {"green" if delta.startswith("+") else "red"};">{delta}</p>' if delta else ''}
        {f'<p style="margin: 0.5rem 0 0 0; font-size: 0.8rem; color: #7f8c8d;">{help_text}</p>' if help_text else ''}
    </div>
    """, unsafe_allow_html=True)

def create_section_header(title, description=""):
    """Create section header"""
    st.markdown(f"""
    <div class="section-header">
        <h3 style="margin: 0;">{title}</h3>
        {f'<p style="margin: 0.5rem 0 0 0; opacity: 0.9;">{description}</p>' if description else ''}
    </div>
    """, unsafe_allow_html=True)

def create_alert(message, alert_type="info"):
    """Create professional alert"""
    st.markdown(f"""
    <div class="alert-info">
        <strong>ℹ️ {alert_type.title()}:</strong> {message}
    </div>
    """, unsafe_allow_html=True)

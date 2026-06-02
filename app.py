import streamlit as st

st.set_page_config(
    page_title="CrowdShield AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    .stApp { font-family: 'Inter', sans-serif; }

    .hero-container {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        border-radius: 20px;
        padding: 60px 40px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    }

    .hero-title { font-size: 3.5em; font-weight: 800; color: white; margin-bottom: 10px; }
    .hero-subtitle { font-size: 1.4em; color: rgba(255,255,255,0.7); }

    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 20px;
        margin: 30px 0;
    }

    .feature-card {
        background: linear-gradient(135deg, #1e1e2e 0%, #2a2a3e 100%);
        border: 1px solid rgba(99,102,241,0.2);
        border-radius: 16px;
        padding: 24px;
        position: relative;
        overflow: hidden;
    }

    .feature-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; width: 4px; height: 100%;
        background: #6366f1;
    }

    .premium-badge {
        background: #ef4444;
        color: white;
        font-size: 0.7em;
        padding: 2px 10px;
        border-radius: 10px;
        position: absolute;
        top: 15px; right: 15px;
        font-weight: 700;
    }

    .feature-icon { font-size: 2em; margin-bottom: 15px; }
    .feature-title { font-size: 1.2em; font-weight: 700; color: #f8fafc; margin-bottom: 10px; }
    .feature-desc { font-size: 0.9em; color: #94a3b8; line-height: 1.6; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-container">
    <div class="hero-title">🛡️ CrowdShield AI ELITE</div>
    <div class="hero-subtitle">Next-Gen Crowd Intelligence, Security & Emergency Response</div>
</div>
""", unsafe_allow_html=True)

st.markdown("### 💎 Elite Security Features")

st.markdown("""
<div class="feature-grid">
    <div class="feature-card">
        <div class="feature-icon">👥</div>
        <div class="feature-title">Real-Time Crowd Tracking & Density</div>
        <div class="feature-desc">Counts people dynamically as they enter and exit, monitoring real-time venue capacity safely.</div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">🌡️</div>
        <div class="feature-title">AI Heatmaps & Hotspot Visualization</div>
        <div class="feature-desc">Overlays thermal-style hotspots on video feeds to detect highly congested areas at a glance.</div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">🧠</div>
        <div class="feature-title">Predictive Panic Index (PPI)</div>
        <div class="feature-desc">Analyzes behavioral chaos (turbulence, speed spikes, compression) to predict stampedes before they occur.</div>
    </div>
    <div class="feature-card">
        <div class="premium-badge">ELITE</div>
        <div class="feature-icon">🔥</div>
        <div class="feature-title">Incident Detection Alerts</div>
        <div class="feature-desc">Real-time detection of fights, aggressive behavior, fire, and smoke signatures using motion heuristics.</div>
    </div>
    <div class="feature-card">
        <div class="premium-badge">ELITE</div>
        <div class="feature-icon">🎒</div>
        <div class="feature-title">Theft & Abandoned Object</div>
        <div class="feature-desc">AI tracks baggage and alerts if items are left unattended for too long or if a bag suddenly changes ownership.</div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">👤</div>
        <div class="feature-title">Person Search & Facial Recognition</div>
        <div class="feature-desc">Advanced facial recognition system to locate missing persons or kids across all live camera feeds.</div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">🗺️</div>
        <div class="feature-title">Smart Evacuation Routing</div>
        <div class="feature-desc">Dynamic routing that guides the crowd to the safest exit based on real-time congestion and incident maps.</div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">📊</div>
        <div class="feature-title">Advanced Crowd Analytics</div>
        <div class="feature-desc">Dive deep into historical crowd flow rates, maximum capacities, and behavioral risks with visual timeline graphs.</div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">🚨</div>
        <div class="feature-title">Multi-Channel Alert System</div>
        <div class="feature-desc">Automates integrated SMS and Email broadcasting for immediate action during critical security threshold breaches.</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; padding: 40px; color: #64748b; border-top: 1px solid rgba(255,255,255,0.05);">
    CrowdShield AI v4.0 • Built with YOLOv8, DeepFace, and Behavioral AI
</div>
""", unsafe_allow_html=True)

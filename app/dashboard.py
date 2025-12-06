# ================================================================
# ThreatEye - AI-Powered Cyber Threat Detection Dashboard
# Author: Lakshmi.S
# Version: Day 6 (with Live Alerts + Log Simulation)
# ================================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
import time
import random

# ---------------------- Page Setup ----------------------
st.set_page_config(page_title="ThreatEye Dashboard", layout="wide")
st.title("🛡️ ThreatEye – AI-Powered Cyber Threat Detection")

# ---------------------- Log Simulation Controls ----------------------
st.sidebar.header("⚙️ Simulation Controls")

if st.sidebar.button("🌀 Generate Simulated Logs"):
    sample_data = {
        "timestamp": pd.date_range(start="2025-12-06 10:00:00", periods=10, freq="min"),
        "user": random.choices(["admin", "guest", "root", "user1"], k=10),
        "action": random.choices(["login", "file_access"], k=10),
        "status": random.choices(["failed", "success", "failed", "failed", "success"], k=10),
        "ip": random.choices(["192.168.1.4", "203.0.113.10", "10.0.0.15", "172.16.0.5"], k=10),
    }
    df = pd.DataFrame(sample_data)
    df.to_csv("data/simulated_logs.csv", index=False)
    st.sidebar.success("✅ Simulated logs generated! Upload 'data/simulated_logs.csv' for analysis.")

# ---------------------- File Upload ----------------------
uploaded_file = st.file_uploader("📂 Upload Log File (CSV)", type=["csv"])

if uploaded_file:
    # Load data
    data = pd.read_csv(uploaded_file)
    st.subheader("📘 Sample Logs")
    st.dataframe(data.head())

    # ---------------------- Basic Summary ----------------------
    st.markdown("### 📊 Log Summary")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Logs", len(data))
    col2.metric("Unique Users", data['user'].nunique())
    col3.metric("Unique IPs", data['ip'].nunique())

    failed_logins = data[data['status'] == 'failed']
    st.write("**Failed login attempts:**", len(failed_logins))

    # ---------------------- Visualization 1 ----------------------
    st.markdown("### 🔍 Failed Logins by User")
    if not failed_logins.empty:
        fig, ax = plt.subplots()
        failed_logins['user'].value_counts().plot(kind='bar', color='tomato', ax=ax)
        ax.set_xlabel("User")
        ax.set_ylabel("Failed Attempts")
        st.pyplot(fig)
    else:
        st.info("No failed login attempts found.")

    # ---------------------- AI Detection ----------------------
    st.markdown("### 🤖 AI-Based Anomaly Detection")

    # Encode categorical features
    data['failed_flag'] = data['status'].apply(lambda x: 1 if x == 'failed' else 0)
    data['user_encoded'] = data['user'].astype('category').cat.codes
    data['ip_encoded'] = data['ip'].astype('category').cat.codes

    # Train Isolation Forest Model
    features = data[['user_encoded', 'ip_encoded', 'failed_flag']]
    model = IsolationForest(contamination=0.3, random_state=42)
    model.fit(features)
    data['anomaly'] = model.predict(features)

    st.dataframe(data[['timestamp', 'user', 'ip', 'status', 'anomaly']])

    # ---------------------- Visualization 2 ----------------------
    fig2, ax2 = plt.subplots()
    colors = ['red' if a == -1 else 'green' for a in data['anomaly']]
    ax2.scatter(data['user_encoded'], data['ip_encoded'], c=colors)
    ax2.set_xlabel("User (encoded)")
    ax2.set_ylabel("IP (encoded)")
    ax2.set_title("Anomaly Detection Visualization")
    st.pyplot(fig2)

    # ---------------------- Threat Severity Scoring ----------------------
    st.markdown("### 🚨 Threat Severity Scoring")

    def calculate_threat_score(row):
        score = 0
        if row['status'] == 'failed':
            score += 40
        if row['anomaly'] == -1:
            score += 50
        if data[data['ip'] == row['ip']]['failed_flag'].sum() > 2:
            score += 20
        return min(score, 100)

    data['threat_score'] = data.apply(calculate_threat_score, axis=1)

    # Label risk levels
    def label_risk(score):
        if score < 40:
            return 'Low'
        elif score < 70:
            return 'Medium'
        else:
            return 'High'

    data['risk_level'] = data['threat_score'].apply(label_risk)

    st.dataframe(data[['timestamp', 'user', 'ip', 'status', 'anomaly', 'threat_score', 'risk_level']])

    # ---------------------- Live Alert Notifications ----------------------
    st.markdown("### 🔔 Live Threat Alerts")

    high_risk_events = data[data['risk_level'] == 'High']
    medium_risk_events = data[data['risk_level'] == 'Medium']

    if not high_risk_events.empty:
        for _, row in high_risk_events.iterrows():
            st.error(f"🚨 High Risk Alert! Suspicious activity detected from IP: {row['ip']} (User: {row['user']})")
            time.sleep(0.3)
    elif not medium_risk_events.empty:
        st.warning(f"⚠️ {len(medium_risk_events)} Medium-risk events detected. Keep monitoring.")
    else:
        st.success("✅ No suspicious activity detected.")

    # ---------------------- Visualization 3 ----------------------
    st.markdown("### 📊 Threat Risk Level Overview")
    risk_counts = data['risk_level'].value_counts()
    fig3, ax3 = plt.subplots()
    risk_counts.plot(kind='bar', color=['green', 'orange', 'red'], ax=ax3)
    ax3.set_xlabel("Risk Level")
    ax3.set_ylabel("Number of Events")
    ax3.set_title("Distribution of Threat Risk Levels")
    st.pyplot(fig3)

    # ---------------------- Summary Insight ----------------------
    st.markdown("### 🧠 Security Insight")
    high_risk = data[data['risk_level'] == 'High']
    if not high_risk.empty:
        st.error(f"⚠️ {len(high_risk)} HIGH-RISK events detected! Immediate review recommended.")
    elif (data['risk_level'] == 'Medium').any():
        st.warning("⚠️ Medium-risk activities observed. Monitor closely.")
    else:
        st.success("✅ All activities appear safe and within normal behavior.")
else:
    st.info("👆 Upload a CSV log file to begin analysis.")
# ---------------------- Day 7: Generate PDF Threat Report ----------------------
from fpdf import FPDF
import os

st.markdown("### 🧾 Generate Threat Report")

def generate_pdf(data):
    def safe_text(text):
        return str(text).encode('latin-1', 'replace').decode('latin-1')

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, txt="ThreatEye - AI Cyber Threat Report", ln=True, align='C')

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=safe_text(f"Total Log Entries: {len(data)}"), ln=True)
    pdf.cell(200, 10, txt=safe_text(f"Unique Users: {data['user'].nunique()}"), ln=True)
    pdf.cell(200, 10, txt=safe_text(f"Unique IPs: {data['ip'].nunique()}"), ln=True)

    high = len(data[data['risk_level'] == 'High'])
    med = len(data[data['risk_level'] == 'Medium'])
    low = len(data[data['risk_level'] == 'Low'])

    pdf.cell(200, 10, txt=safe_text(f"High Risk Events: {high}"), ln=True)
    pdf.cell(200, 10, txt=safe_text(f"Medium Risk Events: {med}"), ln=True)
    pdf.cell(200, 10, txt=safe_text(f"Low Risk Events: {low}"), ln=True)

    pdf.cell(200, 10, txt="", ln=True)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, txt="Detailed Threat Log Summary:", ln=True)
    pdf.set_font("Arial", size=10)

    for _, row in data.iterrows():
        pdf.cell(200, 8, txt=safe_text(f"[{row['timestamp']}] {row['user']} ({row['ip']}) - {row['status']} | Risk: {row['risk_level']}"), ln=True)

    pdf.output("ThreatEye_Report.pdf")
    return "ThreatEye_Report.pdf"

if st.button("📄 Generate PDF Report"):
    filename = generate_pdf(data)
    st.success("✅ Report Generated Successfully!")
    with open(filename, "rb") as f:
        st.download_button("⬇️ Download Report", f, file_name="ThreatEye_Report.pdf")

🛡️ ThreatEye – AI-Powered Cyber Threat Detection System



Author: Lakshmi.S

Domain: Cybersecurity | Artificial Intelligence

Tech Stack: Python, Streamlit, Scikit-learn, Matplotlib, FPDF



📖 Overview



ThreatEye is an AI-powered cybersecurity dashboard that detects, analyzes, and visualizes potential threats from system log data.

It replicates a Security Operations Center (SOC) environment by continuously monitoring logs, identifying anomalies using machine learning, and generating automated risk reports.



🎯 Key Features



✅ Log Analysis: Reads and summarizes CSV-based system log files.

✅ AI Anomaly Detection: Uses Isolation Forest to flag unusual user/IP behavior.

✅ Threat Scoring: Assigns severity levels (Low, Medium, High) based on AI-detected patterns.

✅ Live Alerts: Displays real-time alerts for suspicious IPs and users.

✅ Visualization: Generates clear graphs of login activity and risk distribution.

✅ PDF Reporting: Creates a downloadable AI-generated Threat Report.

✅ Simulation: Auto-generates log data for demo or testing.



🧠 Technology Used

Component	Tool

Frontend UI	Streamlit

Data Handling	Pandas

Visualization	Matplotlib

Machine Learning	Isolation Forest (Scikit-learn)

Report Generation	FPDF

⚙️ How to Run



1️⃣ Clone or Download the Project



git clone https://github.com/yourusername/ThreatEye.git

cd ThreatEye\_Project





2️⃣ Install Dependencies



pip install -r requirements.txt





3️⃣ Run the Streamlit App



streamlit run app/dashboard.py





4️⃣ Open the App in Your Browser



http://localhost:8501





5️⃣ Upload or Generate Log Data



Upload data/sample\_logs.csv



Or use the sidebar button “🌀 Generate Simulated Logs” to create test data.



🧾 Sample Log File (sample\_logs.csv)

timestamp,user,action,status,ip

2025-12-05 10:21:13,admin,login,failed,192.168.1.4

2025-12-05 10:22:45,root,login,success,10.0.0.15

2025-12-05 10:23:55,user1,login,failed,192.168.1.4

2025-12-05 10:24:13,admin,file\_access,success,10.0.0.15

2025-12-05 10:24:44,guest,login,failed,203.0.113.10



🧩 Output Highlights



Threat Summary Table: AI-detected anomalies and risk levels



Visual Charts: Failed logins per user/IP and overall risk distribution



Alerts: Live threat banners for High-Risk or Medium-Risk events



Reports: Downloadable PDF “ThreatEye\_Report.pdf” summarizing the analysis



💼 Project Highlights



Mimics a real Security Operations Center (SOC) workflow



Integrates AI + Cybersecurity seamlessly



Demonstrates Machine Learning-based Threat Detection



Fully interactive web dashboard using Streamlit



Perfect for portfolios, internships, and placement interviews



🧠 Future Enhancements



Add email notifications for high-risk alerts



Integrate with real-time system logs via APIs



Build advanced dashboards using Plotly or Power BI



👩‍💻 Author



Lakshmi.S

B.E Computer Science Engineering (Cyber Security)

R.M.K College of Engineering and Technology



📧 lakshmisuresh383@gmail.com

🌐 GitHub: https://github.com/Lakshh-22



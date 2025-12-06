# ThreatEye - Day 1: Log Reader Program
# Author: Lakshmi.S

import pandas as pd  # Pandas is used for handling CSV data

# Step 1: Load the log file
data = pd.read_csv("data/sample_logs.csv")

# Step 2: Display first few rows to understand data
print("=== Sample Logs ===")
print(data.head())  # Shows the first 5 rows

# Step 3: Basic summary
print("\n=== Log Summary ===")
print(f"Total log entries: {len(data)}")
print(f"Unique users: {data['user'].nunique()}")
print(f"Unique IP addresses: {data['ip'].nunique()}")

# Step 4: Count failed login attempts
failed_logins = data[data['status'] == 'failed']
print(f"Failed login attempts: {len(failed_logins)}")

# Step 5: Show how many failed logins per user
print("\n=== Failed Logins by User ===")
print(failed_logins['user'].value_counts())
# ThreatEye - Day 2: Data Visualization
# Author: Lakshmi.S

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load log file
data = pd.read_csv("data/sample_logs.csv")

# Step 2: Display first few rows
print("=== Sample Logs ===")
print(data.head())

# Step 3: Basic summary
print("\n=== Log Summary ===")
print(f"Total log entries: {len(data)}")
print(f"Unique users: {data['user'].nunique()}")
print(f"Unique IP addresses: {data['ip'].nunique()}")

# Step 4: Count failed logins
failed_logins = data[data['status'] == 'failed']
print(f"Failed login attempts: {len(failed_logins)}")

# Step 5: Show failed logins per user
print("\n=== Failed Logins by User ===")
print(failed_logins['user'].value_counts())

# Step 6: --- Visualization Section ---
print("\nGenerating visualizations...")

# Plot 1: Failed Logins per User
user_counts = failed_logins['user'].value_counts()
plt.figure(figsize=(6, 4))
user_counts.plot(kind='bar', color='tomato')
plt.title('Failed Login Attempts per User')
plt.xlabel('User')
plt.ylabel('Number of Failed Logins')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# Plot 2: Failed Logins per IP Address
ip_counts = failed_logins['ip'].value_counts()
plt.figure(figsize=(6, 4))
ip_counts.plot(kind='bar', color='royalblue')
plt.title('Failed Login Attempts per IP Address')
plt.xlabel('IP Address')
plt.ylabel('Number of Failed Logins')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
# =====================================================
# ThreatEye - Day 3: AI Anomaly Detection (Isolation Forest)
# =====================================================

from sklearn.ensemble import IsolationForest
import numpy as np

print("\n=== AI-Based Anomaly Detection ===")

# Step 1: Prepare numeric features
# We'll use simple numeric representations for this demo
# (In real datasets, features come from many log attributes)
data['failed_flag'] = data['status'].apply(lambda x: 1 if x == 'failed' else 0)
data['user_encoded'] = data['user'].astype('category').cat.codes
data['ip_encoded'] = data['ip'].astype('category').cat.codes

features = data[['user_encoded', 'ip_encoded', 'failed_flag']]

# Step 2: Train Isolation Forest
model = IsolationForest(contamination=0.3, random_state=42)
model.fit(features)

# Step 3: Predict anomalies
data['anomaly'] = model.predict(features)  # -1 = anomaly, 1 = normal

# Step 4: Show results
print("\nAnomaly Detection Results:")
print(data[['timestamp', 'user', 'ip', 'status', 'anomaly']])

# Step 5: Visualize anomalies
plt.figure(figsize=(6,4))
colors = np.where(data['anomaly'] == -1, 'red', 'green')
plt.scatter(data['user_encoded'], data['ip_encoded'], c=colors)
plt.title('Anomaly Detection Visualization')
plt.xlabel('User (encoded)')
plt.ylabel('IP (encoded)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


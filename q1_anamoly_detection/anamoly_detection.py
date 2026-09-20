import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------
# 1. Read the dataset
# -----------------------------------

df = pd.read_csv("sample_metrics.csv")

print("===== AIOps Log Anomaly Detection =====")

# Display first few records
print("\nFirst 5 Records:")
print(df.head())

# -----------------------------------
# 2. Basic Statistics
# -----------------------------------

print("\n===== Basic Statistics =====")
print(df.describe())

# -----------------------------------
# 3. Total Records
# -----------------------------------

print("\nTotal Records:", len(df))

# -----------------------------------
# 4. Threshold-based Anomaly Detection
# -----------------------------------

CPU_THRESHOLD = 80

df["Anomaly"] = df["CPU Usage"] > CPU_THRESHOLD

# -----------------------------------
# 5. Display Anomalies
# -----------------------------------

anomalies = df[df["Anomaly"] == True]

print("\n===== Anomalies Detected =====")
print(anomalies)

print("\nTotal Anomalies:", len(anomalies))

# -----------------------------------
# 6. Display anomaly details
# -----------------------------------

print("\n===== Anomaly Details =====")

for index, row in anomalies.iterrows():
    print(
        f"Timestamp: {row['Timestamp']}, "
        f"CPU Usage: {row['CPU Usage']}%, "
        f"Memory Usage: {row['Memory Usage']}%, "
        f"Response Time: {row['Response Time']} ms"
    )

# -----------------------------------
# 7. Plot CPU Usage
# -----------------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    df["Timestamp"],
    df["CPU Usage"],
    marker="o",
    label="CPU Usage"
)

# Highlight anomalies
plt.scatter(
    anomalies["Timestamp"],
    anomalies["CPU Usage"],
    marker="x",
    s=100,
    label="Anomaly"
)

plt.axhline(
    y=CPU_THRESHOLD,
    linestyle="--",
    label="CPU Threshold"
)

plt.xlabel("Timestamp")
plt.ylabel("CPU Usage (%)")
plt.title("AIOps CPU Usage and Anomalies")

plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.savefig("anomaly_graph.png")

plt.show()
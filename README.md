# AI-Driven Financial Crime & AML Command Center 🕵️‍♂️

**A Capstone FinTech Project by Prajwal**

## Project Overview
Financial fraud is evolving. This project is an end-to-end detection system designed to identify sophisticated transaction patterns like **Smurfing** and **Account Takeovers**. It moves beyond simple reporting to provide AI-driven root cause analysis for security teams.

[dashboard_view.png.pdf](https://github.com/user-attachments/files/24686856/dashboard_view.png.pdf)


## 🛠️ Tech Stack
* **Python (Pandas/Faker):** Generated a synthetic dataset of 5,000+ banking transactions with injected fraud logic.
* **Power BI:** Built the visualization layer, Star Schema modeling, and Drill-Through architecture.
* **DAX:** Engineered risk metrics like `Fraud Rate %` and `Risk Ratios`.
* **AI Integration:** Implemented the 'Key Influencers' visual to detect statistical drivers of fraud.

## 🔍 Key Features
1. **Dynamic Risk Map:** Global heatmap that allows drill-down into specific cities.
2. **Forensic Drill-Through:** Right-click navigation from high-level maps to granular transaction evidence.
3. **AI Root Cause Analysis:** Automated detection of risk factors (e.g., "Electronics Category = 2.5x Risk").

## 💻 How to Run This
1. **The Data:** Check `data_generator.py` to see the Python logic used to simulate the fraud.
2. **The Dashboard:** Download `Fraud_Detection_Dashboard.pbix` and open it in Power BI Desktop.

---
*Created as part of the Master's in FinTech at UOW India.*

# 🌦️ Automated Weather Data Pipeline (ETL)

![Status](https://img.shields.io/badge/Status-Live-green?style=for-the-badge&logo=githubactions) ![Tools](https://img.shields.io/badge/Tools-Python%20|%20BigQuery%20|%20PowerBI-blue?style=for-the-badge)

## 📌 Project Overview
This project is an automated **End-to-End ETL Pipeline** that extracts real-time weather data for Bangalore, loads it into a Google BigQuery Data Warehouse, and visualizes trends on a Power BI Dashboard.

The system runs on autopilot, fully scheduled via **GitHub Actions** CI/CD to execute daily at 6:00 AM UTC.

**Key Objectives:**
* Automate data ingestion from an external REST API.
* Architect a cloud-based storage solution using **Google BigQuery**.
* Establish a real-time **DirectQuery** connection for up-to-the-minute reporting in Power BI.

---

## 🏗️ System Architecture
*The following diagram illustrates the end-to-end data flow, from raw JSON source to final BI visual.*
<img width="2816" height="1536" alt="architecture_diagram" src="https://github.com/user-attachments/assets/c83993c1-0f68-4d82-a5dc-556a86c2dcbe" />


---

## 📊 Live Dashboard Results
*A snapshot of the final Power BI report, showing the daily average temperature and historical data log, connected live to the cloud data warehouse.*
<img width="792" height="437" alt="dashboard_screenshot" src="https://github.com/user-attachments/assets/0873c763-8149-4cc8-afa8-d10bb4e670ba" />

---

## 🛠️ Tech Stack & Tools

| Category | Tool | Usage |
|----------|------|-------|
| **Scripting (ETL)** | 🐍 Python (Pandas) | Extracting JSON & transforming data structures |
| **Cloud Data Warehouse** | ☁️ Google BigQuery | Storing scalable, structured weather logs |
| **Orchestration** | ⚙️ GitHub Actions (CI/CD) | Scheduling the daily automated cron job |
| **Visualization (BI)** | 📊 Microsoft Power BI | DirectQuery connection for reporting |
| **Data Source** | 🌍 OpenWeather API | External raw data provider |

---

## ⚙️ How It Works (The Pipeline Steps)

1.  **Extraction (Python):**
    * An automated Python script hits the OpenWeather API endpoint.
    * It fetches the current temperature, humidity, and city metadata in JSON format.

2.  **Transformation (Pandas):**
    * The JSON data is parsed and flattened into a Pandas DataFrame.
    * Data types are correctly formatted (floats for temperature).
    * A precise UTC timestamp is added to every record to track data freshness and enable historical analysis.

3.  **Loading (BigQuery):**
    * The script authenticates securely with Google Cloud Platform using Service Account credentials stored in GitHub Secrets.
    * The transformed data is appended to the `bangalore_weather` table in **BigQuery**.

4.  **Visualization (Power BI):**
    * Power BI connects directly to BigQuery using **DirectQuery** mode.
    * The dashboard refreshes instantly to show the latest "snapshot" of weather data without needing to import the dataset locally.

---

## 💡 Key Learnings
* Bridging the gap between **Python scripting** and enterprise **Cloud Data Warehouses**.
* Resolving complex **Timezone conflicts** (UTC vs. Local Time) between database storage and BI frontend.
* Implementing **CI/CD workflows** to turn a manual script into a production-grade, automated background process.

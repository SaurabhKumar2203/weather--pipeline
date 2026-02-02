import requests
import pandas as pd
from datetime import datetime
from google.oauth2 import service_account
import pandas_gbq

# --- CONFIGURATION ---
API_KEY = "85b225d27c7e052d45df00b73ef53044"  # <--- PASTE YOUR API KEY HERE AGAIN
CITY = "Bangalore"
PROJECT_ID = "weather-pipeline-486212"            # <--- Updated Project ID
DATASET_ID = "weather_data"
TABLE_ID = "bangalore_weather"
CREDENTIALS_FILE = "service_account.json"

def fetch_weather_data():
    """Fetches data from OpenWeather API."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ API Error: {e}")
        return None

def transform_data(raw_json):
    """Flattens the JSON into a clean dictionary."""
    if not raw_json:
        return None
    
    weather_data = {
        "city": raw_json.get("name"),
        "temperature": raw_json["main"]["temp"] - 273.15,
        "humidity": raw_json["main"]["humidity"],
        "weather_description": raw_json["weather"][0]["description"],
        "wind_speed": raw_json["wind"]["speed"],
        "timestamp": datetime.now() # BigQuery handles datetime objects natively
    }
    return weather_data

def load_to_bigquery(data):
    """Uploads data to Google BigQuery."""
    if not data:
        print("⚠️ No data to upload.")
        return

    # 1. Create a DataFrame
    df = pd.DataFrame([data])

    # 2. Load Credentials
    credentials = service_account.Credentials.from_service_account_file(CREDENTIALS_FILE)

    # 3. Push to BigQuery
    table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"
    
    try:
        pandas_gbq.to_gbq(
            df,
            table_ref,
            project_id=PROJECT_ID,
            credentials=credentials,
            if_exists="append" 
        )
        print(f"✅ Success! Data uploaded to {table_ref}")
    except Exception as e:
        print(f"❌ Upload Error: {e}")

if __name__ == "__main__":
    print(f"🚀 Starting Cloud Pipeline for project: {PROJECT_ID}...")
    
    # E -> T -> L
    raw_data = fetch_weather_data()
    clean_data = transform_data(raw_data)
    load_to_bigquery(clean_data)
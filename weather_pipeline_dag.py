# windows_pipeline.py
from datetime import datetime
import collect_data
import preprocess

def run_pipeline():
    print(f"[{datetime.now()}] Starting Weather Data Pipeline...")

    # Step 1: Collect data
    print(f"[{datetime.now()}] Running data collection...")
    collect_data.collect_weather_data()

    # Step 2: Preprocess data
    print(f"[{datetime.now()}] Running preprocessing...")
    preprocess.main()

    print(f"[{datetime.now()}] Pipeline completed successfully!")

if __name__ == "__main__":
    run_pipeline()

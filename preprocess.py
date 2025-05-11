# preprocess.py
import pandas as pd
from sklearn.preprocessing import StandardScaler

def main():
    print("[Preprocessing] Reading raw data...")
    df = pd.read_csv("data/raw_data.csv")

    # Use the updated ffill syntax to avoid the FutureWarning
    df.ffill(inplace=True)

    print("[Preprocessing] Normalizing numerical fields...")
    scaler = StandardScaler()
    df[["temperature", "humidity", "wind_speed"]] = scaler.fit_transform(
        df[["temperature", "humidity", "wind_speed"]]
    )

    df.to_csv("processed_data.csv", index=False)
    print("[Preprocessing] Data saved to processed_data.csv")

# For manual testing
if __name__ == "__main__":
    main()

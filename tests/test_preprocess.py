import pytest
from unittest import mock
import pandas as pd
from ..preprocess import main
from sklearn.preprocessing import StandardScaler

# Sample raw data for testing
raw_data = {
    "datetime": ["2025-05-11T00:00:00", "2025-05-11T01:00:00"],
    "temperature": [25.0, 28.0],
    "humidity": [60, 65],
    "wind_speed": [10, 12],
    "condition": ["Clear", "Cloudy"]
}

# Expected processed data after normalization
processed_data = {
    "datetime": ["2025-05-11T00:00:00", "2025-05-11T01:00:00"],
    "temperature": [-1.0, 1.0],  # After normalization, values should be different
    "humidity": [-1.0, 1.0],
    "wind_speed": [-1.0, 1.0],
    "condition": ["Clear", "Cloudy"]
}

# Mock the pandas read_csv and to_csv methods
@mock.patch("pandas.read_csv")
@mock.patch("pandas.DataFrame.to_csv")
def test_preprocess(mock_read_csv, mock_to_csv):
    # Create a mock DataFrame for the raw data
    df_raw = pd.DataFrame(raw_data)
    mock_read_csv.return_value = df_raw

    # Mocking StandardScaler to return the processed data directly
    mock_scaler = mock.Mock(spec=StandardScaler)
    mock_scaler.fit_transform.return_value = pd.DataFrame(processed_data)[["temperature", "humidity", "wind_speed"]]

    # Call the main function to test preprocessing
    with mock.patch("sklearn.preprocessing.StandardScaler", return_value=mock_scaler):
        main()

    # Assert read_csv was called with the correct file path
    mock_read_csv.assert_called_once_with("data/raw_data.csv")

    # Check that the forward fill was applied (i.e., ffill method called)
    assert df_raw.ffill.called

    # Ensure that to_csv was called with the correct output file path
    mock_to_csv.assert_called_once_with("processed_data.csv", index=False)

    # Check that the normalization was applied correctly on the columns
    pd.testing.assert_frame_equal(
        mock_scaler.fit_transform.return_value,
        pd.DataFrame(processed_data)[["temperature", "humidity", "wind_speed"]]
    )


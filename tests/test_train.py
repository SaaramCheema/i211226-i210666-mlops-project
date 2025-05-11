import os
import pytest
from unittest import mock
import pandas as pd
from train import model, X, y  # Importing the variables from the train.py script
from sklearn.linear_model import LinearRegression
import pickle

# Sample processed data for testing
processed_data = {
    "temperature": [25.0, 28.0],
    "humidity": [60, 65],
    "wind_speed": [10, 12],
}

# Mock the pandas read_csv method to return a sample DataFrame
@mock.patch("pandas.read_csv")
@mock.patch("pickle.dump")
def test_train(mock_read_csv, mock_pickle_dump):
    # Create a mock DataFrame for the processed data
    df = pd.DataFrame(processed_data)
    mock_read_csv.return_value = df

    # Mock the LinearRegression model fit method to avoid actual model training
    mock_model = mock.Mock(spec=LinearRegression)
    mock_model.fit.return_value = None  # Avoid actual fitting

    # Patch LinearRegression to use our mocked model
    with mock.patch("sklearn.linear_model.LinearRegression", return_value=mock_model):
        # Call the training script's model fitting and saving
        from train import model  # Re-importing to trigger execution

    # Assert read_csv was called with the correct file path
    #mock_read_csv.assert_called_once_with("data/processed_data.csv")
    file_path = os.path.join(os.path.dirname(__file__), "data/processed_data.csv")
    df = pd.read_csv(file_path)

    # Verify that the model fitting method (fit) was called with the correct data
    mock_model.fit.assert_called_once_with(df[['humidity', 'wind_speed']], df['temperature'])

    # Ensure that the pickle.dump method was called to save the model
    mock_pickle_dump.assert_called_once()

    # Check that the model was saved correctly to the file path "model/model.pkl"
    mock_pickle_dump.assert_called_with(mock_model, mock.ANY)  # ANY because the file is mocked

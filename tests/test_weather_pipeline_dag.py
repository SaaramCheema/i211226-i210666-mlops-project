import pytest
from unittest import mock
from windows_pipeline import run_pipeline
from datetime import datetime

# Mocking the collect_data.collect_weather_data and preprocess.main functions
@mock.patch("collect_data.collect_weather_data")
@mock.patch("preprocess.main")
@mock.patch("builtins.print")  # Mock print to verify log messages
def test_run_pipeline(mock_print, mock_preprocess, mock_collect_data):
    # Call the run_pipeline function
    run_pipeline()

    # Check that collect_weather_data was called
    mock_collect_data.assert_called_once()

    # Check that preprocess.main was called
    mock_preprocess.assert_called_once()

    # Verify that print was called with the correct start and end messages
    expected_start_message = f"[{datetime.now()}] Starting Weather Data Pipeline..."
    expected_collect_data_message = f"[{datetime.now()}] Running data collection..."
    expected_preprocess_message = f"[{datetime.now()}] Running preprocessing..."
    expected_end_message = f"[{datetime.now()}] Pipeline completed successfully!"

    # Check if print was called with the expected messages
    mock_print.assert_any_call(expected_start_message)
    mock_print.assert_any_call(expected_collect_data_message)
    mock_print.assert_any_call(expected_preprocess_message)
    mock_print.assert_any_call(expected_end_message)

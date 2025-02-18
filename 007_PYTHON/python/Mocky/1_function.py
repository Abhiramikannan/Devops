import requests
from typing import Dict
from unittest.mock import patch
import unittest

# The function to be tested
def get_data(url: str) -> Dict[str, str]:
    response = requests.get(url)
    return response.json()  # Ensure you call .json() here, not reference it

# Test class
class TestGetData(unittest.TestCase):

    @patch('requests.get')  # Mock the 'requests.get' method
    def test_get_data(self, mock_get: patch) -> None:
        # Create a mock response object
        mock_response = mock_get.return_value
        mock_response.json.return_value = {'key': 'value'}  # Define the mock return value for json()

        # Call the function with a dummy URL
        result = get_data('https://example.com/api')
        print(result)  # For debugging, can be removed for final test

        # Assert that the result is as expected
        self.assertEqual(result, {'key': 'value'})

        # Ensure that the 'requests.get' method was called once with the correct URL
        mock_get.assert_called_once_with('https://example.com/api')

if __name__ == "__main__":
    unittest.main()

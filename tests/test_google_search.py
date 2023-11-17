import unittest
from unittest.mock import patch
from actions.google_search import google_search 

class TestGoogleSearch(unittest.TestCase):

    @patch('requests.get')
    def test_google_search(self, mock_get):
        # Mock response data
        mock_response = {
            "items": [
                {"title": "Test Title 1", "link": "http://example.com/1"},
                {"title": "Test Title 2", "link": "http://example.com/2"}
            ]
        }

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        test_query = "test_query"
        with patch.dict('os.environ', {'GOOGLE_API_KEY': 'test_google_api_key', 'CSE_ID': 'test_cse_id'}):
            response = google_search(test_query)

        mock_get.assert_called_once_with(
            f"https://www.googleapis.com/customsearch/v1?q={test_query}&key=test_google_api_key&cx=test_cse_id"
        )

        self.assertEqual(response, mock_response)

if __name__ == '__main__':
    unittest.main()
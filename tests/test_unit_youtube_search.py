import unittest
from unittest.mock import patch, Mock
from actions.youtube_search import youtube_search

class TestYouTubeSearch(unittest.TestCase):

    @patch('requests.get')
    def test_youtube_search_success(self, mock_get):
        mock_response = Mock()
        expected_dict = {
            "items": [{"id": {"videoId": "xyz"}, "snippet": {"title": "Test video"}}]
        }
        mock_response.json.return_value = expected_dict
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        with patch.dict('os.environ', {'GOOGLE_API_KEY': 'test_google_api_key'}):
            response = youtube_search("test query")

        self.assertEqual(response, expected_dict)

    @patch('requests.get')
    def test_youtube_search_failure(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {"error": "API error"}
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        with patch.dict('os.environ', {'GOOGLE_API_KEY': 'test_google_api_key'}):
            response = youtube_search("test query")

        self.assertIn("error", response)

if __name__ == '__main__':
    unittest.main()
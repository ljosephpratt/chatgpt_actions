import unittest
import os
from actions.youtube_search import youtube_search  # Replace with the actual module name

class TestYouTubeSearchIntegration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Ensure the API key is set
        cls.api_key = os.getenv("GOOGLE_API_KEY")
        if not cls.api_key:
            raise unittest.SkipTest("Google API key not set. Skipping integration tests.")

    def test_youtube_search_integration(self):
        # Perform a search with a known query
        query = "Python programming"
        response = youtube_search(query)

        # Basic checks to validate response structure
        self.assertIn('items', response)
        self.assertIsInstance(response['items'], list)

        # Depending on the API, you might want to check more details of the response
        # For example, checking if the items list is not empty
        self.assertTrue(len(response['items']) > 0)

if __name__ == '__main__':
    unittest.main()
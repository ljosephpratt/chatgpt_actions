import unittest, os
from actions.youtube_search import youtube_search

class TestYouTubeSearchIntegration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api_key = os.getenv("GOOGLE_API_KEY")
        if not cls.api_key:
            raise unittest.SkipTest("Google API key not set. Skipping integration tests.")

    def test_youtube_search_integration(self):
        query = "Python programming"
        response = youtube_search(query)

        self.assertIn('items', response)
        self.assertIsInstance(response['items'], list)

        self.assertTrue(len(response['items']) > 0)

if __name__ == '__main__':
    unittest.main()
import unittest
import os
from actions.google_search import google_search

class GoogleSearchIntegrationTest(unittest.TestCase):
    def setUpClass(cls):
        # Ensure the API key is set
        cls.api_key = os.getenv("GOOGLE_API_KEY")
        if not cls.api_key:
            raise unittest.SkipTest("Google API key not set. Skipping integration tests.")

    def test_google_search_integration(self):
        query = "Python programming"
        response = google_search(query)

        self.assertIn('items', response)
        self.assertIsInstance(response['items'], list)

if __name__ == '__main__':
    unittest.main()
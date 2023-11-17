import requests, os

def google_search(query):
    google_api_key = os.getenv("GOOGLE_API_KEY")
    cse_id = os.getenv("CSE_ID")
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={google_api_key}&cx={cse_id}"
    response = requests.get(url)
    return response.json()
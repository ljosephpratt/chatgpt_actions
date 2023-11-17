import requests, os

def youtube_search(query):
    google_api_key = os.getenv("GOOGLE_API_KEY")
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&key={google_api_key}"
    response = requests.get(url)
    return response.json()
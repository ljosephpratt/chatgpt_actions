# ChatGPT Actions

## Overview

ChatGPT Actions is a custom ChatGPT bot integrated with Google and YouTube search capabilities.

## Suggested Project Structure

your-chatgpt-bot-project/
│
├── .gitignore          # List of files and directories ignored by git
├── README.md           # Project description and instructions
│
├── actions/            # Directory for ChatGPT actions
│   ├── google_search.py
│   ├── youtube_search.py
│   └── other_actions.py
│
├── config/             # Configuration files (not committed)
│   └── config.example.json  # Example config file template
│
├── src/                # Source code of the ChatGPT bot
│   ├── main.py         # Main application script
│   └── other_modules/  # Other necessary modules and scripts
│
├── requirements.txt    # Python dependencies
└── tests/              # Unit and integration tests
    ├── test_google_search.py
    ├── test_youtube_search.py
    └── other_tests.py

## Setup

1. Clone the repository

```sh
git clone [repository URL]
```

1. Install dependencies:

```sh
pip install -r requirements.txt
```

1. Set environment variables for API keys:

```sh
export GOOGLE_API_KEY='your_google_api_key'
export YOUTUBE_API_KEY='your_youtube_api_key'
```

## Running the Bot

To run the bot, execute:

```python
python src/main.py
```

## Features

- Google Search Integration
- YouTube Search Integration

## License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License - see the [LICENSE](https://creativecommons.org/licenses/by-nc/4.0/legalcode) file for details.

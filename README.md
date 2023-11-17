# ChatGPT Actions

## Overview

ChatGPT Actions is a custom ChatGPT Actions integrated with Google and YouTube search capabilities.

## Features

- Google Search Integration
- YouTube Search Integration

## Suggested Project Structure

```graphql
chatgpt_actions/
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
├── requirements.txt    # Python dependencies
└── tests/              # Unit and integration tests
    ├── test_google_search.py
    ├── test_youtube_search.py
    └── other_tests.py
```

## Setup

1. Clone the repository

```sh
git clone https://github.com/ljosephpratt/chatgpt_actions
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

## Unit and Integration Testing

### Run All Tests

```sh
 python -m unittest discover -s tests -p "test_*.py"
```

### Run Unit Tests

```sh
 python -m unittest discover -s tests -p "test_unit_*.py"
```

### Run Integration Tests

```sh
 python -m unittest discover -s tests -p "test_integration_*.py"
```

## License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License - see the [LICENSE](https://creativecommons.org/licenses/by-nc/4.0/legalcode) file for details.

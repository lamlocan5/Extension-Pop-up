# Extension Pop-up Powered AI

A Chrome extension with Python backend that integrates artificial intelligence to provide language learning tools and improve users' writing skills through an intuitive pop-up interface.

## Project Overview

This extension enhances web browsing by offering translation, vocabulary practice, pronunciation guides, and content automation directly within the browser. When users highlight text on a webpage, a smart pop-up appears with various AI-powered language tools, powered by a Python backend with state-of-the-art AI models.

## Architecture

This project follows a client-server architecture:
- **Chrome Extension**: Frontend interface that users interact with (JavaScript, HTML, CSS)
- **Python Backend**: API server that processes requests and provides AI functionality (FastAPI)
- **AI Models**: State-of-the-art models for text processing, translation, and speech

## Features

- **AI Translation**: Translate highlighted text with phonetics, meanings, and definitions
- **Smart Flashcards**: Automatically generate vocabulary flashcards
- **Text-to-Speech**: Hear pronunciation in multiple languages
- **Grammar Checking**: Get suggestions for grammar improvements
- **Image Search**: Find images related to highlighted text
- **Text Summarization**: Generate concise summaries of lengthy content

**VIP Features:**
- Accent pronunciation check
- Writing enhancement suggestions
- Automatic word recommendations based on flashcards
- AI content detection
- Content humanization

## Tech Stack

### Frontend (Chrome Extension)
- HTML5, CSS3, JavaScript
- Chrome Extension APIs
- Fetch API for communicating with backend

### Backend (Python)
- FastAPI: Modern, high-performance web framework
- Pydantic: Data validation and settings management
- SQLAlchemy: Database ORM (for user data and flashcards)
- Redis: Caching for API responses
- Docker: Containerization for deployment

### AI Models & Libraries
- Gemini Flash-Lite 2: Translation, summarization, writing enhancement
- Google Cloud Text-to-Speech: Pronunciation
- coqui/XTTS-v2: Advanced multilingual TTS
- whisper-large-v3: Speech recognition and accent analysis
- LanguageTool API: Grammar checking
- Microsoft Bing Image Search API: Image search

## Project Structure

```
extension-popup-powered-ai/
├── README.md                     # Project overview and documentation
├── extension/                    # Chrome extension frontend
│   ├── manifest.json             # Extension configuration
│   ├── assets/                   # Static assets (icons, stylesheets)
│   ├── popup/                    # Extension popup interface
│   ├── content/                  # Content scripts
│   ├── background/               # Background scripts
│   └── options/                  # Extension options page
│
├── backend/                      # Python backend API
│   ├── app/                      # Main application package
│   │   ├── __init__.py           # Package initialization
│   │   ├── main.py               # FastAPI application entry point
│   │   ├── api/                  # API routes
│   │   │   ├── __init__.py
│   │   │   ├── routes/           # API endpoints
│   │   │   │   ├── __init__.py
│   │   │   │   ├── translation.py # Translation endpoints
│   │   │   │   ├── tts.py        # Text-to-speech endpoints
│   │   │   │   ├── grammar.py    # Grammar checking endpoints
│   │   │   │   ├── flashcards.py # Flashcard endpoints
│   │   │   │   ├── images.py     # Image search endpoints
│   │   │   │   └── summary.py    # Summarization endpoints
│   │   │   └── vip/              # VIP feature endpoints
│   │   │       ├── __init__.py
│   │   │       ├── accent.py     # Accent checking
│   │   │       ├── writing.py    # Writing enhancement
│   │   │       ├── detection.py  # AI content detection
│   │   │       └── humanize.py   # Content humanization
│   │   ├── core/                 # Core application code
│   │   │   ├── __init__.py
│   │   │   ├── config.py         # Application configuration
│   │   │   ├── security.py       # Authentication and security
│   │   │   └── database.py       # Database connection
│   │   ├── db/                   # Database models and repositories
│   │   │   ├── __init__.py
│   │   │   ├── models/           # SQLAlchemy models
│   │   │   └── repositories/     # Database access
│   │   ├── services/             # Business logic services
│   │   │   ├── __init__.py
│   │   │   ├── translation.py    # Translation service
│   │   │   ├── tts.py            # Text-to-speech service
│   │   │   ├── grammar.py        # Grammar checking service
│   │   │   ├── flashcards.py     # Flashcard service
│   │   │   ├── images.py         # Image search service
│   │   │   └── summary.py        # Summarization service
│   │   └── ml/                   # Machine learning models
│   │       ├── __init__.py
│   │       ├── translation/      # Translation models
│   │       ├── tts/              # Text-to-speech models
│   │       ├── grammar/          # Grammar checking models
│   │       └── summarization/    # Text summarization models
│   ├── tests/                    # Tests for backend code
│   │   ├── __init__.py
│   │   ├── conftest.py           # Test configuration
│   │   ├── unit/                 # Unit tests
│   │   └── integration/          # Integration tests
│   ├── alembic/                  # Database migrations
│   ├── .env                      # Environment variables (not in repo)
│   ├── .env.example              # Example environment variables
│   ├── requirements.txt          # Python dependencies
│   ├── Dockerfile                # Container definition
│   └── docker-compose.yml        # Service orchestration
│
└── docs/                         # Documentation
    ├── api/                      # API documentation
    ├── architecture/             # Architecture diagrams
    ├── deployment/               # Deployment guides
    └── user-guides/              # User documentation
```

## Getting Started

### Backend Setup

1. Clone the repository
2. Navigate to the backend directory: `cd extension-popup-powered-ai/backend`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Create a `.env` file based on `.env.example`
7. Start the development server: `uvicorn app.main:app --reload`

### Extension Setup

1. Navigate to the extension directory: `cd extension-popup-powered-ai/extension`
2. Open Chrome and go to `chrome://extensions/`
3. Enable "Developer mode"
4. Click "Load unpacked" and select the extension directory

## Development

### Backend Development

- Run tests: `pytest -v`
- Generate migration: `alembic revision --autogenerate -m "message"`
- Apply migration: `alembic upgrade head`
- Start server with hot reload: `uvicorn app.main:app --reload`

### Extension Development

- Load unpacked extension in Chrome
- After changes, reload the extension in Chrome Extensions page

## Deployment

### Backend Deployment

The Python backend can be deployed using Docker:

```bash
cd backend
docker-compose up -d
```

For production deployment, consider using:
- AWS Lambda + API Gateway
- Google Cloud Run
- Heroku

### Extension Deployment

1. Build the extension
2. Package it as a ZIP file
3. Upload to the Chrome Web Store

## AI Integration Best Practices

- Use API key rotation and secure storage
- Implement rate limiting for API calls
- Create fallback mechanisms for offline usage
- Process sensitive data locally when possible
- Use model quantization for performance
- Implement streaming for large responses

## License
[MIT License](LICENSE)
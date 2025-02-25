# Extension Pop-up Powered AI Architecture

This document explains the overall architecture of the Extension Pop-up Powered AI system, how components interact, and the design decisions.

## System Overview

The Extension Pop-up Powered AI is a browser extension with a Python backend that provides language learning and writing enhancement tools. The system follows a client-server architecture:

- **Frontend**: Chrome extension (JavaScript, HTML, CSS)
- **Backend**: FastAPI server (Python)

## Component Diagram

```
+----------------------+      HTTP      +------------------------+
|                      |   Requests     |                        |
|  Chrome Extension    |<-------------->|  FastAPI Backend       |
|                      |                |                        |
+----------------------+                +------------------------+
         |                                         |
         v                                         v
+----------------------+                +------------------------+
|                      |                |                        |
|  Browser Storage     |                |  Database              |
|  (flashcards, etc.)  |                |  (flashcards, etc.)    |
|                      |                |                        |
+----------------------+                +------------------------+
                                                 |
                                                 v
                                        +------------------------+
                                        |                        |
                                        |  AI Services           |
                                        |  - Translation         |
                                        |  - TTS                 |
                                        |  - Grammar             |
                                        |  - Summarization       |
                                        |  - Image Search        |
                                        |  - VIP Features        |
                                        +------------------------+
```

## Frontend Architecture

The Chrome extension frontend consists of the following components:

### Content Script

- Injected into web pages
- Listens for user text selection
- Shows a popup with action buttons near the selected text
- Communicates with the background script

### Background Script

- Manages extension lifecycle
- Sets up context menu items
- Coordinates communication between content script and popup
- Manages API requests to backend

### Popup UI

- User interface for accessing all features
- Tabbed interface for different tools
- Communication with backend API

## Backend Architecture

The backend is organized following domain-driven design principles:

### API Layer

- `app/api/routes/` - API endpoints for core features
- `app/api/vip/` - API endpoints for premium features
- Both use FastAPI routers for organization

### Service Layer

- `app/services/` - Core service implementations
- `app/services/vip/` - Premium service implementations
- Services encapsulate business logic and external API calls

### Data Layer

- `app/db/models/` - SQLAlchemy ORM models
- `app/core/database.py` - Database connection setup
- Uses SQLite for development and can be switched to PostgreSQL for production

### ML Layer

- `app/ml/` - Machine learning model integrations
- Abstracts ML operations from services

## Authentication and Authorization

The system uses a simple API key-based authentication for the backend:

1. API keys stored in environment variables
2. Middleware validates API key for all requests
3. VIP features require additional authorization

## Data Flow

### Translation Flow

1. User selects text on a webpage
2. Content script displays popup with action buttons
3. User clicks "Translate"
4. Request sent to backend `/api/v1/translation` endpoint
5. Backend translation service processes request
6. Response rendered in popup

### Flashcard Flow

1. User selects text in popup or on webpage
2. User chooses to create flashcard
3. Frontend sends data to backend `/api/v1/flashcards` endpoint
4. Backend creates flashcard in database
5. Confirmation returned to user

## Extensibility

The system is designed for extensibility:

1. New language tools can be added by:
   - Creating a new route in the API layer
   - Implementing the service logic
   - Adding a new tab in the frontend UI

2. VIP features follow the same pattern but in separate modules

## Future Architectural Considerations

- **Serverless Deployment**: Backend functions could be refactored as serverless functions
- **WebSocket Support**: For real-time features like dictation
- **Federated Learning**: On-device ML for privacy-sensitive features
- **Caching Layer**: Redis integration for performance optimization 
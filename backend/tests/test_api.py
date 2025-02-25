import pytest
from fastapi.testclient import TestClient

def test_health_check(client):
    """
    Test the health check endpoint.
    """
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_translation_api(client):
    """
    Test the translation API endpoint.
    """
    request_data = {
        "text": "Hello, how are you?",
        "target_language": "es"
    }
    
    response = client.post("/api/v1/translation", json=request_data)
    assert response.status_code == 200
    
    result = response.json()
    assert "translated_text" in result
    assert "source_language" in result

def test_tts_api(client):
    """
    Test the text-to-speech API endpoint.
    """
    request_data = {
        "text": "Hello, this is a test.",
        "language_code": "en-US",
        "voice_name": "en-US-Standard-A"
    }
    
    response = client.post("/api/v1/tts", json=request_data)
    assert response.status_code == 200
    
    result = response.json()
    assert "audio_content" in result

def test_summary_api(client):
    """
    Test the summary API endpoint.
    """
    # Create a longer text for summarization
    long_text = "This is a long text that should be summarized. " * 10
    
    request_data = {
        "text": long_text,
        "max_length": 100
    }
    
    response = client.post("/api/v1/summary", json=request_data)
    assert response.status_code == 200
    
    result = response.json()
    assert "summary" in result
    assert "original_length" in result
    assert "summary_length" in result
    assert result["summary_length"] <= 100 
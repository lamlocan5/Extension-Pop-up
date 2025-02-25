async def check_grammar(text: str, language: str = "en-US"):
    """
    Check grammar and provide improvement suggestions.
    
    Args:
        text: The text to check
        language: Language code
        
    Returns:
        Dictionary with:
        - original text
        - list of grammar errors
        - improved text
    """
    # This is a mock implementation
    # In a real implementation, you would call a grammar checking API
    
    # Mock grammar errors for demonstration
    mock_errors = []
    
    # Example errors for demonstration
    if "their" in text:
        mock_errors.append({
            "start": text.find("their"),
            "end": text.find("their") + 5,
            "message": "Consider whether 'there' or 'they're' would be more appropriate here.",
            "suggestions": ["there", "they're"]
        })
    
    if "its" in text and "it's" not in text:
        mock_errors.append({
            "start": text.find("its"),
            "end": text.find("its") + 3,
            "message": "Check whether you need the possessive 'its' or the contraction 'it's' (it is).",
            "suggestions": ["it's"]
        })
    
    # Generate improved text (just a mock example)
    improved_text = text
    
    # In a real implementation, you'd use a grammar checking service
    # to analyze the text and provide suggestions
    
    return {
        "text": text,
        "errors": mock_errors,
        "improved_text": improved_text if not mock_errors else None
    } 
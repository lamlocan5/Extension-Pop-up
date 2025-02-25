from app.core.config import settings

async def summarize_text(text: str, max_length: int = 200):
    """
    Generate a summary of the text using AI.
    
    Args:
        text: The text to summarize
        max_length: Maximum length of the summary in characters
        
    Returns:
        Summarized text
    """
    # This is a mock implementation
    # In a real implementation, you would call an AI model or API
    
    # Simple mock summarization - just takes the first few sentences
    sentences = text.split('. ')
    
    # Take the first 1/3 of sentences, or at least 1 sentence
    summary_sentences = sentences[:max(1, len(sentences) // 3)]
    summary = '. '.join(summary_sentences)
    
    # Add period if needed
    if summary and not summary.endswith('.'):
        summary += '.'
    
    # Ensure the summary doesn't exceed max_length
    if len(summary) > max_length:
        summary = summary[:max_length-3] + '...'
    
    return summary
    
    # Real implementation using an AI model would look like:
    """
    from openai import AsyncOpenAI
    
    client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
    
    response = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Summarize the following text concisely."},
            {"role": "user", "content": text}
        ],
        max_tokens=max_length // 4,  # approximation for token to char ratio
    )
    
    return response.choices[0].message.content.strip()
    """ 
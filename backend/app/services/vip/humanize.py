from app.core.config import settings
import re

async def humanize_content(text: str, style: str = "conversational"):
    """
    Make machine-generated content sound more human.
    
    Args:
        text: The text to humanize
        style: The desired writing style (conversational, professional, casual, creative)
        
    Returns:
        Dictionary with humanized text and number of changes made
    """
    # This is a mock implementation
    # In a real implementation, you would call an AI model or API
    
    # Simple humanization rules
    changes = 0
    humanized_text = text
    
    # Add contractions
    if "it is" in humanized_text:
        humanized_text = re.sub(r'\bit is\b', "it's", humanized_text)
        changes += humanized_text.count("it's")
    
    if "cannot" in humanized_text:
        humanized_text = humanized_text.replace("cannot", "can't")
        changes += humanized_text.count("can't")
    
    # Add filler words based on style
    if style == "conversational":
        # Add occasional filler words
        sentences = humanized_text.split('. ')
        if len(sentences) > 2:
            sentences[1] = "Well, " + sentences[1].lower()
            changes += 1
        
        if len(sentences) > 4:
            sentences[3] = "You know, " + sentences[3].lower()
            changes += 1
            
        humanized_text = '. '.join(sentences)
    
    # Vary sentence structure
    if style == "creative" and "," in humanized_text:
        # Find a sentence with a comma and rearrange it
        sentences = humanized_text.split('. ')
        for i, sentence in enumerate(sentences):
            if ',' in sentence:
                parts = sentence.split(', ', 1)
                if len(parts) == 2:
                    sentences[i] = parts[1] + ' - ' + parts[0].lower()
                    changes += 1
                    break
                    
        humanized_text = '. '.join(sentences)
    
    return {
        "humanized_text": humanized_text,
        "changes_made": changes
    }
    
    # Real implementation using an AI model would look like:
    """
    from openai import AsyncOpenAI
    
    client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
    
    response = await client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": f"You are a content humanizer. Rewrite the following AI-generated text to sound more natural and human-like, in a {style} style. Keep the same meaning but make it less formulaic and more authentic."},
            {"role": "user", "content": text}
        ]
    )
    
    humanized_text = response.choices[0].message.content
    
    # Simple method to estimate number of changes
    from difflib import SequenceMatcher
    
    def similarity(a, b):
        return SequenceMatcher(None, a, b).ratio()
    
    sim = similarity(text, humanized_text)
    changes_made = int((1 - sim) * 100)  # rough estimate of percentage change
    
    return {
        "humanized_text": humanized_text,
        "changes_made": changes_made
    }
    """ 
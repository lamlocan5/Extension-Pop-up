# Extension Pop-up Powered AI User Guide

Welcome to the Extension Pop-up Powered AI! This guide will help you get started with using all the features available in this Chrome extension.

## Installation

### Installing from Chrome Web Store

1. Go to the Chrome Web Store
2. Search for "Extension Pop-up Powered AI"
3. Click "Add to Chrome"
4. Confirm the installation when prompted

### Installing in Developer Mode

1. Download or clone the repository
2. Open Chrome and go to `chrome://extensions/`
3. Enable "Developer mode" in the top-right corner
4. Click "Load unpacked" and select the `extension` folder
5. The extension should now appear in your Chrome toolbar

## Getting Started

After installing the extension, you'll see the extension icon in your Chrome toolbar. To use the AI-powered features:

1. Highlight any text on a webpage
2. A small popup will appear near your selection with action buttons
3. Alternatively, right-click on selected text and use the context menu
4. You can also click the extension icon to open the full popup interface

## Features

### Translation

Translate selected text to any supported language:

1. Select text on a webpage
2. Click the "Translate" button in the popup
3. Choose your target language from the dropdown
4. View the translation, pronunciation guide, and definitions

### Pronunciation

Hear the correct pronunciation of selected text:

1. Select text containing words or phrases
2. Click the "Listen" button
3. An audio player will appear with the pronunciation
4. Use the "Record" button to practice and compare your pronunciation

### Grammar Check

Check your writing for grammar and style improvements:

1. Select text you want to check
2. Click the "Grammar" button
3. View suggestions and corrections
4. Apply suggestions with a single click

### Flashcards

Create flashcards for vocabulary learning:

1. Select a word or phrase
2. Click the "Flashcard" button
3. Edit the front (word) and back (definition) if needed
4. Click "Create Flashcard"
5. Access your flashcards in the extension popup anytime

### Image Search

Find images related to selected text:

1. Select a word or phrase
2. Click the "Images" button
3. View relevant images
4. Click any image to open it in a new tab

### Summarization

Summarize long texts:

1. Select a paragraph or longer text
2. Click the "Summary" button
3. View a concise summary of the selected text

## VIP Features

The following features are available to premium users:

### Accent Training

Improve your accent with AI feedback:

1. Navigate to the "Pronunciation" tab
2. Click "Record Your Pronunciation"
3. Speak the displayed reference text
4. Receive detailed feedback on your accent
5. View specific suggestions for improvement

### Writing Enhancement

Get professional writing assistance:

1. Select text you want to enhance
2. Go to the extension popup and select the "VIP" tab
3. Choose "Enhance Writing"
4. Select your desired tone and target audience
5. Receive improved text and detailed suggestions

### AI Content Detection

Detect whether content was written by AI:

1. Select the text you want to analyze
2. Go to the VIP tab and select "Detect AI"
3. View the probability that the text was AI-generated
4. See confidence score and assessment

### Content Humanization

Make AI-generated content sound more human:

1. Select AI-generated text
2. Go to the VIP tab and select "Humanize"
3. Choose your desired writing style
4. Receive more natural-sounding text

## Troubleshooting

### Extension Not Working

If the extension isn't working as expected:

1. Make sure you're connected to the internet
2. Check that the backend server is running (if self-hosted)
3. Try refreshing the page
4. Reinstall the extension if problems persist

### Backend Server Issues

If you're hosting your own backend:

1. Make sure the server is running at `http://localhost:8000`
2. Check the server logs for errors
3. Ensure your API keys are properly configured in the `.env` file

### Performance Issues

If the extension is running slowly:

1. Try processing smaller amounts of text at once
2. Close unused tabs to free up memory
3. Check your internet connection speed

## Privacy

This extension processes text you select. Here's how your data is handled:

1. Selected text is sent to the backend for processing
2. Backend API keys are kept secure using environment variables
3. No data is stored unless you explicitly save it (e.g., flashcards)
4. All API requests are made over HTTPS for security

## Getting Help

If you need additional help:

1. Check the documentation in the `docs` folder
2. Submit an issue on GitHub
3. Contact support at support@extension-popup-ai.example.com 
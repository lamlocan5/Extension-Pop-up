// Initialize variables
let selectedText = '';
let popup = null;
const API_BASE_URL = 'http://localhost:8000/api/v1';

// Create a popup element
function createPopup() {
  // Remove existing popup if any
  if (popup) {
    document.body.removeChild(popup);
  }
  
  // Create new popup element
  popup = document.createElement('div');
  popup.className = 'ai-extension-popup';
  popup.style.display = 'none';
  document.body.appendChild(popup);
  
  return popup;
}

// Position the popup near the selected text
function positionPopup(selection) {
  const range = selection.getRangeAt(0);
  const rect = range.getBoundingClientRect();
  
  // Position the popup below the selection
  popup.style.top = `${window.scrollY + rect.bottom + 10}px`;
  popup.style.left = `${window.scrollX + rect.left}px`;
  
  // Make sure popup doesn't go off screen
  const popupRect = popup.getBoundingClientRect();
  if (popupRect.right > window.innerWidth) {
    popup.style.left = `${window.innerWidth - popupRect.width - 20}px`;
  }
}

// Show popup with actions
function showActionsPopup(selection) {
  selectedText = selection.toString().trim();
  if (!selectedText) return;
  
  // Create or get the popup
  popup = popup || createPopup();
  
  // Position the popup
  positionPopup(selection);
  
  // Set popup content
  popup.innerHTML = `
    <div class="ai-extension-popup-header">
      <span>AI Tools</span>
      <button class="ai-extension-popup-close">&times;</button>
    </div>
    <div class="ai-extension-popup-actions">
      <button class="ai-extension-popup-button" data-action="translation">Translate</button>
      <button class="ai-extension-popup-button" data-action="pronunciation">Pronounce</button>
      <button class="ai-extension-popup-button" data-action="grammar">Check Grammar</button>
      <button class="ai-extension-popup-button" data-action="flashcards">Add to Flashcards</button>
      <button class="ai-extension-popup-button" data-action="images">Find Images</button>
      <button class="ai-extension-popup-button" data-action="summary">Summarize</button>
    </div>
  `;
  
  // Add event listeners
  popup.querySelector('.ai-extension-popup-close').addEventListener('click', () => {
    popup.style.display = 'none';
  });
  
  // Add action event listeners
  const actionButtons = popup.querySelectorAll('.ai-extension-popup-button');
  actionButtons.forEach(button => {
    button.addEventListener('click', (e) => {
      const action = e.target.getAttribute('data-action');
      handleAction(action);
    });
  });
  
  // Show the popup
  popup.style.display = 'block';
}

// Handle different actions
async function handleAction(action) {
  popup.style.display = 'none';
  
  switch (action) {
    case 'translation':
      chrome.runtime.sendMessage({
        action: 'openPopup',
        tab: 'translation',
        text: selectedText
      });
      break;
    case 'pronunciation':
      chrome.runtime.sendMessage({
        action: 'openPopup',
        tab: 'pronunciation',
        text: selectedText
      });
      break;
    case 'grammar':
      chrome.runtime.sendMessage({
        action: 'openPopup',
        tab: 'grammar',
        text: selectedText
      });
      break;
    case 'flashcards':
      chrome.runtime.sendMessage({
        action: 'openPopup',
        tab: 'flashcards',
        text: selectedText
      });
      break;
    case 'images':
      chrome.runtime.sendMessage({
        action: 'openPopup',
        tab: 'images',
        text: selectedText
      });
      break;
    case 'summary':
      chrome.runtime.sendMessage({
        action: 'openPopup',
        tab: 'summary',
        text: selectedText
      });
      break;
  }
}

// Listen for messages from the background script
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'showPopup') {
    const selection = window.getSelection();
    showActionsPopup(selection);
    
    // If a specific tab is requested, handle that action
    if (request.tab) {
      handleAction(request.tab);
    }
  }
});

// Listen for text selection
document.addEventListener('mouseup', (e) => {
  const selection = window.getSelection();
  if (selection.toString().trim()) {
    showActionsPopup(selection);
  } else if (popup && !popup.contains(e.target)) {
    popup.style.display = 'none';
  }
});

// Close popup when clicking outside
document.addEventListener('mousedown', (e) => {
  if (popup && !popup.contains(e.target)) {
    popup.style.display = 'none';
  }
});

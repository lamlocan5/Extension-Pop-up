document.addEventListener('DOMContentLoaded', function() {
  // Variables
  const API_BASE_URL = 'http://localhost:8000/api/v1';
  const tabs = document.querySelectorAll('.tab');
  const tabContents = document.querySelectorAll('.tab-content');
  const languageSelector = document.getElementById('target-language');
  const resultContainer = document.querySelector('.result-container');
  const loadingIndicator = document.querySelector('.loading-indicator');
  const errorMessage = document.querySelector('.error-message');
  
  let currentText = '';
  
  // Initialize
  init();
  
  // Functions
  function init() {
    setupTabs();
    setupLanguageSelector();
    
    // Get current selection from storage
    chrome.storage.local.get(['selectedText', 'activeTab'], function(result) {
      if (result.selectedText) {
        currentText = result.selectedText;
        
        // If activeTab exists, switch to it
        if (result.activeTab) {
          const tabToActivate = document.querySelector(`.tab[data-tab="${result.activeTab}"]`);
          if (tabToActivate) {
            tabToActivate.click();
          }
        }
        
        // Process the current text based on active tab
        processCurrentText();
      }
    });
    
    // Listen for messages from content script
    chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
      if (request.text) {
        currentText = request.text;
        
        // If a specific tab is requested, switch to it
        if (request.tab) {
          const tabToActivate = document.querySelector(`.tab[data-tab="${request.tab}"]`);
          if (tabToActivate) {
            tabToActivate.click();
          }
        }
        
        // Process the current text
        processCurrentText();
      }
    });
  }
  
  function setupTabs() {
    tabs.forEach(tab => {
      tab.addEventListener('click', () => {
        // Remove active class from all tabs and contents
        tabs.forEach(t => t.classList.remove('active'));
        tabContents.forEach(content => content.classList.remove('active'));
        
        // Add active class to current tab and content
        tab.classList.add('active');
        const tabName = tab.getAttribute('data-tab');
        document.getElementById(tabName).classList.add('active');
        
        // Save active tab to storage
        chrome.storage.local.set({ activeTab: tabName });
        
        // Process the current text for the new tab
        processCurrentText();
      });
    });
  }
  
  function setupLanguageSelector() {
    if (languageSelector) {
      languageSelector.addEventListener('change', () => {
        // Process translation with new language
        if (currentText) {
          translateText(currentText, languageSelector.value);
        }
      });
    }
  }
  
  function processCurrentText() {
    // Get active tab
    const activeTab = document.querySelector('.tab.active');
    if (!activeTab || !currentText) return;
    
    const tabName = activeTab.getAttribute('data-tab');
    
    // Process text based on tab
    switch (tabName) {
      case 'translation':
        translateText(currentText, languageSelector.value);
        break;
      case 'pronunciation':
        getPronunciation(currentText);
        break;
      case 'grammar':
        checkGrammar(currentText);
        break;
      case 'flashcards':
        prepareFlashcard(currentText);
        break;
      case 'images':
        searchImages(currentText);
        break;
      case 'summary':
        summarizeText(currentText);
        break;
    }
  }
  
  async function translateText(text, targetLanguage) {
    showLoading(true);
    clearError();
    
    try {
      const response = await fetch(`${API_BASE_URL}/translation`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          text: text,
          target_language: targetLanguage
        })
      });
      
      if (!response.ok) {
        throw new Error('Translation failed');
      }
      
      const data = await response.json();
      displayTranslation(data);
    } catch (error) {
      showError('Error translating text: ' + error.message);
    } finally {
      showLoading(false);
    }
  }
  
  function displayTranslation(data) {
    resultContainer.innerHTML = `
      <div class="translation-result">
        <div class="translated-text">${data.translated_text}</div>
        ${data.phonetics ? `<div class="phonetics">${data.phonetics}</div>` : ''}
        ${data.definitions && data.definitions.length > 0 ? `
          <div class="definitions">
            <h4>Definitions:</h4>
            <ul>
              ${data.definitions.map(def => `<li>${def}</li>`).join('')}
            </ul>
          </div>
        ` : ''}
      </div>
    `;
  }
  
  // Helper functions
  function showLoading(isLoading) {
    loadingIndicator.style.display = isLoading ? 'flex' : 'none';
  }
  
  function showError(message) {
    errorMessage.textContent = message;
    errorMessage.style.display = 'block';
  }
  
  function clearError() {
    errorMessage.textContent = '';
    errorMessage.style.display = 'none';
  }
  
  // Additional API functions would be implemented here
  // (getPronunciation, checkGrammar, prepareFlashcard, searchImages, summarizeText)
  
  // Placeholder implementations for other features
  async function getPronunciation(text) {
    showLoading(true);
    clearError();
    resultContainer.innerHTML = `<p>Pronunciation feature coming soon!</p>`;
    showLoading(false);
  }
  
  async function checkGrammar(text) {
    showLoading(true);
    clearError();
    resultContainer.innerHTML = `<p>Grammar checking feature coming soon!</p>`;
    showLoading(false);
  }
  
  async function prepareFlashcard(text) {
    showLoading(true);
    clearError();
    resultContainer.innerHTML = `<p>Flashcard feature coming soon!</p>`;
    showLoading(false);
  }
  
  async function searchImages(text) {
    showLoading(true);
    clearError();
    resultContainer.innerHTML = `<p>Image search feature coming soon!</p>`;
    showLoading(false);
  }
  
  async function summarizeText(text) {
    showLoading(true);
    clearError();
    resultContainer.innerHTML = `<p>Summarization feature coming soon!</p>`;
    showLoading(false);
  }
});

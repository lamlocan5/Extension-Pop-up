document.addEventListener('DOMContentLoaded', function() {
  const apiUrlInput = document.getElementById('api-url');
  const defaultLanguageSelect = document.getElementById('default-language');
  const saveBtn = document.getElementById('save-btn');
  const resetBtn = document.getElementById('reset-btn');
  const upgradeLink = document.getElementById('upgrade-link');
  
  // Load saved settings
  chrome.storage.sync.get({
    apiUrl: 'http://localhost:8000/api/v1',
    defaultLanguage: 'en',
    isVip: false
  }, function(items) {
    apiUrlInput.value = items.apiUrl;
    defaultLanguageSelect.value = items.defaultLanguage;
    
    // Update account status
    const accountStatus = document.getElementById('account-status');
    if (items.isVip) {
      accountStatus.innerHTML = '<p>You are a <strong>VIP user</strong> with access to all premium features.</p>';
    }
  });
  
  // Save settings
  saveBtn.addEventListener('click', function() {
    chrome.storage.sync.set({
      apiUrl: apiUrlInput.value,
      defaultLanguage: defaultLanguageSelect.value
    }, function() {
      // Show saved message
      const message = document.createElement('div');
      message.textContent = 'Settings saved!';
      message.style.color = '#4caf50';
      message.style.marginTop = '10px';
      message.style.fontWeight = 'bold';
      
      const actions = document.querySelector('.actions');
      actions.appendChild(message);
      
      // Remove message after 2 seconds
      setTimeout(() => {
        message.remove();
      }, 2000);
    });
  });
  
  // Reset to defaults
  resetBtn.addEventListener('click', function() {
    apiUrlInput.value = 'http://localhost:8000/api/v1';
    defaultLanguageSelect.value = 'en';
    
    chrome.storage.sync.set({
      apiUrl: 'http://localhost:8000/api/v1',
      defaultLanguage: 'en'
    });
  });
  
  // Handle upgrade link
  upgradeLink.addEventListener('click', function(e) {
    e.preventDefault();
    
    // Open upgrade page
    chrome.tabs.create({ url: 'https://your-domain.com/upgrade' });
  });
});

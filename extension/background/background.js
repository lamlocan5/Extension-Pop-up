// Initialize context menu
chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create({
    id: 'aiExtensionMenu',
    title: 'AI Tools',
    contexts: ['selection']
  });
  
  chrome.contextMenus.create({
    id: 'translationMenu',
    title: 'Translate selection',
    parentId: 'aiExtensionMenu',
    contexts: ['selection']
  });
  
  chrome.contextMenus.create({
    id: 'pronounceMenu',
    title: 'Pronounce selection',
    parentId: 'aiExtensionMenu',
    contexts: ['selection']
  });
  
  chrome.contextMenus.create({
    id: 'grammarMenu',
    title: 'Check grammar',
    parentId: 'aiExtensionMenu',
    contexts: ['selection']
  });
  
  chrome.contextMenus.create({
    id: 'flashcardMenu',
    title: 'Add to flashcards',
    parentId: 'aiExtensionMenu',
    contexts: ['selection']
  });
  
  chrome.contextMenus.create({
    id: 'summarizeMenu',
    title: 'Summarize selection',
    parentId: 'aiExtensionMenu',
    contexts: ['selection']
  });
});

// Handle context menu clicks
chrome.contextMenus.onClicked.addListener((info, tab) => {
  let action = '';
  
  switch (info.menuItemId) {
    case 'translationMenu':
      action = 'translation';
      break;
    case 'pronounceMenu':
      action = 'pronunciation';
      break;
    case 'grammarMenu':
      action = 'grammar';
      break;
    case 'flashcardMenu':
      action = 'flashcards';
      break;
    case 'summarizeMenu':
      action = 'summary';
      break;
  }
  
  if (action) {
    chrome.tabs.sendMessage(tab.id, {
      action: 'showPopup',
      tab: action,
      text: info.selectionText
    });
  }
});

// Listen for messages from content script
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'openPopup') {
    chrome.action.openPopup();
  }
});

// Fungsi Chat
function sendChat() {
  const input = document.getElementById('chat-input').value;
  if (input) {
    const chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += `<p>User: ${input}</p>`;
    // Simulasi respons GENESIS (bisa extend dengan fetch ke AI jika auth API)
    chatBox.innerHTML += `<p>GENESIS: Sudah diproses! Cek Issues untuk detail.</p>`;
    saveChatToLocal(input);
    document.getElementById('chat-input').value = '';
    chatBox.scrollTop = chatBox.scrollHeight;
  }
}

function saveChatToLocal(message) {
  let chats = JSON.parse(localStorage.getItem('genesisChats')) || [];
  chats.push(message);
  localStorage.setItem('genesisChats', JSON.stringify(chats));
}

function loadChats() {
  const chats = JSON.parse(localStorage.getItem('genesisChats')) || [];
  const chatBox = document.getElementById('chat-box');
  chats.forEach(msg => chatBox.innerHTML += `<p>User: ${msg}</p><p>GENESIS: Respons otomatis.</p>`);
}

function syncToDiscussions() {
  const chats = JSON.parse(localStorage.getItem('genesisChats')) || [];
  // Buka link untuk buat Discussion baru dengan chat history
  window.open('https://github.com/username/GENESIS/discussions/new?category=GENESIS%20Chat&title=Chat%20Sync&body=' + encodeURIComponent(chats.join('\n')), '_blank');
}

// Fungsi CRUD
let familyData = JSON.parse(localStorage.getItem('genesisFamily')) || [];
let assetsData = JSON.parse(localStorage.getItem('genesisAssets')) || [];

function addMember() {
  const name = document.getElementById('new-name').value;
  const role = document.getElementById('new-role').value;
  if (name && role) {
    familyData.push({name, role});
    updateFamilyList();
    saveData();
  }
}

function deleteMember() {
  const name = document.getElementById('new-name').value;
  familyData = familyData.filter(member => member.name !== name);
  updateFamilyList();
  saveData();
}

function updateFamilyList() {
  const list = document.getElementById('family-list');
  list.innerHTML = '';
  familyData.forEach(member => list.innerHTML += `<li>${member.name} - ${member.role}</li>`);
}

function addAsset() {
  const asset = document.getElementById('new-asset').value;
  if (asset) {
    assetsData.push(asset);
    updateAssetsList();
    saveData();
  }
}

function deleteAsset() {
  const asset = document.getElementById('new-asset').value;
  assetsData = assetsData.filter(a => a !== asset);
  updateAssetsList();
  saveData();
}

function updateAssetsList() {
  const list = document.getElementById('assets-list');
  list.innerHTML = '';
  assetsData.forEach(asset => list.innerHTML += `<li>${asset}</li>`);
}

function saveData() {
  localStorage.setItem('genesisFamily', JSON.stringify(familyData));
  localStorage.setItem('genesisAssets', JSON.stringify(assetsData));
  alert('Data disimpan di local storage!');
}

function loadData() {
  familyData = JSON.parse(localStorage.getItem('genesisFamily')) || [];
  assetsData = JSON.parse(localStorage.getItem('genesisAssets')) || [];
  updateFamilyList();
  updateAssetsList();
}

function syncToRepo() {
  // Buka link untuk edit file data di GitHub
  window.open('https://github.com/username/GENESIS/edit/main/data/family-members.json', '_blank');
}

function addPlugin() {
  const pluginName = prompt('Nama plugin baru:');
  if (pluginName) {
    // Buka link untuk buat folder plugin baru
    window.open('https://github.com/username/GENESIS/new/main/plugins/' + pluginName, '_blank');
  }
}

// Init load
loadData();
loadChats();

let funFacts = [
  "Fun fact: VIRAI mining with PLTS saves 30% energy, bro! 🌞",
  "Did you know? VIRAI swaps take <1 sec on Solana! 🚀",
  "Pro tip: Jual NFT GENESIS di Magic Eden, dompetmu bakal gemuk!"
];

let token = localStorage.getItem('jwt_token');

if (token) {
  document.getElementById('auth-section').style.display = 'none';
  document.getElementById('chat-section').style.display = 'block';
  document.getElementById('friends-section').style.display = 'block';
  document.getElementById('private-chat-section').style.display = 'block';
  document.getElementById('group-chat-section').style.display = 'block';
  document.getElementById('quick-actions').style.display = 'block';
  document.getElementById('wallet-section').style.display = 'block';
  document.getElementById('analytics-section').style.display = 'block';
}

async function specialAccess() {
  const access_code = document.getElementById('access-code').value;
  const response = await fetch('http://localhost:8000/api/special_access', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ access_code })
  }).then(res => res.json());
  if (response.status === 'logged_in') {
    localStorage.setItem('jwt_token', response.token);
    token = response.token;
    document.getElementById('auth-section').style.display = 'none';
    document.getElementById('chat-section').style.display = 'block';
    document.getElementById('friends-section').style.display = 'block';
    document.getElementById('private-chat-section').style.display = 'block';
    document.getElementById('group-chat-section').style.display = 'block';
    document.getElementById('quick-actions').style.display = 'block';
    document.getElementById('wallet-section').style.display = 'block';
    document.getElementById('analytics-section').style.display = 'block';
    document.getElementById('predictions').innerText = `Special Access: ${response.message} as ${response.email}`;
  } else {
    document.getElementById('predictions').innerText = `Special Access Failed: ${response.message}`;
  }
}

async function register() {
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;
  const username = document.getElementById('username').value;
  const response = await fetch('http://localhost:8000/api/register', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password, username })
  }).then(res => res.json());
  document.getElementById('predictions').innerText = `Register: ${response.message}. Wallet: ${response.wallet_public_key}`;
}

async function verifyOTP() {
  const email = document.getElementById('email').value;
  const otp = document.getElementById('otp').value;
  const response = await fetch('http://localhost:8000/api/verify_otp', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, otp })
  }).then(res => res.json());
  document.getElementById('predictions').innerText = `OTP: ${response.message}`;
}

async function login() {
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;
  const response = await fetch('http://localhost:8000/api/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password })
  }).then(res => res.json());
  if (response.status === 'logged_in') {
    localStorage.setItem('jwt_token', response.token);
    token = response.token;
    document.getElementById('auth-section').style.display = 'none';
    document.getElementById('chat-section').style.display = 'block';
    document.getElementById('friends-section').style.display = 'block';
    document.getElementById('private-chat-section').style.display = 'block';
    document.getElementById('group-chat-section').style.display = 'block';
    document.getElementById('quick-actions').style.display = 'block';
    document.getElementById('wallet-section').style.display = 'block';
    document.getElementById('analytics-section').style.display = 'block';
    document.getElementById('predictions').innerText = `Logged in as ${email}!`;
  } else {
    document.getElementById('predictions').innerText = `Login failed: ${response.message}`;
  }
}

async function addFriend() {
  const friend_email = document.getElementById('friend-email').value;
  const response = await fetch('http://localhost:8000/api/add_friend', {
    method: 'POST',
    headers: { 
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify({ friend_email })
  }).then(res => res.json());
  document.getElementById('predictions').innerText = `Friend Request: ${response.status} to ${response.friend}`;
}

async function acceptFriend() {
  const friend_email = document.getElementById('friend-email').value;
  const response = await fetch('http://localhost:8000/api/accept_friend', {
    method: 'POST',
    headers: { 
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify({ friend_email })
  }).then(res => res.json());
  document.getElementById('predictions').innerText = `Friend Accepted: ${response.status} with ${response.friend}`;
}

async function sendPrivateMessage() {
  const to_user = document.getElementById('to-user').value;
  const message = document.getElementById('private-message').value;
  const response = await fetch('http://localhost:8000/api/send_private_chat', {
    method: 'POST',
    headers: { 
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify({ to_user, message })
  }).then(res => res.json());
  document.getElementById('predictions').innerText = `Message: ${response.status} to ${response.to_user}`;
}

async function createGroup() {
  const group_name = document.getElementById('group-name').value;
  const members = document.getElementById('group-members').value.split(',');
  const response = await fetch('http://localhost:8000/api/create_group', {
    method: 'POST',
    headers: { 
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify({ group_name, members })
  }).then(res => res.json());
  document.getElementById('predictions').innerText = `Group Created: ${response.group_id}`;
}

async function sendGroupMessage() {
  const group_id = document.getElementById('group-id').value;
  const message = document.getElementById('group-message').value;
  const response = await fetch('http://localhost:8000/api/send_group_chat', {
    method: 'POST',
    headers: { 
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify({ group_id, message })
  }).then(res => res.json());
  document.getElementById('predictions').innerText = `Group Message: ${response.status} in ${group_id}`;
}

async function getMessages(type) {
  let url = type === 'private' ? 
    `http://localhost:8000/api/get_private_chat?user=${localStorage.getItem('user_email')}&to_user=${document.getElementById('to-user').value}` :
    `http://localhost:8000/api/get_group_chat?group_id=${document.getElementById('group-id').value}`;
  const response = await fetch(url, {
    headers: { 'Authorization': `Bearer ${token}` }
  }).then(res => res.json());
  const chatBox = type === 'private' ? document.getElementById('private-chat') : document.getElementById('group-chat');
  chatBox.innerHTML = response.chats.map(c => `<p>${c.from}: ${c.message}</p>`).join('');
}

async function sendChat() {
  const input = document.getElementById('chat-input').value;
  const userId = localStorage.getItem('genesis_userId') || 'user1';
  const response = await fetch('http://localhost:8000/api/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ input, userId })
  }).then(res => res.json());
  const chatBox = document.getElementById('chat-box');
  chatBox.innerHTML += `<p>User: ${input}</p><p>GENESIS: ${response.response}</p>`;
  document.getElementById('fun-fact').innerText = funFacts[Math.floor(Math.random() * funFacts.length)];
}

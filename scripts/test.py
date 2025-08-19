import unittest
from scripts.auth_engine import AuthEngine
from scripts.friend_engine import FriendEngine
from scripts.chat_engine import ChatEngine

class TestGENESIS(unittest.TestCase):
    def test_auth(self):
        auth = AuthEngine()
        result = auth.register('test@example.com', 'password123', 'testuser')
        self.assertEqual(result['status'], 'registered')
    
    def test_friend(self):
        friend = FriendEngine()
        result = friend.add_friend('user1', 'friend@example.com')
        self.assertIn(result['status'], ['request_sent', 'error'])
    
    def test_chat(self):
        chat = ChatEngine()
        result = chat.send_private_chat('user1', 'user2', 'Yo, bro!')
        self.assertEqual(result['status'], 'sent')

if __name__ == '__main__':
    unittest.main()

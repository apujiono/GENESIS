from pymongo import MongoClient
from datetime import datetime

class FriendEngine:
    def __init__(self):
        self.mongo_client = MongoClient('mongodb://mongodb:27017/')
        self.db = self.mongo_client['genesis']

    def add_friend(self, user_id, friend_email):
        friend = self.db.users.find_one({'email': friend_email})
        if not friend:
            return {'status': 'error', 'message': 'Friend not found'}
        if friend_email in self.get_friends(user_id):
            return {'status': 'error', 'message': 'Already friends'}
        self.db.friend_requests.insert_one({'from': user_id, 'to': friend_email, 'status': 'pending', 'timestamp': str(datetime.now())})
        return {'status': 'request_sent', 'friend': friend_email}

    def accept_friend(self, user_id, friend_email):
        request = self.db.friend_requests.find_one({'from': friend_email, 'to': user_id, 'status': 'pending'})
        if not request:
            return {'status': 'error', 'message': 'Request not found'}
        self.db.friend_requests.update_one({'_id': request['_id']}, {'$set': {'status': 'accepted'}})
        self.db.friends.insert_one({'user': user_id, 'friend': friend_email, 'timestamp': str(datetime.now())})
        self.db.friends.insert_one({'user': friend_email, 'friend': user_id, 'timestamp': str(datetime.now())})
        return {'status': 'accepted', 'friend': friend_email}

    def get_friends(self, user_id):
        friends = self.db.friends.find({'user': user_id})
        return [f['friend'] for f in friends]

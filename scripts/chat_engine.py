from pymongo import MongoClient
from datetime import datetime
from nacl.secret import SecretBox
from nacl.utils import random
from scripts.web3_engine import Web3Engine

class ChatEngine:
    def __init__(self):
        self.mongo_client = MongoClient('mongodb://mongodb:27017/')
        self.db = self.mongo_client['genesis']
        self.secret_key = random(SecretBox.KEY_SIZE)
        self.web3_engine = Web3Engine()

    def send_private_chat(self, from_user, to_user, message):
        box = SecretBox(self.secret_key)
        encrypted = box.encrypt(message.encode())
        self.db.private_chats.insert_one({'from': from_user, 'to': to_user, 'message': encrypted.hex(), 'timestamp': str(datetime.now())})
        return {'status': 'sent'}

    def get_private_chat(self, user, to_user):
        chats = self.db.private_chats.find({'$or': [{'from': user, 'to': to_user}, {'from': to_user, 'to': user}]})
        box = SecretBox(self.secret_key)
        decrypted = []
        for chat in chats:
            decrypted.append({'from': chat['from'], 'message': box.decrypt(bytes.fromhex(chat['message'])).decode()})
        return {'chats': decrypted}

    def create_group(self, creator, group_name, members):
        group = {'creator': creator, 'name': group_name, 'members': members, 'timestamp': str(datetime.now())}
        self.db.groups.insert_one(group)
        return {'group_id': str(group['_id'])}  # Gunakan ObjectId sebagai group_id

    def send_group_chat(self, from_user, group_id, message):
        box = SecretBox(self.secret_key)
        encrypted = box.encrypt(message.encode())
        self.db.group_chats.insert_one({'from': from_user, 'group_id': group_id, 'message': encrypted.hex(), 'timestamp': str(datetime.now())})
        return {'status': 'sent'}

    def get_group_chat(self, group_id):
        chats = self.db.group_chats.find({'group_id': group_id})
        box = SecretBox(self.secret_key)
        decrypted = []
        for chat in chats:
            decrypted.append({'from': chat['from'], 'message': box.decrypt(bytes.fromhex(chat['message'])).decode()})
        return {'chats': decrypted}

    def send_tip(self, from_user, to_user, amount):
        self.web3_engine.transfer_virai(from_user, to_user, amount)
        return {'status': 'tip_sent', 'amount': amount}

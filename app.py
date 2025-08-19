from flask import Flask, request, jsonify
import json
from pymongo import MongoClient
from scripts.process_data import process_chat, process_crud
from scripts.ml_predict import predict_future
from scripts.sentiment import analyze_sentiment
from scripts.tasks import run_upgrade
from scripts.kafka_producer import produce_message
from scripts.virai_engine import VIRAI
from scripts.mining_engine import MiningEngine
from scripts.web3_engine import Web3Engine
from scripts.nft_engine import NFTEngine
from scripts.wallet_engine import WalletEngine
from scripts.auth_engine import AuthEngine
from scripts.friend_engine import FriendEngine
from scripts.chat_engine import ChatEngine
from scripts.help_engine import HelpEngine
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
mongo_client = MongoClient('mongodb://localhost:27017')  # Ganti dengan URL cloud
db = mongo_client['genesis']
virai = VIRAI()
mining_engine = MiningEngine()
web3_engine = Web3Engine()
nft_engine = NFTEngine()
wallet_engine = WalletEngine()
auth_engine = AuthEngine()
friend_engine = FriendEngine()
chat_engine = ChatEngine()
help_engine = HelpEngine()

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    username = data.get('username')
    return jsonify(auth_engine.register(email, password, username))

@app.route('/api/verify_otp', methods=['POST'])
def verify_otp():
    data = request.json
    email = data.get('email')
    otp = data.get('otp')
    return jsonify(auth_engine.verify_otp(email, otp))

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    return jsonify(auth_engine.login(email, password))

@app.route('/api/add_friend', methods=['POST'])
def add_friend():
    data = request.json
    user_id = data.get('user_id')
    friend_email = data.get('friend_email')
    return jsonify(friend_engine.add_friend(user_id, friend_email))

@app.route('/api/accept_friend', methods=['POST'])
def accept_friend():
    data = request.json
    user_id = data.get('user_id')
    friend_email = data.get('friend_email')
    return jsonify(friend_engine.accept_friend(user_id, friend_email))

@app.route('/api/friend_list', methods=['GET'])
def friend_list():
    user_id = request.args.get('user_id')
    return jsonify(friend_engine.get_friends(user_id))

@app.route('/api/send_private_chat', methods=['POST'])
def send_private_chat():
    data = request.json
    from_user = data.get('from_user')
    to_user = data.get('to_user')
    message = data.get('message')
    return jsonify(chat_engine.send_private_chat(from_user, to_user, message))

@app.route('/api/create_group', methods=['POST'])
def create_group():
    data = request.json
    creator = data.get('creator')
    group_name = data.get('group_name')
    members = data.get('members')
    return jsonify(chat_engine.create_group(creator, group_name, members))

@app.route('/api/send_group_chat', methods=['POST'])
def send_group_chat():
    data = request.json
    from_user = data.get('from_user')
    group_id = data.get('group_id')
    message = data.get('message')
    return jsonify(chat_engine.send_group_chat(from_user, group_id, message))

@app.route('/api/get_messages', methods=['GET'])
def get_messages():
    from_user = request.args.get('from_user')
    to_user = request.args.get('to_user')
    group_id = request.args.get('group_id')
    return jsonify(chat_engine.get_messages(from_user, to_user, group_id))

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    input_text = data.get('input', '')
    user_id = data.get('userId', 'user1')
    cache_key = f"chat:{user_id}:{input_text}"
    cached = redis_client.get(cache_key)
    if cached:
        return jsonify({'response': cached.decode(), 'source': 'cache'})
    
    if input_text == '/help':
        response = help_engine.get_help()
        return jsonify({'response': response, 'source': 'help'})
    
    # Lanjutan seperti di app.py sebelumnya

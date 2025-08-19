import json
import bcrypt
import jwt
import smtplib
from email.mime.text import MIMEText
from pymongo import MongoClient
from datetime import datetime, timedelta
import random
import string
from scripts.wallet_engine import WalletEngine

class AuthEngine:
    def __init__(self):
        self.mongo_client = MongoClient('mongodb://mongodb:27017/')
        self.db = self.mongo_client['genesis']
        self.wallet_engine = WalletEngine()
        self.jwt_secret = 'YOUR_JWT_SECRET'  # Ganti dengan secret aman
        self.smtp_server = 'smtp.gmail.com'
        self.smtp_port = 587
        self.smtp_user = 'your-email@gmail.com'  # Ganti dengan emailmu
        self.smtp_pass = 'your-app-password'  # Ganti dengan app password Gmail
        self.otp_expiry = timedelta(minutes=10)

    def register(self, email, password, username):
        if self.db.users.find_one({'email': email}):
            return {'status': 'error', 'message': 'Email already registered'}
        
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        otp = ''.join(random.choices(string.digits, k=6))
        user = {
            'email': email,
            'username': username,
            'password': hashed_password,
            'otp': otp,
            'otp_timestamp': str(datetime.now()),
            'verified': False,
            'timestamp': str(datetime.now())
        }
        self.db.users.insert_one(user)
        self.send_otp(email, otp)
        wallet = self.wallet_engine.create_wallet(email)
        return {'status': 'registered', 'message': 'OTP sent to email', 'wallet_public_key': wallet['public_key']}

    def send_otp(self, email, otp):
        msg = MIMEText(f"Your GENESIS OTP is {otp}. Expires in 10 minutes.")
        msg['Subject'] = 'GENESIS OTP Verification'
        msg['From'] = self.smtp_user
        msg['To'] = email
        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.starttls()
        server.login(self.smtp_user, self.smtp_pass)
        server.sendmail(self.smtp_user, email, msg.as_string())
        server.quit()

    def verify_otp(self, email, otp):
        user = self.db.users.find_one({'email': email})
        if user and user['otp'] == otp and (datetime.now() - datetime.fromisoformat(user['otp_timestamp'])) < self.otp_expiry:
            self.db.users.update_one({'email': email}, {'$set': {'verified': True}})
            return {'status': 'verified', 'message': 'Email verified'}
        return {'status': 'error', 'message': 'Invalid or expired OTP'}

    def login(self, email, password):
        user = self.db.users.find_one({'email': email})
        if not user or not user['verified']:
            return {'status': 'error', 'message': 'User not found or unverified'}
        if bcrypt.checkpw(password.encode(), user['password'].encode()):
            token = jwt.encode({'email': email, 'exp': datetime.utcnow() + timedelta(hours=24)}, self.jwt_secret, algorithm='HS256')
            return {'status': 'logged_in', 'token': token}
        return {'status': 'error', 'message': 'Invalid password'}

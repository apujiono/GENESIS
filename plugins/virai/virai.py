import json
from datetime import datetime

class VIRAI:
    def __init__(self):
        self.wallets = {}  # Dummy wallet storage
        self.transactions = []

    def create_wallet(self, email):
        public_key = f"virai_public_key_{email}"
        private_key = f"virai_private_key_{email}"
        self.wallets[email] = {'public_key': public_key, 'private_key': private_key, 'balance': 5}
        return {'public_key': public_key}

    def transfer(self, from_email, to_email, amount):
        if from_email in self.wallets and self.wallets[from_email]['balance'] >= amount:
            self.wallets[from_email]['balance'] -= amount
            self.wallets[to_email]['balance'] += amount
            self.transactions.append({
                'from': from_email,
                'to': to_email,
                'amount': amount,
                'timestamp': str(datetime.now())
            })
            return {'status': 'transferred', 'amount': amount}
        return {'status': 'error', 'message': 'Insufficient balance'}

    def get_balance(self, email):
        return self.wallets.get(email, {'balance': 0})['balance']

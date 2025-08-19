import json
from datetime import datetime

class WalletEngine:
    def __init__(self):
        self.wallets = {}  # Dummy in-memory, ganti dengan blockchain real

    def create_wallet(self, email):
        public_key = 'dummy_public_key_' + email
        private_key = 'dummy_private_key_' + email
        self.wallets[email] = {'public_key': public_key, 'private_key': private_key, 'balance': 5}  # Bonus 5 VIRAI
        return {'public_key': public_key}

    def transfer_virai(self, from_email, to_email, amount):
        if from_email in self.wallets and self.wallets[from_email]['balance'] >= amount:
            self.wallets[from_email]['balance'] -= amount
            self.wallets[to_email]['balance'] += amount
            return {'status': 'transferred', 'amount': amount}
        return {'status': 'error', 'message': 'Insufficient balance'}

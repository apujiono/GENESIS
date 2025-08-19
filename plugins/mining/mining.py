import random
from datetime import datetime

class MiningEngine:
    def start_mining(self, coin):
        hash_rate = random.randint(100, 1000)
        reward = hash_rate * 0.001
        return {
            'status': 'mining_started',
            'coin': coin,
            'hash_rate': hash_rate,
            'reward': reward,
            'timestamp': str(datetime.now())
        }

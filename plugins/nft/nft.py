import json
from datetime import datetime

class NFTEngine:
    def generate_nft(self, data_type, user_id):
        nft_id = f"nft_{user_id}_{data_type}_{int(datetime.now().timestamp())}"
        return {
            'nft_id': nft_id,
            'data_type': data_type,
            'owner': user_id,
            'timestamp': str(datetime.now())
        }

    def sell_nft(self, nft_id, price):
        return {'status': 'listed', 'nft_id': nft_id, 'price': price}

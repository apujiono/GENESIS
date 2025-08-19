import json
from datetime import datetime

class NFTEngine:
    def generate_nft(self, data_type, user_id):
        nft_id = f"nft_{user_id}_{data_type}_{int(datetime.now().timestamp())}"
        with open('data/nft_log.json', 'a') as f:
            json.dump({
                'nft_id': nft_id,
                'data_type': data_type,
                'owner': user_id,
                'timestamp': str(datetime.now())
            }, f)
        return {'nft_id': nft_id, 'data_type': data_type, 'owner': user_id}

    def sell_nft(self, nft_id, price):
        return {'status': 'listed', 'nft_id': nft_id, 'price': price}

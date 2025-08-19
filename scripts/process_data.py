import json
from datetime import datetime

def process_chat(input_text, user_id):
    cache_file = 'data/cache.json'
    with open(cache_file, 'r') as f:
        cache = json.load(f)
    cache_key = f"chat:{user_id}:{input_text}"
    if cache_key in cache['cache']:
        return cache['cache'][cache_key]
    
    response = f"Processed input for {user_id}: {input_text}"
    cache['cache'][cache_key] = response
    with open(cache_file, 'w') as f:
        json.dump(cache, f, indent=2)
    return response

def process_crud(collection, operation, data):
    with open(f'data/{collection}.json', 'r') as f:
        db = json.load(f)
    if operation == 'create':
        db[collection].append(data)
    elif operation == 'read':
        return db[collection]
    elif operation == 'update':
        for i, item in enumerate(db[collection]):
            if item['id'] == data['id']:
                db[collection][i] = data
                break
    elif operation == 'delete':
        db[collection] = [item for item in db[collection] if item['id'] != data['id']]
    with open(f'data/{collection}.json', 'w') as f:
        json.dump(db, f, indent=2)
    return {'status': f'{operation} success'}

import json
import random
import numpy as np
from sentence_transformers import SentenceTransformer

def compute_embeddings(text):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    return model.encode(text).tolist()

def evolve_code(memory_path):
    memory = json.load(open(memory_path))
    history = memory['history'][-10:]
    embeddings = [compute_embeddings(h['user']) for h in history]
    avg_embedding = np.mean(embeddings, axis=0).tolist() if embeddings else [0] * 384
    
    new_feature = random.choice([
        'optimize task priority',
        'enhance ML prediction',
        'add plugin for creative solutions'
    ]) if not history else f"improve {history[-1]['user'].split()[0]} handling"
    
    memory['learning_log'].append({
        'upgrade': f"Upgrade #{len(memory['learning_log']) + 1}: {new_feature}",
        'embedding': avg_embedding
    })
    memory['state'] = 'evolving'
    with open(memory_path, 'w') as f:
        json.dump(memory, f, indent=2)
    print(f"Evolution: {new_feature}")

if __name__ == '__main__':
    evolve_code('memory/genesis-memory.json')

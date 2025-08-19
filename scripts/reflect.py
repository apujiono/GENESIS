import json
from datetime import datetime

def reflect_on_memory(memory_path):
    memory = json.load(open(memory_path))
    history = memory['history'][-5:]
    reflection = f"Reflected on {len(history)} interactions: {' '.join([h['user'][:20] for h in history])}"
    memory['history'].append({
        'reflection': reflection,
        'timestamp': str(datetime.now())
    })
    with open(memory_path, 'w') as f:
        json.dump(memory, f, indent=2)
    return reflection

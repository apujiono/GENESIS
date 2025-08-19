import numpy as np
from sentence_transformers import SentenceTransformer

def predict_future(data):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(data)
    prediction = np.mean(embeddings, axis=0).tolist()
    return {'prediction': prediction, 'confidence': 0.95}

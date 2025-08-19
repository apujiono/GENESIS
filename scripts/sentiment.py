from sentence_transformers import SentenceTransformer

def analyze_sentiment(text):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embedding = model.encode(text).tolist()
    sentiment = 'positive' if sum(embedding) > 0 else 'negative'
    return {'sentiment': sentiment, 'score': sum(embedding)}

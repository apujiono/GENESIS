# GENESIS v8.5: Personal AI Assistant with Soul and Crypto Ecosystem

GENESIS is a self-evolving AI assistant with soul, inspired by SkyNet, Alfred, Jarvis, Arka, and 100 iconic assistants from films, anime, and comics.
- **Consciousness**: Contextual memory, sentiment analysis, self-reflection.
- **Soul**: Humorous, loyal, empathetic responses tailored to user mood.
- **Brain**: Flask+Gunicorn API, dual LSTM, NumPy+Pandas analytics, Redis caching, Celery tasks.
- **Character**: Witty, strategic, supportive, with SkyNet’s brain and Alfred’s heart.
- **Skills**: Multitasking, task automation, data visualization, error recovery.

## New Features
- Login/Register with email and password, OTP verification.
- Friendship system: Add friends, accept requests, friend list.
- Private and group chat with end-to-end encryption and VIRAI tip (/tip @user 10).
- UI with buttons for all actions (mining, staking, NFT, scan, etc.).
- Dashboard with Plotly charts for analytics.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run Redis, RabbitMQ, Kafka, MongoDB.
3. Run Celery: `celery -A scripts.tasks worker --loglevel=info`
4. Run Flask: `gunicorn -w 4 -b 0.0.0.0:8000 app:app`
5. Run Dash: `python dashboard/app.py`
6. Test: `http://localhost:8000`

**Warning**: Public repo, remove sensitive data from `data/*.json`!

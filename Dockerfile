FROM python:3.10-slim
WORKDIR /app
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*
RUN python3.10 -m venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir --timeout 900 -r requirements.txt
COPY . .
CMD ["python", "main.py"] # Adjust to your app’s entry point
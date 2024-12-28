FROM python:3.11-slim

WORKDIR /app

COPY . /app
RUN pip install uv
RUN uv venv
RUN uv sync
EXPOSE 8000
CMD ["sh", "-c", "source .venv/bin/activate && fastapi run src/ --port 8000"]

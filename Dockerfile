FROM python:3-alpine

COPY main.rickroll .
COPY src-py .

CMD ["timeout", "5", "python3", "RickRoll.py", "main.rickroll"]

FROM python:3.8-slim

RUN pip install Flask

COPY form.html .
COPY app.py /app.py

CMD ["python", "/app.py"]


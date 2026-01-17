FROM python:3.12-slim
WORKDIR /app
RUN pip install psycopg2-binary
COPY ethan.py .
CMD ["python", "ethan.py"]

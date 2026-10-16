
FROM python:3.12-slim

WORKDIR /app

COPY lambda_app/ ./lambda_app/
COPY test_calculator.py .

ENV PYTHONPATH=/app

CMD ["python", "-m", "unittest", "discover", "-v"]

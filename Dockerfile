
FROM python:3.12-slim

WORKDIR /app

COPY lambda_app/calculator.py ./calculator.py
COPY test_calculator.py ./test_calculator.py

CMD ["python", "-m", "unittest", "-v"]


FROM python:3.12-slim

WORKDIR /app

COPY calculator.py ./calculator.py
COPY test_calculator.py ./test_calculator.py

CMD ["python", "-m", "unittest", "-v"]

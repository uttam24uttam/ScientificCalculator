FROM python:3.12-slim

WORKDIR /app


COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /app/src

ENV PYTHONPATH=/app

# Define the command to run the application
CMD ["python", "-m", "src.calculator_app.calculator"]
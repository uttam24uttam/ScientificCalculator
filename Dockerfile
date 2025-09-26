# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy project files into container
COPY . .

# Install dependencies if requirements.txt exists
RUN pip install --no-cache-dir -r requirements.txt || echo "No requirements file, skipping"

# Default command to run calculator
CMD ["python", "calculator.py"]


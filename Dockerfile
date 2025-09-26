FROM python:3.12-slim

#working directory
WORKDIR /app

#Copying project files into container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt || echo "No requirements file, skipping"

# run calculator
CMD ["python", "calculator.py"]


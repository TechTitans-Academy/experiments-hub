# Base image
FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Copy requirements and install
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app/ .

# Run the app
CMD ["python", "app.py"]

# Use a clean base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Expose the port used by Flask
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]

